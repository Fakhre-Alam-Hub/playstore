# playstore

REST API with python flask to fetch playstore app details

1. Clone this repo

  `git clone `

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
