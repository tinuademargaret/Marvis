import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/tinuade/Downloads/marvis-vdohmu-0350eefd01d2.json'
DIALOGFLOW_PROJECT_ID = 'marvis-vdohmu'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

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
        command.action = response.query_result.action
        command.query = response.query_result.parameters.given_name + response.query_result.parameters.number + response.query_result.parameters.number1.join("")
        return command
    except InvalidArgument:
        raise

    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)








