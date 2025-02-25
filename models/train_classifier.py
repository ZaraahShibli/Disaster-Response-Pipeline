import sys
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

import pandas as pd
from sklearn.externals import joblib
from sqlalchemy import create_engine

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report

def load_data(database_filepath):
    '''
    Description: Load data from database
    
    Arguments:
        database_filepath: database path
    Return:
        X: feature
        Y: labels
        category_names: category names 
        
    '''
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('DisasterResponseTable',engine)
    X = df['message']
    Y = df.drop(columns=['id','message','original','genre'])
    category_names = Y.columns
    
    return X,Y,category_names
    

def tokenize(text):
    '''
    Description: convert text to tokens
    
    Arguments:
        text: string messages
    Return:
        clean_tokens: clean tokens 
        
    '''
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    '''
    Description: build ML pipeline  
    
    Arguments:
        None
    Return:
        cv: natural language processing pipeline
        
    '''
    pipeline = Pipeline([
                    ('vect', CountVectorizer(tokenizer=tokenize)),
                    ('tfidf', TfidfTransformer()),
                    ('clf', MultiOutputClassifier(RandomForestClassifier()))
                ])
    
    parameters = {
        'tfidf__use_idf': (True, False),
        'clf__estimator__min_samples_split': [2, 4]
    }
    
    cv = GridSearchCV(pipeline,parameters)

    
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    '''
    Description: Load data from database
    
    Arguments:
        model: trained model
        X_test: test feature
        Y_test: test labels
        category_names: category names 
    Return:
        None 
        
    ''' 
    y_pred = model.predict(X_test)
    y_pred = pd.DataFrame(y_pred,columns= category_names)
    for col in category_names:
        print('Column Name: ',col)
        print(classification_report(Y_test[col], y_pred[col]))
        print('--------------------------------------------------')


def save_model(model, model_filepath):
    '''
    Description: Save model
    
    Arguments:
        model: trained model 
        model_filepath: model file path
    Return:
        None
        
    '''
    joblib.dump(model, model_filepath)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()