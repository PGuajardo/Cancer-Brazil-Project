# Cancer-Brazil-Project
# By Paige Guajardo

## Goals defined by Cancer Data Brazil!

#### 1: Finding out what are the drivers of having no cancer?
#### 2: Create a ML(using classification algorithms) and create a model that predicts no cancer patients!
#### 3: Deliver report of step by step process, what steps where taken, why and what the outcomes were!


# Project Goals: 

*The goal of this project is to define the key drivers of no cancer patients, which patients are at likely to have no cancer, and make recommendations for changes using a classifcation ML on the cancer data set provided to create the best fit model that identifies, and gives results of no cancer patients based on the findings to help identify cancer patients, and a step by step process of the steps taken and the outcomes of the findings.*


# Project Description:

*In brazil this data contains National Cancer Intitute data from 2000 - 2019, my question posed here is trying to identify the patients that ended up having no cancer at all. Here I anazlyed based on this data key features of that and recommendation of those findings for future programs!*

# Initial Questions:

*Those of different genders have an effect on having cancer and those who do not?
*Are different educations a cause of no cancer?
*Are differnt race/colors of an indiviual in the data set have more of an effect on no cancer?
*Being in a different legal status such as single/married/ect. have an effect on having no cancer?

# Data Dictionary:

|  something | else |
_________________________
| data 1  |   variable |
##### Come back
gender | gender of customer (Male or Female)
age | the amount of years of the patient
nationality | where a patient is born
education | the level of education a patient has in brazil
status_address | state the patient was born
city_address | city the patient was born
rare_case | binary true or false if the case was rare or not
diagnostic_means | if a patient had a history of tumors or any other medical entries of family memebers
Type_of_death | if a patient had cancer or no cancer
year | the year the patient was born
Gender_Ignored | encoded value
Gender_Male | encoded value
Education_Fundamental I | encoded value
Education_Fundamental II | encoded value
Education_Graduated | encoded value
Education_Incomplete High | encoded value
Education_Without Education | encoded value
Race_Color_BRANCO | encoded value
Race_Color_IND�GENA | encoded value
Race_Color_PARDA | encoded value
Race_Color_PRETA | encoded value
Legal_Status_SEPARADO JUDICIALMENTE | encoded value
Legal_Status_SOLTEIRO | encoded value
Legal_Status_UNI�O CONSENSUAL | encoded value
Legal_Status_VI�VO | encoded value
Legal_Status_Casado | encoded value

# Steps to reproduce:


*You will need an cancer_brazil_data.csv file that contains database that containing all the data*

*Clone the repo from github(including all the files prepare.py and acquire.py) (confirm .gitignore is hiding your *.csv file)*
*Libraries needed are pandas, matplotlib, seaborn, numby, sklearn*
*After so you will be able to run Brazil_Final*

# The Plan:

- Acquire data
- Clean Data
- Split data
- Observe first questions:  Does Legal Status effect no cancer?
- Create graph and observe statistical analysis
- Observe second questions: oes the race/color effect no cancer?
- Create graph and observe statistical analysis
- Observe third questions: Does the education effect no cancer?
- Create graph and observe statistical analysis
- Observe fourth questions: Does gender effect no cancer?
- Create graph and observe statistical analysis
- Create baseline
- Test model on train set
- Create decision tree / knn model
- Observe F1-score
- Use smote to upscale data
- Create decision tree / knn / randome forest  models with smote values
- Observe F1-Score
- Test Models on validation set
- Observe F1-Score
- Test Models on test set
- Observe F1-SCore
- Key takeaway
- Recommendation
- Next Step


# Wrangle: 

 *Modules : acquire.py and prepare.py*

test acquire function
add to acquire.py module
write code to clean data in notebook
merge code into a single function & test
write code to split data in notebook
merge code into a single function & test
merge functions in a single function & test
Add all 3 functions (or more) to prepare.py file
import into notebook and test functions


# Data Split (prepare.py (def function), Brazil_Final.ipynb (run function))

This function takes in a dataframe, the name of the target variable
(for stratification purposes)
and splits the data into train, validate and test. 
Test is 20% of the original dataset, validate is .3 * .8 = 24% of the 
original dataset, and train is .7 * .80= 56% of the original dataset. 
The function returns, in this order, train, validate and test dataframes. 


# Explore

1)Is there a certain legal status that has an effect on their cancer rates?

2) The options inserted for race/color, do any of these options have more of a cause of no cancer?

3)Does education background have an effect on no cancer patients and is there a signifcance in the majority?

4) Is gender a factor of no cancer patients?

