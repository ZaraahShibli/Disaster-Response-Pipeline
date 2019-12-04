
# Disaster Response Pipeline

------
1. [Project Overview](#ProjectOverview)
2. [Installation](#installation)
3. [Project Components](#ProjectComponents)
4. [Results](#results)
5. [Files](#files)
6. [Acknowledgements](#acknowledgements)

## 1. Project Overview <a name="ProjectOverview"></a> 
The aim of this project is to build a model for classifies disaster messages. The dataset collected by [Figure Eight](https://www.figure-eight.com/). The [disaster response dataset](https://www.figure-eight.com/dataset/combined-disaster-response-data/) contains 30,000 messages, It has been encoded with 36 different categories related to disaster response and has been stripped of messages with sensitive information in their entirety.   

## 2. Installation <a name="installation"></a>

- Python versions 3.*.
- Python Libraries:
    - Pandas.
    - Scikit-learn.
    - numpy.
    - nltk.
    - sqlalchemy.
  
## 3. Project Components <a name="ProjectComponents"></a> 
There are three main folder in this project :
1. **ETL Pipeline:** 
data/process_data.py, contains data cleaning pipeline that:
    - Loads the messages and categories datasets
    - Merges the two datasets
    - Cleans the data
    - Stores it in a SQLite database
        
2. **ML Pipeline:** 
models/train_classifier.py contains machine learning pipeline that:
    - Loads data from the SQLite database
    - Splits the dataset into training and test sets
    - Builds a text processing and machine learning pipeline
    - Trains and tunes a model using GridSearchCV
    - Outputs results on the test set
    - Exports the final model as a pickle file

3. **Flask Web App:** 
contains web app to classifier messages in real time using trained model.

## 4. Results <a name="results"></a> 
Here are a few screenshots of the web app.

![figure1](https://user-images.githubusercontent.com/42017072/70146091-8f286380-16b2-11ea-9ac2-d00762dcb374.PNG)


![figure2](https://user-images.githubusercontent.com/42017072/70146109-994a6200-16b2-11ea-8ff6-86e96fc20f6a.PNG)


![figure3](https://user-images.githubusercontent.com/42017072/70146274-f0e8cd80-16b2-11ea-9ce6-d64cbd2688d7.PNG)

## 5. Files <a name="files"></a>
<pre>
- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- DisasterResponse.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md
</pre>

## 6. Acknowledgements <a name="acknowledgements"></a> 
I wish to thank [Figure Eight](https://www.figure-eight.com/) for dataset. Also, thanks for [Udacity](https://www.udacity.com/) for advice.

