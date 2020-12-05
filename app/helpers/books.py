from sqlalchemy.orm import Session
from tornado.web import HTTPError

from models.models import BookModel


def get_book_or_404(db_session: Session, book_id):
    book = db_session.query(BookModel).filter_by(
        id=book_id
    ).first()
    if not book:
        raise HTTPError(404, 'Not found book')
    return book
