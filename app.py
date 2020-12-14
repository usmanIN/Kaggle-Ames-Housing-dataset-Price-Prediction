from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)


file = 'house_model.pkl'
if os.path.exists(file):
    model = pickle.load(open(file,'rb'))
else:
    print("File Don't Exists")    


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/predict",methods=["POST"])	
def predict():

	if request.method == "POST":

		LotArea = float(request.form["LotSize"])
		YearBuilt = int(request.form["YearBuilt"])
		FlrSF1st = int(request.form["FlSF1st"])
		FlrSF2nd = int(request.form["FlrSF2nd"])
		FullBath = int(request.form["FullBath"])
		BedroomAbvGr = int(request.form["BedroomAbvGr"])
		TotRmsAbvGrd = int(request.form["TotRmsAbvGrd"])

		predict = model.predict([[LotArea, YearBuilt, FlrSF1st, FlrSF2nd, FullBath,BedroomAbvGr, TotRmsAbvGrd]])

		result = round(predict[0],2)

		if result < 0:
			return render_template('index.html',result="Sorry you cannot sell this car")
		else:
			return render_template("index.html",result=result)

	else:
			return render_template("index.html")					
if __name__ == '__main__':
    app.run()