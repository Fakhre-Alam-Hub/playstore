from flask import Flask, jsonify
from celery import Celery
from google_play_scraper import app
from bs4 import BeautifulSoup
import requests
from tasks import fetch_package_details
from sqliteDB import add_data
from create_sqliteDB import create_sqliteDB_table

# app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'amqp:/guest:guest@127.0.0.1:5672/'
# app.config['CELERY_RESULT_BACKEND'] = 'rpc://'
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

app = Flask(__name__)
celery = Celery(app.name, broker="amqp://guest:guest@127.0.0.1:5672",backend="'rpc://")

# uncomment this if you want to create table
# create table if not exist
# if True:
#     create_sqliteDB_table()


# Function to scrape the data from the URL and filter out package names and return list of package names
def get_package_names():
    url = 'https://play.google.com/store/games?hl=en&gl=US'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    package_names = []
    app_containers = soup.find_all('a', class_='Si6A0c Gy4nib')
    for app_container in app_containers:
        package_name = app_container['href'].split('=')[-1]
        package_names.append(package_name)
    return package_names


@app.route('/api/apps', methods=['GET'])
def fetch_app_details():
    # get the package names
    package_names = get_package_names()

    # Queue the package names for fetching details
    tasks = [fetch_package_details.delay(package_name) for package_name in package_names]

    # Retrieve the results from the task queue
    results = [task.get() for task in tasks]

    # Store the results in the SQLite database
    add_data(results)

    # Return the JSON response
    response = {
        "message": "Added the data to the database successfully...",
        "package_names":package_names
    }    
    return jsonify(results)

@app.route('/', methods=['GET'])
def home():
    response = {
        "info": "Welcome to Home Page!",
        "message": "Go to --> http://127.0.0.1:5000/api/apps"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)