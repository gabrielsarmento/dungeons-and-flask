from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class BookModel(Base):
    __tablename__ = 'books'

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


class SpellModel(Base):
    __tablename__ = 'spells'

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    level = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    casting_time = Column(String(256), nullable=False)
    components = Column(String(256), nullable=False)
    duration = Column(String(256), nullable=False)
    school_id = Column(String(36), ForeignKey('schools.id'), nullable=False)
    range = Column(String(256), nullable=False)
    is_ritual = Column(Boolean, nullable=False)
    book_id = Column(String(36), ForeignKey('books.id'), nullable=False)

    school = relationship('SchoolModel', back_populates='spells')
    book = relationship('BookModel')


class SchoolModel(Base):
    __tablename__ = 'schools'

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    book_id = Column(String(36), ForeignKey('books.id'), nullable=False)

    book = relationship('BookModel')
    spells = relationship('SpellModel')
