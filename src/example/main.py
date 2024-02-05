import os
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from sqlalchemy import and_

from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group

if __name__ == "__main__":
    db_is_created=os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

 
    session = Session()
    for it in session.query(Lesson):
        print(it)
    print('*'*30)

    session = Session()
    for it in session.query(Lesson).filter(Lesson.id > 3):
        print(it)
    print('*'*30)

    session = Session()
    for it in session.query(Lesson).filter(and_(Lesson.id >= 3), Lesson.lesson_title.like('Ф%')):
        print(it)
    print('*'*30)

    session = Session()
    for it in session.query(Student).join(Group).filter(Group.group_name == '1-МДА-7'):
        print(it)
    print('*'*30)