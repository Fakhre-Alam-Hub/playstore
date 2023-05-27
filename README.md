# Playstore

REST API with python flask to fetch playstore app details

1. Clone this repo

  `git clone https://github.com/Fakhre-Alam-Hub/playstore.git`

2. Activate environment env

  `source env/Scripts/activate`
 
3. Install the rquired libraries from requirements.txt
    
    pip install -r requirements.txt

4. Run the application:

    a. Start RabbitMQ server.
  
    b. Start the Celery worker: Open a new terminal, navigate to the project directory, and run the following command:
  
    `celery -A tasks worker --loglevel=info `
    
    c. Start the Flask application: In another terminal, navigate to the project directory, and run the following command:
  
    `python app.py
    OR
    flask run`
   
5. The API will be accessible at http://localhost:5000/api/apps.

### Result

Here is the sored data in sqlite DB database


![playstore db](https://github.com/Fakhre-Alam-Hub/playstore/assets/60462475/12fc446a-6791-4c8b-b229-a2886c33d432)
