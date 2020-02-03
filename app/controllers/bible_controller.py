from app import app
from flask import render_template
import requests
from app.broker.consumer import consumer

def get_bible(passage, version):
    response = requests.get(
        "http://api.biblia.com/v1/bible/content/{version}.html?passage={passage}&style=fullyFormatted"
        "&key=22dcf3b6a7aa5901f179588cdf18ae56".format(version=version, passage=passage))
    f = open('/home/tinuade/PycharmProject/project_marvis/app/templates/bible.html', "w+")
    f.write(response.text)
    f.close()



@app.route('/index')
def index():
    messages = consumer()
    for message in messages:
        action = message.key
        query = message.value
        if action == "openBible":
            get_bible(query, )





    return render_template(bible())


