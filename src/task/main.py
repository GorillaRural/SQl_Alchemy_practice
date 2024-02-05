import os
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from sqlalchemy import and_

from models.spaceship import Spaceship
from models.officer import Officer

if __name__ == "__main__":
    db_is_created=os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
 
    session = Session()
    for it in session.query(Spaceship):
        print(it)
    print('*'*30)