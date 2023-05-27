from distutils.log import debug

from flask import Flask, request,jsonify,render_template,redirect,url_for

import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import pickle


app=Flask(__name__)
models=pickle.load(open('ModelDiabRF.pkl','rb'))
dict_class_lesion={
	1:"Positif",
	0:"Negatif"
	
}

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/predict', methods=['POST'])

def predict():
	models=pickle.load(open('ModelDiabRF.pkl','rb'))

	#Conversion de float enint
	int_futures=[float(i) for i in request.form.values()] 
	derniers_futures=[np.array(int_futures)]

	derniers_futures=np.array([derniers_futures]).reshape(1,8)
	predire=models.predict(derniers_futures)

	#Pour supprimer le target
	pre_class=predire.argmax(axis=-1)
	# Pour prendre en charge le dictionnaire
	prediction=dict_class_lesion[predire[0]]
	result=str(prediction)

	return render_template('index.html', prediction_text_="Votre type est: {}".format(result))
if __name__=='__main__':
	app.run(debug=True)