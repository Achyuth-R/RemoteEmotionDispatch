import os
from flask import Flask

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
LightRecordFile = open("LightRecordFile.txt",'w')
LightRecordFile.write('0')
LightRecordFile.close()

from server.module.routes import *