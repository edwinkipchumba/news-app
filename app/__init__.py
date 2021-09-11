from flask import Flask
from .config import DevConfig

from app import views

# Initializing application
app = Flask(__name__,instance_relative_config =True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')



