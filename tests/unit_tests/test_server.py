
    
# tests Login 
def test_login_valid_email(client, clubs_tests):
    club = clubs_tests[0]
    response = client.post("/showSummary", data={"email": club['email']})
    data = response.data.decode()
    assert club['email'] in data
    assert response.status_code == 200

    
def test_login_invalid_email(client):
    invalid_email = "test@gmail.com"
    response = client.post("/showSummary", data={"email": invalid_email})
    data = response.data.decode()
    assert "Email not found !" in data
    assert response.status_code == 200


# Clubs should not be able to use more than their points allowed
def test_purchasePlaces_not_enough_points(client, clubs_tests, competitions_tests):
    club_test = clubs_tests[0]
    competition_test = competitions_tests[0]
    places = 5
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})

    data = response.data.decode()

    assert response.status_code == 200
    assert "You don\'t have enought points." in data
    
    
# Clubs shouldn't be able to book more than 12 places per competition
def test_purchasePlaces_not_more_12points_per_competition(client, clubs_tests, competitions_tests):
    club_test = clubs_tests[1]
    competition_test = competitions_tests[1]
    places = 13
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})

    data = response.data.decode()
    assert response.status_code == 200
    assert "You can\'t reserve more than 12 places for a competition." in data

