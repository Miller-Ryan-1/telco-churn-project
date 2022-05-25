## Churn Drivers and Prediction Report

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (acquire.py, prepare.py) that make your process repeateable.
> - Construct a model to predict customer churn using classification techniques.
> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

#### Business Goals
> - Identify Key Drivers of Churn
> - Construct a ML classification model that accurately predicts whether or not a customer will churn.
> - Document your process well enough to be presented or read like a report.

#### Audience
> - Telco COO Dirk Digglerholmsteingrensonowski
> - First line supervisory team (Adam Gomez, Ryan Orsinger, et al.)
> - CodeUp Students!

#### Project Deliverables
> - A final report notebook (telco_churn_report.ipynb)
> - A predictor of customer churn driven by best ML model (predictions.csv)
> - All necessary modules to make my project reproducible

#### Data Dictionary
- Note: Includes only pre-encoded features of signifigance:

|Target|Datatype|Definition|
|:-------|:--------|:----------|
| churn | 7032 non-null: object | whether a customer says or leaves - Yes/No |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| patner       | 7032 non-null: object | whether a customer is partnered - Yes/No |
| dependents        | 7032 non-null: object | whether a customer has dependents - Yes/No |
| multiple_lines       | 7032 non-null: object | whether a customer has multiple phone lines - Yes/No/No Phone Service |
| online_security        | 7032 non-null: object | whether a customer has online security service - Yes/No/No Internet Service |
| online_backupy        | 7032 non-null: object | whether a customer has online backup service - Yes/No/No Internet Service |
| device_protection        | 7032 non-null: object | whether a customer has device protection service - Yes/No/No Internet Service |
| online_security        | 7032 non-null: object | whether a customer has online security service - Yes/No/No Internet Service |
| online_backup       | 7032 non-null: object | whether a customer has online backup service - Yes/No/No Internet Service |
| device_protection        | 7032 non-null: object | whether a customer has device protection service - Yes/No/No Internet Service |
| tech_support        | 7032 non-null: object | whether a customer has tech support service - Yes/No/No Internet Service |
| streaming_tv        | 7032 non-null: object | whether a customer has streaming tv service - Yes/No/No Internet Service |
| streaming_movies        | 7032 non-null: object | whether a customer has streaming movies service - Yes/No/No Internet Service |
| paperless_billing        | 7032 non-null: object | whether a customer uses paperless billing - Yes/No |
| contract_type        | 7032 non-null: object | type of contract a customer has - Month-to-month/One year/Two year |
| internet_service_type        | 7032 non-null: object | whether a customer has internet and if so what type - DSL/Fiber optic/None |
| payment_type        | 7032 non-null: object | how a customer pays Telco - Bank transfer (automatic)/Credit card (automatic)/Electronic check/Mailed check |
| tenure        | 7032 non-null: int64 | how long a customer has been with Telco, in months |
| monthly_charges        | 7032 non-null: float64 | how much a customer contractually pays per month, in $USD |
| total_charges        | 7032 non-null: float64 | total amount a customer has paid to Telco, in $USD (note:changed from object) |


#### Initial Hypotheses

> - **Hypothesis 1 -**
> - Higher monthly charges lead to more churn

> - **Hypothesis 2 -** 
> - Customers with dependents have higher churn

> - **Hypothesis 3 -** 
> - Types of internet has a signifigant impace on churn

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Problem: The operations team reached out to the data science division to understand what the main drivers of customer churn are, and to predict future churn based on these drivers in order for ops and marketing to intercede before we lose these customers. 
> - Actions: Performed an analysis examing drivers of churn using statistical testing, as well as creating and examing a number of models to predict churn to see what levers we have for retaining customers.  26.5% of customers churn in the month examined costing \$2.4MM.
> - Conclusions: Customers without dependents, streaming services and not subscribing to auxiliary services are driving churn.  In general, those with higher monthly costs are also more prone to churn - and quickly.  Fortunately, we now have a model that predicts churn nearly 9\% better than baseline, so we can better target those customers with churn reducing interventions.
> - Recommendations: Allow customers without dependents to join "friends and family plans" akin to having dependents, and analyze streaming service prices to evaluate their cost vs. percevied value, and perhaps give a few months fo those services at a free or reduced cost.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x]  Investigate data, formulate hypotehsis, visualize analsyis and run statistical tests when necessary (ensuring signifigance and hypotheses are created and assumptions met).  Document findings and takeaways.
- [x] Establish a baseline accuracy.
- [x] Train multiple different classification models, to include hyperparameter tuning.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with predictions on test data.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> Acquire
> - Store functions that are needed to acquire telco customer data from the Codeup data science database server; make sure the acquire.py module contains the necessary imports for anyone with database access to run the code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final functions (prep.py and splitter.py) should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare functions from the prepare.py and spliter.py modules and use them to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Feature Selection and Encoding: Are there any variables that seem to provide limited to no additional information? If so, remove them.  Also encode any non-numerical features of signifigance.
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 4 different models.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.  In this case we used Precision (Positive Predictive Value).
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk the management team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, splitter.py and matrix_result.py and telco_churn_report.ipynb files into your working directory.
- [ ] For more details on the analysis, download the telco_workbook.ipynb file as well as EDA_functions.py that the workbook uses.
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook

#### Credit to Faith Kane (https://github.com/faithkane3) for the format of this README.md file.
