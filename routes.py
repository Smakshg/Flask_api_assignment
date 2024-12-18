from flask import Blueprint, request, jsonify
from db import BOOKS_DB, MEMBERS_DB, BOOK_ID_COUNTER, MEMBER_ID_COUNTER
from model import Book, Member

routes = Blueprint("routes", __name__)

@routes.route("/books", methods=["GET", "POST"])
def manage_books():
    global BOOK_ID_COUNTER
    if request.method == "POST":
        data = request.get_json()
        new_book: Book = {
            "id": BOOK_ID_COUNTER,
            "title": data["title"],
            "author": data["author"],
            "published_year": data["published_year"],
            "available": True
        }
        BOOKS_DB[BOOK_ID_COUNTER] = new_book
        BOOK_ID_COUNTER += 1
        return jsonify(new_book), 201
    return jsonify(list(BOOKS_DB.values())), 200

@routes.route("/books/<int:book_id>", methods=["GET", "PUT", "DELETE"])
def book_operations(book_id):
    if book_id not in BOOKS_DB:
        return jsonify({"error": "Book not found"}), 404
    
    if request.method == "GET":
        return jsonify(BOOKS_DB[book_id]), 200
    elif request.method == "PUT":
        data = request.get_json()
        BOOKS_DB[book_id].update(data)
        return jsonify(BOOKS_DB[book_id]), 200
    elif request.method == "DELETE":
        del BOOKS_DB[book_id]
        return jsonify({"message": "Book deleted"}), 200

@routes.route("/books/search", methods=["GET"])
def search_books():
    query = request.args.get("q", "").lower()
    filtered_books = [
        book for book in BOOKS_DB.values() 
        if query in book["title"].lower() or query in book["author"].lower()
    ]
    return jsonify(filtered_books), 200