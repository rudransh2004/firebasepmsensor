from firebase_admin import db
import firebase_admin
from flask import Flask,jsonify,request,make_response,url_for,redirect
import  json
app = Flask(__name__)

cred_obj = firebase_admin.credentials.Certificate('nsr-airview-firebase-adminsdk-o22ic-b0468123ae.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://nsr-airview-default-rtdb.firebaseio.com/"
	})




ref = db.reference("/")
ref.set({
	"Pmsensor":
	{
		"Data": -1
	}
})

ref = db.reference("/Pmsensor/Data")
import json


@app.route('/', methods=['GET','POST'])

def create_row_in_gs():
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        seq  =  request.json["seq"]
        PM10 = request.json["PM10"]
        PM25 = request.json["PM25"]
        PM100 = request.json["PM100"]
        
        create_row_data = {"2_PM10" : PM10 ,"3_PM25":PM25,"4_PM100":PM100,"1_seq":seq}
        data=json.dumps(create_row_data)
        data = json.loads(data)
        ref.push().set(data)    
        return data


if  __name__ == '__main__':
    app.run(host='localhost',debug=False, use_reloader=True)