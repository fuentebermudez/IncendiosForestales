
from joblib import dump, load

from sklearn.metrics import mean_squared_error

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import explained_variance_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier
import Transformer as t

import Extract as e

def train_and_evaluate(clf, X_train, y_train):

    clf.fit(X_train, y_train)
    y_pred=clf.predict(X_train)
    print("Coefficient of determination on training set:", clf.score(X_train, y_train), "RMSE:", mean_squared_error(y_train, y_pred),
          explained_variance_score(y_train,y_pred), "R:", r2_score(y_train,y_pred))

    return clf


train_path="..\..\data\incendios_merge.csv"

incendios=e.load_data(train_path)

PARAMETROS=['cota','lat','lng', 't_max', 't_min','racha', 'vel_media', 'NDVI','ETO','PENDIENTE','superficie']
incendios=incendios[PARAMETROS].dropna()

X=incendios.drop('superficie',axis=1)
#X=t.add_clase(incendios)
#scaler = StandardScaler()

#X=scaler.fit_transform(X)
X=incendios.drop('superficie',axis=1)
y=incendios['superficie']

X_train, X_test, Y_train,Y_test=train_test_split(X,y,test_size=0.33,random_state=1)

param_grid_KNN={
    'n_neighbors': [4,6,8,10,1000],
    'weights':['distance','uniform']
}

param_grid_SVR={
    'gamma': ['scale'],
    'C':[1000],
    'epsilon':[0.2]
}

param_grid = {
    'bootstrap': [True],
    'max_depth': [80,90,100],
    'max_features': [2, 3,6],
    'min_samples_leaf': [2,3],
    'min_samples_split': [2,4, 10],
    'n_estimators': [100]
}# Create a based model
clf = RandomForestRegressor()# Instantiate the grid search model
#clf=SVR()
#clf=KNeighborsRegressor()
clf = GridSearchCV(estimator = clf, scoring='neg_mean_squared_error',param_grid = param_grid,
                          cv = 3, n_jobs = -1, verbose = 2)

clf=train_and_evaluate(clf,X_train, Y_train)
#clf=train_and_evaluate(clf,X, y)

dump(clf, '../../output/models/clf.joblib')



