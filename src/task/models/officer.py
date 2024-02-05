from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from models.database import Base


class Officer(Base):
    __tablename__ = 'officers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    rank = Column(String)
    spaceship_name = Column(String, ForeignKey('spaceships.name'))
    spaceship = relationship('Spaceship', back_populates='officers')
