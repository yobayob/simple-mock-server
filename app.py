from flask import Flask
app = Flask(__name__)
app.mock = []
from simple_mock_server.views import *

