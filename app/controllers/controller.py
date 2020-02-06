
from app import app, socketio, emit
import requests
from app.broker.consumer import consumer
message = consumer()


class Controller:

    def get_bible(self, passage, version):
        response = requests.get(
            "http://api.biblia.com/v1/bible/content/{version}.html?passage={passage}&style=fullyFormatted"
            "&key=22dcf3b6a7aa5901f179588cdf18ae56".format(version=version, passage=passage))
        return response
        # f = open('/home/tinuade/PycharmProject/project_marvis/app/templates/bible.html', "w+")
        # f.write(response.text)
        # f.close()

    def search(self, query):
        pass

    def run(self):
        # for message in messages:
        if message.action == "openBible":
            data = self.get_bible(message.query, "kjv")
            socketio.emit("result", {"data": data}, namespace="/marvis")
        elif message.action == "search":
            data = self.search(message.query)
            socketio.emit("result", {"data": data}, namespace="/marvis")








