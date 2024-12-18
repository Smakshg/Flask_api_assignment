This project is a Flask-based API for managing books and members in a library. It supports basic CRUD operations and includes optional features like search, pagination, and token-based authentication.

How to Run the Project :-

To run this project, follow these steps:
Clone the Repository
Clone the GitHub repository to your local machine.

Install Dependencies
Make sure Python is installed, then install Flask:

 bash
 Copy code
 pip install flask
 Run the Application
 Navigate to the project directory and run:

 bash
 Copy code
 python app.py
 The server will start at http://127.0.0.1:5000.




Design Choices :-

Framework: Flask was chosen for its simplicity and lightweight nature, making it ideal for small applications.

Data Storage: A dictionary-based in-memory storage was used instead of a database to meet the "no third-party library" constraint and keep the project simple.

Blueprint: Routes were organized using Flask Blueprints to improve modularity.
Code Organization: Separate files (db.py and model.py) were created for better structure and maintainability.


Assumptions and Limitations :-

Assumptions:

All book and member data is stored in memory and will be reset when the application stops.
Users will provide valid data when interacting with the API.
Limitations:

No database is implemented, so data is not persistent.
No input validation has been implemented.
Token-based authentication is not fully implemented (optional feature).
Optional Features (Implemented)
Search Functionality: Users can search for books by title or author using query parameters.
Pagination: (To be implemented if needed; not currently active in the provided code).
Token-Based Authentication: Not implemented due to time constraints.

Endpoints
1. /books
GET: List all books.
POST: Add a new book.
2. /books/<book_id>
GET: Fetch details of a book by ID.
PUT: Update an existing book.
DELETE: Delete a book.
3. /books/search
GET: Search for books by title or author.


Running Example
Here’s an example workflow:

Start the Server
bash
Copy code
python app.py
Add a Book
bash
Copy code
curl -X POST http://127.0.0.1:5000/books \
-H "Content-Type: application/json" \
-d '{"title": "New Book", "author": "Author Name", "published_year": 2024}'
List All Books
bash
Copy code
curl -X GET http://127.0.0.1:5000/books
Search for a Book
bash
Copy code
curl -X GET "http://127.0.0.1:5000/books/search?q=author"
