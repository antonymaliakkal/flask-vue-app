
# Grocery Store Website

This project is an online platform for purchasing groceries and essential items, designed with a modern and efficient tech stack. The application features a Vue.js-based user interface, a Flask backend with SQLite for persistent storage, and Celery integrated with Redis for handling asynchronous tasks.The project has three login the user , manager & admin.User can search & purchase items , the manager & admin can create , edit and delete product categories and products. The manager can also view monthly, weekly and daily purchse report.Redis is used to cache the frequently searched items by user for faster access.Celery is used to send mails of purschase , remainders etc..
 



## Features

- **User-Friendly Interface**: The front end is built with Vue.js, providing a smooth and responsive user experience.

- **Secure and Robust Backend**: Powered by Flask, the backend ensures secure data handling and efficient processing.

- **Persistent Storage**: SQLite is used as the database for storing user information, order details, and product inventory.

- **Asynchronous Task Processing**: Celery is utilized for handling background tasks such as sending emails, notifications, and reminders.

- **In-Memory Caching**: Redis is employed to enhance performance with in-memory caching, reducing load times and improving the overall user experience.



## Installation

#### 1. Clone the Repository:
```
git clone https://github.com/antonymaliakkal/grocery-store-website.git
cd grocery-store-website
```
#### 2. Backend Setup:
- Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate
```

- Install the required Python packages:
```
pip install -r requirements.txt
```

#### 3. Frontend Setup:

- Navigate to the frontend directory and install dependencies:
```
cd frontend
npm install
```
#### 4. Running the Application:

- Start the Flask backend:
```
flask run
```
- Start the Vue.js frontend:
```
npm run serve
```
#### 5. Starting Celery:
- In a separate terminal navigate to backend, start the Celery worker:
```
celery -A app.celery worker --loglevel=info
```
- In a separate terminal navigate to backend, start the Celery beat(to schedule tasks):
```
celery -A app_instance.celery_app beat --loglevel INFO
```

#### 6. Starting Redis:

- Ensure Redis server is running. If not, start Redis using:
```
redis-server
```

