from celery import Celery
from google_play_scraper import app
from flask import Flask, jsonify

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

# celery function to get details of package 
@app.task
def fetch_package_details(package_name):
    return app(package_name, lang='en', country='us')
