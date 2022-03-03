import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib



if 1==0:
    music_data = pd.read_csv('music.csv')
    x =  music_data.drop(columns='genre')
    y = music_data['genre']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(x_train,y_train)
    predictions = model.predict(x_test)

    scores = accuracy_score(y_test, predictions)

    print(scores)

else:
    music_data = pd.read_csv('music.csv')
    x =  music_data.drop(columns='genre')
    y = music_data['genre']

    model = DecisionTreeClassifier()
    model.fit(x,y)

    joblib.dump(model, 'music-recommender.joblib')
