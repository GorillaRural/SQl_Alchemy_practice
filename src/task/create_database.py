from models.database import create_db, Session
from faker import Faker
from models.spaceship import Spaceship
from models.officer import Officer


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    # Loading JSON data
    list_of_json_data = [{
        "alignment": "Ally",
        "name": "Normandy",
        "class": "Corvette",
        "length": 216.3,
        "crew_size": 8,
        "armed": True,
        "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
    }, {
        "alignment": "Ally",
        "name": "Nrmandy",
        "class": "Corvette",
        "length": 216.3,
        "crew_size": 8,
        "armed": True,
        "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
    },
    {
        "alignment": "Ally",
        "name": "Nomandy",
        "class": "Corvette",
        "length": 216.3,
        "crew_size": 8,
        "armed": True,
        "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
    },
    {
        "alignment": "Ally",
        "name": "Norandy",
        "class": "Corvette",
        "length": 216.3,
        "crew_size": 8,
        "armed": True,
        "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
    },
    {
        "alignment": "Enemy",
        "name": "Normndy",
        "class": "Corvette",
        "length": 216.3,
        "crew_size": 8,
        "armed": True,
        "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
    }]

    # Creating Spaceship object and adding it to the session
    for json_data in list_of_json_data:
        spaceship = Spaceship(
            name=json_data['name'],
            alignment=json_data['alignment'],
            spaceship_class=json_data['class'],
            length=json_data['length'],
            crew_size=json_data['crew_size'],
            armed=json_data['armed'],
            officers=[Officer(**officer_data)
                    for officer_data in json_data['officers']]
        )
        session.add(spaceship)

        # Committing the changes to the database
        session.commit()

    # Closing the session
    session.close()
