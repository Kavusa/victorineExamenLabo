import flask
import pandas as pd
from sklearn import metrics
import pickle as pkl


with open(f'ModelDiabRF.pkl','rb') as f:
	model=load(f)

app=flask.Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST'])
def main():
	if flask.request.method=='GET':
		return (flask.render_template('index.html'))

	if flask.request.method=='POST':
		Pregnacies=flask.request.form['Pregnacies']
		glucose=flask.request.form['glucose']
		BloodPressure=flask.request.form['glucose']

		input_variables=pd.DataFrame([1,0]), columns=([1,0]),dtype='float',index=['input']

		predictions=model.predict(input_variables)[0]
		print(predictions)

		return flas.render_template('index.html', original_input=)

	if __name__=='__main__':
		app.run(debug=True)

