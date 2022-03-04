import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn import tree



if 1 == 0:
    music_data = pd.read_csv('music.csv')
    x =  music_data.drop(columns=['genre'])
    y = music_data['genre']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(x_train,y_train)
    predictions = model.predict(x_test)

    scores = accuracy_score(y_test, predictions)

    print(scores)

elif 'save it'==0:
    music_data = pd.read_csv('music.csv')
    x =  music_data.drop(columns='genre')
    y = music_data['genre']

    model = DecisionTreeClassifier()
    model.fit(x,y)

    joblib.dump(model, 'music-recommender.joblib')
elif 'loadmodel'==0:
    model = joblib.load( 'music-recommender.joblib')
    predictions = model.predict([[21,1]])
    print (predictions)
else:
    music_data = pd.read_csv('music.csv')
    model = joblib.load( 'music-recommender.joblib')
    tree.export_graphviz(model, out_file='mosic-reccomender.dot',
    feature_names=['age','gender'],
    class_names=sorted(music_data['genre'].unique()),
    label='all',
    rounded=True,
    filled=True)
