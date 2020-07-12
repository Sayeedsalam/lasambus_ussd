

import requests


#uploding data
data = {"time": "20200518-233450",
        "lat": -65.00,
        "long": 20.08,
        "call_scenario": "Collapsed Building",
        "reporter": 12345}

resp = requests.post("http://149.165.157.107:8333/report_incident", json=data)

print(resp.content)

#checking status of a reported incident

id = "5f0b441040fc56525d9775ec"

resp = requests.get("http://149.165.157.107:8333/api/track?incident_id="+id)

print(resp.content)





