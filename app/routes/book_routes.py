from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from ..db import db
from .route_utilities import create_model, validate_model, get_models_with_filters

bp = Blueprint("bp", __name__, url_prefix="/books")

@bp.post("")
def create_book():
    request_body = request.get_json()

    # try:
    #     new_book = Book.from_dict(request_body)
        
    # except KeyError as error:
    #     response = {"message": f"Invalid request: missing {error.args[0]}"}
    #     abort(make_response(response, 400))

    # db.session.add(new_book)
    # db.session.commit()

    # return new_book.to_dict(), 201
    return create_model(Book, request_body)

@bp.get("")
def get_all_books():
    # # add check if the `title` query param is present as a column in DB
    # # title_param = request.args.get("title")
    # # if title_param:
    # #     query = db.select(Book).where(Book.title.ilike(f"%{title_param}%")).order_by(Book.id)
    # # else:
    # #     query = db.select(Book).order_by(Book.id)
    # # REORGANIZING to apply 2 filters:
    # query = db.select(Book)

    # title_param = request.args.get("title")
    # if title_param:
    #     query = query.where(Book.title.ilike(f"%{title_param}%"))

    # description_param = request.args.get("description")
    # if description_param:
    #     query = query.where(Book.description.ilike(f"%{description_param}%"))

    # query = query.order_by(Book.id)
    # books = db.session.scalars(query)
    # # We could also write the line above as:
    # # books = db.session.execute(query).scalars()

    # query = query.order_by(Book.id)

    # books_response = []
    # for book in books:
    #     books_response.append(book.to_dict())
    # return books_response

    return get_models_with_filters(Book, request.args)

@bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_model(Book, book_id)
    return book.to_dict()

@bp.put("/<book_id>")
def update_book(book_id):
    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

# @bp.put("/<book_id>")
# def update_book(book_id):
#     book = validate_model(Book, book_id)
#     request_body = request.get_json()

#     book.title = request_body.get("title", book.title)
#     book.description = request_body.get("description", book.description)

#     # Validate and update author if provided
#     author_id = request_body.get("author_id")
#     if author_id is not None:
#         author = db.session.get(Author, author_id)
#         if not author:
#             response = {"message": f"Author {author_id} not found"}
#             abort(make_response(response, 404))
#         book.author = author

#     db.session.commit()
#     return Response(status=204, mimetype="application/json")

@bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")