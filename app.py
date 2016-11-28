from flask import Flask
app = Flask(__name__)
app.mock = []
from modules.views import *

