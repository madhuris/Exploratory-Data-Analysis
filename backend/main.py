
import os
from flask import Flask
from flask import stream_with_context, Response, current_app,send_from_directory, request, jsonify, abort
import csv
import recommendations

import apriori

app = Flask(__name__)

@app.route("/ping")
def isOnline():
    return "Server Online."


@app.route("/")
def loadIndex():
    return send_from_directory("../","index.html")


@app.route("/getAllData")
def getAllData():
    infile =  open("data.csv")
    def generate():
        for line in infile:
             yield str(line)
    return Response(stream_with_context(generate()))

@app.route("/getOnePatient")
def getPatient():
    return "patient 1"

@app.route('/frontend/<path:path>')
def send_frontend(path):
    return send_from_directory('../frontend', path)

@app.route('/getAllAssociations')
def getAllAssociations():
	return str(rules.allRules())

@app.route('/getAssociations',methods=['POST'])
def getAssociations():
	print request.form["input"].split(",")
	if not request.form["input"].split(","):
		print "An error occurred - Expecting JSON request with list codes"
		abort(400)

	print "Incoming request"


	return str(rules.getMatchedRules(request.form["input"].split(",")))
	#return str(rules.getMatchedRules(["348831","89362005"]))

@app.route('/getDiseasesAndSymptoms', methods=['POST'])
def getDiseaseAndSymptomRecommendations():
	print request.json
	if not request.json:
		print "An error occurred - Expecting JSON request with list of patient IDs"
        print

	print "Incoming request"
	print
    # recommender = recommendations.Recommender("testdata.csv")
	recommender = recommendations.Recommender("data.csv")
	diseases = recommender.get_disease_recommendations(request.json, limit=3)
	symptoms = recommender.get_symptom_recommendations(request.json, limit=5)
	response = {"diseases" : diseases, "symptoms" : symptoms}
	print "Logging results returned for disease recommendations : "
	print
	print jsonify(response)
	#return jsonify({})
	return jsonify(response)

if __name__ == "__main__":
	rules = apriori.Apriori(0.01) #Generate rules on startup
	app.run()
