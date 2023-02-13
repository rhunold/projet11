import pytest
import server


@pytest.fixture()
def app():
    app = server.app
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
        
@pytest.fixture()
def clubs_tests():
    server.clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "11"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "0"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "10"
        }
    ]

    return server.clubs

@pytest.fixture()
def competitions_tests():
    server.competitions = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }

    ]
    return server.competitions