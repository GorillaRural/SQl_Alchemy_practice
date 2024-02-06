import os
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from sqlalchemy import select, and_, union_all

from models.spaceship import Spaceship
from models.officer import Officer

def list_traitors():
    session = Session()
    query_ally = session.query(Officer.first_name, Officer.last_name, Officer.rank).\
        join(Spaceship).\
        filter(Spaceship.alignment == 'Ally')

    query_enemy = session.query(Officer.first_name, Officer.last_name, Officer.rank).\
        join(Spaceship).\
        filter(Spaceship.alignment == 'Enemy')
    
    # query_union = union_all(query_ally, query_enemy)

    # results = session.execute(query_union)
    # for row in results:
    #     first_name, last_name, rank = row
    #     print(f"Officer: {first_name} {last_name}, Rank: {rank}")

    # Finding the intersection of query_ally and query_enemy
    query_intersection = query_ally.intersect(query_enemy)

    # Executing the query and printing the results
    results = query_intersection.all()
    for first_name, last_name, rank in results:
        print(f"Officer: {first_name} {last_name}, Rank: {rank}")



if __name__ == "__main__":
    db_is_created=os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
    list_traitors()
