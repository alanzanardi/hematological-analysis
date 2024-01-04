# statistical-tools
A collection of statistical tools written in Python and SQL, designed for analyzing data related to physiological parameters derived from experimental measurements. These tools were created to expedite the statistical analysis process, extracting and sorting data from tabular-format datasets, in my specific case studies.<br>
<br>
Hoping they can be useful to you as example from which collecting inspiration for your specific cases.<br>
<br>
**\*\*\* DISCLAIMER \*\*\*** these scripts were written to help me in my laboratory data analysis work. The example I used to explain how they work show totally random values, in any case each data contained here should be trated as confidential. Thank you for the support.<br>
<br>
## How it works :wrench: <br>
Both scripts are designated to collect specific data from my dataset (namely, haematological_dataset.db). The difference is that data are stored in a local database located in the project folder (not present in the repository) in haematological_analysis_local_folder case; while in haematological_analysis_host case, data are stored on a database located on an host (in my case, the localhost).<br><br>
## What was my problem? :mag:<br>
The type of dataset I needed to analyze was relatively simple.<br>
In my case, the dataset was made from haematological analysis performed on blood sample from different subjects (both male and female) at different timepoints (6, 12, 18 and 24 months). These subjects were grouped on the basis of genotype (knock-out, KO; heterozygous, HE; and wild-type, WT).<br> 
**The haematological parameters measured are:** red blood cell count, rcb; haemoglobin level, hgb; hematocrit, hct; mean corpuscular volume, mcv; mean corpuscular haemoglobin, mch; mean corpuscular haemoglobin concentration, mchc; red cell distribution width - standard deviation, rdw_sd; reticulocyte number, ret_num; reticulocyte percentage, ret_perc; platelet count, plt; white blood cell count, wbc; reticulocyte haemoglobin content, ret_he.<br>
An example of such dataset is depicted in figure 1, left panel.<br>
My goal was to group data at different timepoints on the basis of the parameter considered (see figure 1, right panels), in order to perform variance analysis and post hoc test on the three genotypes, using Prism GraphPad.<br>
Given the amount of haematological parameters measured, the timepoints considered and the difference between male and female that could be significant, this process used to be time consuming (approximately two hours for analysis).<br>
