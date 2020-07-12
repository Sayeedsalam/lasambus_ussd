

import requests



data = {"time": "20200518-233450",
        "lat": -65.00,
        "long": 20.08,
        "call_scenario": "Collapsed Building",
        "reporter": 12345}

resp = requests.post("http://127.0.0.1:5000/report_incident", json=data)

print(resp.content)

