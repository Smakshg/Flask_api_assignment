from model import Book, Member

BOOKS_DB: dict[int, Book] = {}
MEMBERS_DB: dict[int, Member] = {}

BOOK_ID_COUNTER = 1
MEMBER_ID_COUNTER = 1