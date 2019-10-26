from monkeylearn import MonkeyLearn
import pandas as pd
ml =  MonkeyLearn('5f2cefcb8b5e4114101683b8291faf235c5fffad')
model_id = 'cl_pi3C7JiL'

def get_data_twitter():
    col_names = ['Time','Tweet']
    jetblue = pd.read_csv('jetblue.csv', names = col_names)
    return jetblue

def mlsetiment_twitter():
    jetblue = get_data_twitter()
    tweets = list(jetblue['Tweet'])
    result = ml.classifiers.classify(model_id, tweets)
    print(result.body)

def get_data_aq():
    col_names = ['Review']
    review = pd.read_csv('review.csv', names=col_names, encoding='utf-8')
    return review

def mlsetiment_aq():
    reviews = get_data_aq()
    reviews = list(reviews['Review'])[0:299]
    result = ml.classifiers.classify(model_id, reviews)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(result.body)

# mlsetiment_twitter()
mlsetiment_aq()