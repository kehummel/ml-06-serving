# Project Documentation

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get the example projects running on your machine.


## Phase 4. Technical Modification

I changed the target from 'species' to 'sex' of the penguins.
I chose that change because phase 4 is supposed to be a small technical change to make sure we can make a change and run the scripts correctly.
This was a simple change that would definitely give me a different output or prediction, making it easy to see if my modification had worked or not.

I tested the technical change with two different keys and they both returned a gender instead of a species.

This was an easy change and it only required me to change a few lines in the code.
It was simple and allowed me to better understand the code and what was happening in the project.

![Phase 4 Test](./docs/images/06_P4_output.png)

## Phase 5. Custom Project

For my custom project I created a server in which you could input a person's glucose, BMI, and age and it would predict whether or not they had diabetes.

### Basis and Data

In the last module I used a dataset on people with diabetes. I decided to use that dataset again to create a server that predicted whether or not each person had diabetes.

This database came from kaggle. It originally had 8 features and over 700 data instances.
I created a column "diabetic" to state whether or not each person was diabetic.
I did this because when I was originally getting the prediction it was a 0 or 1 from the "outcome" feature, which I thought would be harder for a user to understand.
There were no rows with missing values, so I did not have to remove any rows.

A limitation of this data is that there are rows with zeros in the feature columns.
These rows should have been removed because they are not valid values for a glucose level, BMI value, or age.
A next step for this project would be to remove outliers from the dataset before the model is trained so that it is not skewing the data.

After I did the basic transformations, I then used the processes from module 5 to determine which model to use to train the data and to determine which features were most important.
Between the single tree, random forest, and voting models, the random forest had the highest accuracy so that was the model I used.
I then calculated the most important features to use in the server which were glucose, BMI, and age.
I was initially going to include the diabetes pedigree function as an important feature since it was similar to age, but I decided to not use it because a user would be less likely to know their diabetes pedigree function which would make them less likely to use the server.

[ml_06_important_features.ipynb](project06/ml_06_important_features.ipynb)

![Test Accuracy Per Model](./docs/images/06_P4_test_accuracy.png)

![Most Important Features](./docs/images/06_P4_important_features.png)

### Example Model and Serving Approach

The model predicts whether or not a person has diabetes based on the inputs of glucose level, BMI, and age.

The data is loaded and split between training and testing sets with stratification for diabetic or not.

The data is trained using a random forest classifier and saved to model2.joblib.

The API receives the request of the three features in the terminal and outputs a json prediction.

The model is deployed locally.

### Custom Application

I changed the dataset from the example, which caused me to change my target and features.
I looked into changing the model, but found that the random forest had the highest accuracy of the three I compared so I kept it the same.
I calculated which features were the most important instead of just guessing which ones were the best.

I also added in the probability of the outcomes so that users could understand the confidence of the prediction given.

Additionally, I created warnings for someone with a very low glucose level as they would be at risk for hypoglycimeia.
I also created warnings for extremely low and high BMIs.
All of these warnings were made because they signal a possible medical problem that does not relate to the prediction of the server.

I made these changes because I wanted the user to get the most usable information from the server.
Having a prediction that is 60% as opposed to 80% is a different level of confidence.
Being warned about possible medical problems is a possible preventative heads up for a user.

I verified it worked by creating multiple requests and testing them on the system.

[practice_requests.md](project06/practice_requests.md)

Results from practice requests:

![Testing Results 1](./docs/images/06_P5_testing1.png)

![Testing Results 2](./docs/images/06_P5_testing2.png)

### Summary

When I ran my requests I got reasonable responses, with the probability and warnings when appropriate.

I learned how to create and run a server.
I learned how to add on additional features to make the user more informed.

My server runs correctly and is able to provide the user with more information than a simple "diabetic" or "not diabetic".
I believe it is a thorough and solid server.

However, I originally intended to run requests through Hugging Face as a web based ML model.
I ran out of time and knew I was not going to be able to set that up as well as modifying the server as I knew I wanted to.
I decided it was better to get the experience running and modifying the server to look professional and meet user needs instead of trying a new system.

I can see applying this to my current work where I am looking at students' test scores and what teachers need to work on to improve state test scores.
This could also be used in determining risk management, and whether or not loans are approved or denied for potential borrowers.
