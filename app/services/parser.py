import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/tinuade/Downloads/marvis-vdohmu-0350eefd01d2.json'
DIALOGFLOW_PROJECT_ID = 'marvis-vdohmu'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'
from google.protobuf.json_format import MessageToJson
import json

"""
keywords = 'Marvis open bible 
           Marvis Search for
           Marvis next/previous/nth slide'
"""


def parser(transcript):
    command = {}
    text_to_be_analyzed = transcript
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        response = MessageToJson(response)
        response = json.loads(response)
        print(response)
        command['action'] = response['queryResult']['action']
        number = str(response['queryResult']['parameters']['number'])
        number = number.split('.')[0]
        if response['queryResult']['parameters']['number1']:
            verse = response['queryResult']['parameters']['number1']
            verse = '-'.join([str(int(elem)) for elem in verse])
            command['query'] = response['queryResult']['parameters']['given-name'] + str(number) +":"+ verse
            return  command
        command['query'] = response['queryResult']['parameters']['given-name'] +str(number)
                           # + response['queryResult']['parameters']['number1'].join("")
        return command
    except InvalidArgument:
        raise
    except KeyError:
        pass









