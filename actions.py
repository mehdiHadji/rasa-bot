from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import logging
import requests
import json
from slackclient import SlackClient

SLACK_BOT_TOKEN = "xoxb-774540282707-788506962980-1iINzBjbDwHzDA7y439nIDol"
API_URL = "http://xhub.ddns.net:8383/certifs"
slack_client = SlackClient(SLACK_BOT_TOKEN)



def slackitems(tracker):
    username = tracker.sender_id
    print("username", username)
    userinfo = slack_client.api_call("users.info", user=username)
    email = userinfo['user']['profile']['email']
    real_name = userinfo['user']['profile']['real_name']
    return email, real_name




class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_demand_certif"

    def run(self, dispatcher,tracker,domain):
        res = requests.get(API_URL)
        if res.status_code == 200:
            data = res.json()
            certif = data['data'][0]
            #owner = data['data'][1]
            email = slackitems(tracker)[0]
            username = slackitems(tracker)[1]
            out_message = "your request is under review following the parameters :\n*certificate : {} \n*owner : {} \n*email : {}".format(certif,username,email)
            dispatcher.utter_message(out_message)
        return []
