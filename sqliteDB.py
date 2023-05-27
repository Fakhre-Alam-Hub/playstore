import sqlite3

def add_data(results):
    # Create a connection to the SQLite database
    conn = sqlite3.connect('playstore.db')
    cursor = conn.cursor()

    for result in results:
        package_name = result['appId']
        title = result['title']
        developer = result['developer']
        score = result['score']
        reviews = result['reviews']
        ratings = result['ratings']
        genre = result['genre']
        icon = result['icon']

        cursor.execute('''
            INSERT INTO app_details (package_name, title, developer, score, reviews, ratings, genre, icon )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (package_name, title, developer, score, reviews, ratings, genre, icon ))

    print("Results added to database successfully !")
    conn.commit()
    conn.close()