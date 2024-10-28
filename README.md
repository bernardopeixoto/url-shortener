# URL Shortener API

A Django URL shortener API that creates short URLs with a specific signature format.

## Architecture

1. *Layered Architecture*:
   - Repository Layer: Handles data persistence and retrieval
   - Service Layer: Contains business logic
   - DTO Layer: Uses serializers for data transfer and verification (not really a DTO but serializers follow DTO verification logic)
   - Controller Layer: mapped targets for the specified routes / http requests (views)

Above mentioned onion based architecture was chosen due to the separation of responsibilities, modularization of code and distancing controllers/views and business logic/database interactions

2. *URL Shortening Logic*:
   - Format: `{base62_encoded_id}{signature}`
   - The signature is based on the original URL
   - Uses base62 encoding for shorter URLs

This is important to ensure uniqueness for the urls. Shortened links aren't following a sequential and predictable logic, disallowing people to easily guess links

Also, this decision was taken to save pointless and possible expensive trips to the database. If a shortened requested link doesn't follow our signature, return an error

3. *Database*:
   - 

## Endpoints

1. POST /api/shorten
   - Request: {"url": "https://example.com/very/very/very/very/very/very/very/very/very/very/long/url"}
   - Response: {"short_url": "http://localhost:8000/abc123"}

2. GET /{code}
   - Redirects to the original URL
