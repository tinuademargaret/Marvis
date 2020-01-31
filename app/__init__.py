from flask import Flask
# from src.config.constants import Config
# from src.config.database import Configdb
# from src.config.cors import *
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_restful import Api
# from flask_marshmallow import Marshmallow
# from flask_msearch import Search
# import base64, re, logging
# from elasticsearch import Elasticsearch


import os

app = Flask(__name__)
# app.config.from_object(Config)
# app.config.from_object(Configdb)
# app.after_request(add_cors_headers)
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
# migrate = Migrate(app, db)
# api = Api(app)
# app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) if app.config['ELASTICSEARCH_URL'] else None
# app.app_context().push()
# Log transport details (optional):
# logging.basicConfig(level=logging.INFO)
# Parse the auth and host from env:
# bonsai = app.config['ELASTICSEARCH_URL']
 # 'https://q9x9bmxtfw:m9kqgdsfy1@box-380265849.us-east-1.bonsaisearch.net'
 #'https://bytx8k0hih:i17jwsgfgi@inventedu-testing-3659711170.us-east-1.bonsaisearch.net'
# # auth = re.search("https\:\/\/(.*)\@", bonsai).group(1).split(':')
# host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

# # Connect to cluster over SSL using auth for best security:
# # es_header = [{
# #  'host': host,
# #  'port': 443,
# #  'use_ssl': True,
# #  'http_auth': (auth[0], auth[1])
# }]

# # Instantiate the new Elasticsearch connection:
# app.elasticsearch = Elasticsearch(es_header)
# search = Search()
# search.init_app(app)
# MSEARCH_INDEX_NAME = 'msearch'
# simple,whoosh,elaticsearch, default is simple
# MSEARCH_BACKEND = 'whoosh'
# auto create or update index
# MSEARCH_ENABLE = True
# APP_URL = "https://inventedu.herokuapp.com/"
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# from src.app.services import database_service
