from sqlalchemy.orm import Session
from tornado.web import HTTPError

from models.models import SchoolModel


def get_school_or_404(db_session: Session, school_id):
    school_db = db_session.query(SchoolModel).filter_by(
        id=school_id
    ).first()
    if not school_db:
        raise HTTPError(404, 'Not found school')
    return school_db
