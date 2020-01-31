from app import app
from flask import render_template
import requests
from app.broker.consumer import consume


def get_passage(consumer=consume()):
    for msg in consumer:
        pass


def get_bible(passage, version):
    response = requests.get(
        "http://api.biblia.com/v1/bible/content/{version}.html?passage={passage}&style=fullyFormatted"
        "&key=22dcf3b6a7aa5901f179588cdf18ae56".format(version=version, passage=passage))
    f = open('/home/tinuade/PycharmProject/project_marvis/app/templates/bible.html', "w+")
    f.write(response.text)
    f.close()


# key_word = transcribe_streaming(stream_file=os.path.join(
#         os.path.dirname(__file__),
#         'resources', 'cinderella.wav')
#     )


# if key_word == 'Open Bible':
#     get_bible(passage='luke1.35', version='KJV')
#     return 'bible.html'


@app.route('/index')
def index():
    return render_template(bible())


if __name__ == '__main__':
    app.run()
