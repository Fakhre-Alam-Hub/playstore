from sqliteDB import add_data
from google_play_scraper import app
from bs4 import BeautifulSoup
import requests

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

def fetch_package_details(package_name):
    return app(package_name, lang='en', country='us')

package_names = get_package_names()

results = [fetch_package_details(package_name) for package_name in package_names[2:]]
# print(results)
for result in results:
    package_name = result['appId']
    title = result['title']
    developer = result['developer']
    score = result['score']
    reviews = result['reviews']
    ratings = result['ratings']
    genre = result['genre']
    icon = result['icon']

    print("package_name: ",package_name)
    print("title: ",title)
    print("developer: ",developer)
    print("score: ",score)
    print("reviews: ",reviews)
    print("ratings: ",ratings)
    print("genre: ",genre)
    print("icon: ",icon)
    print("---------------------------------")


add_data(results)