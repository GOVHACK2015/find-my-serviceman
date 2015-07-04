# Import Flask
from flask import Flask

# Define application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


