from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import logging
import requests
import json

API_URL = "http://xhub.ddns.net:8383/certifs"

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_demand_certif"

    def run(self, dispatcher,tracker,domain):
        res = requests.get(API_URL)
        if res.status_code == 200:
            data = res.json()
            certif = data['data'][0]
            owner = data['data'][1]
            out_message = "Here some quick info:\nThe certificate : {} was recently demanded by : {}".format(certif,owner)
            dispatcher.utter_message(out_message)
        return []
