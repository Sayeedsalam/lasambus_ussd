from datetime import datetime
from pprint import pprint

from flask import Flask, request, Response
from pymongo import MongoClient
import json
app = Flask(__name__)
import requests

# from pyfcm import FCMNotification
#
# push_service = FCMNotification(api_key="AAAAjvhjgEA:APA91bHtd9vHsDrU8vx0_xVmrr9TyAfk-CFDO9L24Q0J0hK6lzyp6HgKeeVA5kjKRy_Bt15624F5uyuKP7YumFtHZdyOTQN5s-epLogKpzRVImWGnSZ_wgvbG2hn1rXPKwxXJz1Aawce")


def _get_mongo():

    return MongoClient(port=3154)


@app.route('/api/gen_id')
def get_id():
    db = _get_mongo().covid_info
    obj_id = db.users.insert({"field":"dummy"})
    return Response(json.dumps({"status": "success", "payload": {"id": str(obj_id)}}), mimetype="application/json")



@app.route('/api/track')
def track_incident():
    incident_id = request.args.get("incident_id")

    # print (data)
    # db = _get_mongo().covid_info
    # for loc in data["locations"]:
    #     loc["id"] = data["id"]
    # db.loc_info.insert_many(data["locations"])

    return Response(json.dumps({"status": "error", "data": "API not implemented yet"}), mimetype="application/json")


@app.route('/report_incident', methods=['POST'])
def upload_data():
    data = request.get_json()


    time = data["time"]
    lat = data["lat"]
    long = data["long"]
    scenario = data["call_scenario"]
    reporter = data["reporter"]

    record_type = "ussd_reports"



    db = _get_mongo().lasambus


    #db[record_type].remove({"year": year, "name": name, "type": type})

    obj = db[record_type].insert(data)

    print("done")
    return Response('{"status": "success", "incident_id":"'+str(obj)+'"}', mimetype="application/json", )





def _validate(data):
    return True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8333, threaded=True)
