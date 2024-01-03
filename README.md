1. To install frontend part,
   cd to frontend;
   then npm install;
   npm run dev   
	 	
2. To install the backend part,
    cd to backend 
    python3 -m venv .venv (to create virtual environment)
    . .venv/bin/activate 
    pip install -r requirements.txt (to install required packages) 
    flask run  (run the app)

3. redis-cli to start the redis server on default port

4. To run the celery workers
  cd to backend
  celery -A app_instance.celery_app worker --loglevel INFO

5. To run celery beat to run scheduled tasks
  cd to backend
  celery -A app_instance.celery_app beat --loglevel INFO
