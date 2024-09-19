# statistical-tools
:warning: **WARNING:** This script was the first one I created over a year ago, before I began studying data analysis with Python. I now realize that the analysis could have been performed more efficiently and less clumsily using NumPy and Pandas. Nonetheless, it was my first real programming challenge, and I am very proud to have overcome it with the limited knowledge I had at that time.<br><br>
Here I have collected two scripts written in Python and SQL, designed for analyzing data related to physiological parameters derived from experimental measurements. These tools were created to expedite the statistical analysis process, extracting and sorting data from tabular-format datasets, in my specific case studies.<br>
<br>
Hoping they can be useful to you as example from which collecting inspiration for your specific cases.<br>
<br>
**\*\*\* DISCLAIMER \*\*\*** these scripts were written to help me in my laboratory data analysis work. The example I used to explain how they work show totally random values, in any case each data contained here should be trated as confidential. Thank you for the support.<br>
<br>
## How it works :wrench: <br>
Both scripts are designated to collect specific data from my dataset (namely, haematological_dataset.db). The difference is that data are stored in a local database located in the project folder (not present in the repository) in *haematological_analysis_local_folder case*; while in *haematological_analysis_host case*, data are stored on a database located on an host (in my case, the localhost).<br><br>
## What was my problem? :mag:<br>
The type of dataset I needed to analyze was relatively simple.<br><br> 
In my case, the dataset was made from haematological analysis performed on blood sample from different subjects (both male and female) at different timepoints (6, 12, 18 and 24 months). These subjects were grouped on the basis of genotype (knock-out, KO; heterozygous, HE; and wild-type, WT).<br><br> 
**The haematological parameters measured are:** red blood cell count, rcb; haemoglobin level, hgb; hematocrit, hct; mean corpuscular volume, mcv; mean corpuscular haemoglobin, mch; mean corpuscular haemoglobin concentration, mchc; red cell distribution width - standard deviation, rdw_sd; reticulocyte number, ret_num; reticulocyte percentage, ret_perc; platelet count, plt; white blood cell count, wbc; reticulocyte haemoglobin content, ret_he.<br><br> 
An example of such dataset is depicted in figure 1, left panel.<br><br> 
My goal was to group data at different timepoints on the basis of the parameter considered (see figure 1, right panels), in order to perform variance analysis and post hoc test on the three genotypes, using Prism GraphPad.<br><br> 
Given the amount of haematological parameters measured, the timepoints considered and the difference between male and female that could be significant, this process used to be time consuming (approximately two hours for analysis).<br><br>
**Figure 1**<br>
<img src="https://github.com/alanzanardi/statistical-tools/blob/main/Fig1.jpg" width="1089" height="550">
<br>
## Why the project was useful? :bulb:<br>
These scripts were created to automate the data collection process from my dataset, covering all the steps I previously performed manually — from the Excel file to the Prism GraphPad analysis.<br><br> 
Data were collected at specific timepoints (the input inserted at the beginning) and grouped based on the hematological parameter considered (in my case, all parameters).<br><br> 
Following this, the algorithm conducted the Shapiro-Wilk normality test on the Gaussian distribution to determine the appropriate test type to use (parametric vs. non-parametric); then, it calculted the p-value through ANOVA or Kruskal-Wallis test, and conducted post hoc tests (Tukey’s or Dunn’s, depending on the data distribution) for multiple comparisons.<br><br> 
At this stage of the algorithm, a report displaying p-values and post hoc test results for each parameter is printed in the terminal (see Figure 2).<br><br>
**Figure 2**<br><br> 
<img src="https://github.com/alanzanardi/statistical-tools/blob/main/Fig2.jpg" width="200" height="533">
<br>
In addition, a brief preview of the corresponding graphs for each considered parameter is also displayed to provide an overview of the data distribution in each situation (see figure 3).<br><br>
**Figure 3**<br>
<img src="https://github.com/alanzanardi/statistical-tools/blob/main/Fig3.jpeg" idth="400" height="423"><br><br> 
**Using these scripts, I was able to save several hours of unproductive work. :smiling_face_with_three_hearts:**
