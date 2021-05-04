from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')

from flaskapp import routes