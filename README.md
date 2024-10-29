# URL Shortener API

A Django URL shortener API that creates short URLs with a specific signature format.

## Architecture / Implementation Decisions

1. *Layered Architecture*:
   - Repository Layer: Handles data persistence and retrieval
   - Service Layer: Contains business logic
   - DTO Layer: Uses serializers for data transfer and verification (not really a DTO but serializers follow DTO verification logic)
   - Controller Layer: mapped targets for the specified routes / http requests (views)

Above mentioned onion based architecture was chosen due to the separation of responsibilities, modularization of code and distancing controllers/views from business logic/database interactions

2. *URL Shortening Logic*:
   - Format: `{base62_encoded_id}{signature}`
   - The signature is based on the original URL
   - Uses base62 encoding for shorter URLs

This is important to ensure uniqueness for the urls. Shortened links aren't following a sequential and predictable logic, disallowing people to easily guess links

Also, this decision was taken to save pointless and possible expensive trips to the database. If a shortened requested link doesn't follow our signature, return an error

3. *Database*:
   - Next step would be implementing connection to a PG DB, using docker images for quick and simple setup

## Endpoints

1. POST /shorten
   - Request: 
   {
    "url": "https://example.com/very/very/very/very/very/very/very/very/very/very/long/url"
   }
   - Response: {"short_url": "http://localhost:8000/aBc1234"}

2. GET /{code}
   - Redirects to the original URL


## How to run locally:
1. Create a virtual environment:
    -  python -m venv venv
    -  venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run migrations:
   python manage.py migrate

4. Start the development server:
   python manage.py runserver

   server will be running on http://127.0.0.1:8000/

## To Do:

![image](https://github.com/user-attachments/assets/6e37e21d-df05-4e66-9585-9a79a95c981b)
- this model has a visits property for eventual future database cleanup. We can use this field to assess which urls are not accessed or have low hits and clean them up from our database. Either by true deletion of soft deletion, depending on future requirements based on users' behaviours.
- apply testing to our app
- create rest of CRUD endpoints
