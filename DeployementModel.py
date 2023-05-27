from distutils.log import debug

from flask import Flask, request,jsonify,render_template,redirect,url_for

import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import pickle

app=Flask(__name__)

#Création du dictionnaire
models=pickle.load(open('ModelDiabRF.pkl','rb'))


@app.route('/')
def home():
	return render_template('index.html')
@app.route('/predict', methods=['POST'])

def predict():
	models=pickle.load(open('ModelDiabRF.pkl','rb'))

	#Conversion de float enint
	int_future=[float(i) for i in request.form.values()] 
	dernier_future=[np.array(int_future)]

	dernier_future=np.array([dernier_future]).reshape(1,8)
	predire=models.predict(dernier_future)
	if(models.predict(dernier_future)==1):
		predire="Positif"
	else:
		predire="Negatif"

	return render_template('index.html', prediction_text_="Votre type est: {}".format(predire))
if __name__=='__main__':
	app.run(debug=True)