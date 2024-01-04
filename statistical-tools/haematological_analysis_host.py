# this script performs the analysis of variance from a dataset based in the localhost
# it outputs the relative p value and perform post hoc tests based on the distribution normality
# as additional output it creates non-detailed graph previews to give data distribution insight

import mysql.connector
import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt
from scikit_posthocs import posthoc_dunn

# connection to the dataset
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = db.cursor()

print("\nINTERGENOTYPE ANALYSIS")

# choose the age of the experimental subjects you want to compare
age = input("Age: ")

# choose the parameter to analyze
parameter = ["rcb", "hgb", "hct", "mcv", "mch", "mchc", "rdw_sd", "ret_num", "ret_perc", "plt", "wbc", "ret_he"]

x_axis = ["KO", "HE", "WT"]
y_axis = []
yerr = []

print("Results: ")
# selection of data of interest from the dataset
for i in range(len(parameter)):
    sql1 = f"SELECT {parameter[i]} FROM ematologici_he WHERE genotype = 'KO' AND age = {age} "
    cursor.execute(sql1)
    result1 = cursor.fetchall()

    sql2 = f"SELECT {parameter[i]} FROM ematologici_he WHERE genotype = 'HE' AND age = {age} "
    cursor.execute(sql2)
    result2 = cursor.fetchall()

    sql3 = f"SELECT {parameter[i]} FROM ematologici_he WHERE genotype = 'WT' AND age = {age} "
    cursor.execute(sql3)
    result3 = cursor.fetchall()

    data1 = [float(i[0]) for i in result1]
    data2 = [float(i[0]) for i in result2]
    data3 = [float(i[0]) for i in result3]
    data = [data1, data2, data3]

# normality test: do the data passed normality test for Gaussian distribution?
    if len(data1) < 3:
        pvalue1 = 1
    else:
        stat1, pvalue1 = ss.shapiro(data1)

    if len(data2) < 3:
        pvalue2 = 1
    else:
        stat2, pvalue2 = ss.shapiro(data2)

    if len(data3) < 3:
        pvalue3 = 1
    else:
        stat3, pvalue3 = ss.shapiro(data3)

# Analysis of Variance
    if (pvalue1 > 0.05) and (pvalue2 > 0.05) and (pvalue3 > 0.05):
        f_value, p_value = ss.f_oneway(data1, data2, data3)
        if p_value < 0.0001:
            print((f"  {parameter[i]}: ANOVA p-value < 0.0001"))
        elif p_value < 0.05:
            print(f"  {parameter[i]}: ANOVA p-value=  %.4f" % p_value)
        else:
            print(f"  {parameter[i]}: n.s (p = %.4f)" % p_value)

    else:
        h_statistic, p_value = ss.kruskal(
            data1, data2, data3, nan_policy='omit')
        if p_value < 0.0001:
            print(f"  {parameter[i]}: Kruskal-Wallis < 0.0001")
        elif p_value < 0.05:
            print(f"  {parameter[i]}: Kruskal-Wallis = %.4f" % p_value)
        else:
            print(f"  {parameter[i]}: ns (Kruskal-Wallis = %.4f)" % p_value)


# post hoc test, multiple comparisons
    if (pvalue1 > 0.05) and (pvalue2 > 0.05) and (pvalue3 > 0.05):
        post_hoc = ss.tukey_hsd(data1, data2, data3)
        if post_hoc.pvalue[0, 1] < 0.0001:
            print("    KO vs. HE < 0.0001")
        elif post_hoc.pvalue[0, 1] < 0.05:
            print("    KO vs. HE = %.4f" % post_hoc.pvalue[0, 1])
        else:
            print("    KO vs HE = ns")

        if post_hoc.pvalue[0, 2] < 0.0001:
            print("    KO vs. WT < 0.0001")
        elif post_hoc.pvalue[0, 2] < 0.05:
            print("    KO vs. WT = %.4f" % post_hoc.pvalue[0, 2])
        else:
            print("    KO vs WT = ns")

        if post_hoc.pvalue[1, 2] < 0.0001:
            print("    HE vs. WT < 0.0001\n")
        elif post_hoc.pvalue[1, 2] < 0.05:
            print("    HE vs. WT = %.4f\n" % post_hoc.pvalue[1, 2])
        else:
            print("    HE vs WT = ns\n")

    else:
        post_hoc = posthoc_dunn(data)
        if post_hoc.values[0, 1] < 0.0001:
            print("    KO vs. HE < 0.0001")
        elif post_hoc.values[0, 1] < 0.05:
            print("    KO vs. HE = %.4f" % post_hoc.values[0, 1])
        else:
            print("    KO vs HE = ns")

        if post_hoc.values[0, 2] < 0.0001:
            print("    KO vs. WT < 0.0001")
        elif post_hoc.values[0, 2] < 0.05:
            print("    KO vs. WT = %.4f" % post_hoc.values[0, 2])
        else:
            print("    KO vs WT = ns")

        if post_hoc.values[1, 2] < 0.0001:
            print("    HE vs. WT < 0.0001\n")
        elif post_hoc.values[1, 2] < 0.05:
            print("    HE vs. WT = %.4f\n" % post_hoc.values[1, 2])
        else:
            print("    HE vs WT = ns\n")

# draw the graph
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    mean3 = np.mean(data3)

    sem1 = np.std(data1, ddof=1) / np.sqrt(np.size(data1))
    sem2 = np.std(data2, ddof=1) / np.sqrt(np.size(data2))
    sem3 = np.std(data3, ddof=1) / np.sqrt(np.size(data3))

    y_axis.append([mean1, mean2, mean3])
    yerr.append([sem1, sem2, sem3])

a = []
fig, axs = plt.subplots(nrows=3, ncols=4, sharex=True)
fig.suptitle(f'Age: {age} months', fontsize=16)
plt.subplots_adjust(hspace=0.4)
for i, row in enumerate(axs):
    for j, ax in enumerate(row):
        a.append(ax)

for i, ax in enumerate(a):
    ax.errorbar(x_axis, y_axis[i], yerr[i], fmt='o', linewidth=2, capsize=6)
    ax.set_title(f"{parameter[i]}")
    ax.set(yticklabels=[])

plt.show()
