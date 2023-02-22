# Try to connect 
def test_connect(client, clubs_tests):
    club_test = clubs_tests[0]

    client.get('/')

    # Email is not recogized so show an error messsage
    response = client.post('/showSummary', data={"email": "invalid@email.com"})
    data = response.data.decode()
    assert "Email not found !" in data
    assert response.status_code == 200    

    # Email is recognized so connect the user
    response = client.post('/showSummary', data={"email": club_test['email']})
    data = response.data.decode()
    assert club_test['email'] in data
    assert response.status_code == 200


# Try to book 
def test_booking(client, clubs_tests, competitions_tests):

    club_test = clubs_tests[2]

    # Log the user
    response = client.post('/showSummary', data={"email": club_test['email']})
    data = response.data.decode()
    assert club_test['email'] in data
    assert response.status_code == 200
    
    # Club can't purchase less than 1 place
    competition_test = competitions_tests[0]    
    places = -1
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})
    data = response.data.decode()
    assert response.status_code == 200
    assert "You can reserve less than 1 place." in data    

    # Club do not have enought points to book
    competition_test = competitions_tests[0]    
    places = 14
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})
    data = response.data.decode()
    assert response.status_code == 200
    assert "You don\'t have enought points." in data

    # Club can't book more than 12 place per competition
    competition_test = competitions_tests[0]    
    places = 13
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})
    data = response.data.decode()
    assert response.status_code == 200
    assert "You can\'t reserve more than 12 places for a competition." in data
    
    # Club can't book for past competition
    competition_test = competitions_tests[0]    
    response = client.get(f'/book/{competition_test["name"]}/{club_test["name"]}')
    data = response.data.decode()
    assert response.status_code == 200
    assert "This competition has already taken place" in data
    

    # Club can book for futur competition
    competition_test = competitions_tests[1]    
    response = client.get(f'/book/{competition_test["name"]}/{club_test["name"]}')
    data = response.data.decode()
    assert response.status_code == 200
    assert "Places available" in data 
    
    # Club booking places for upcoming competition & deducing points
    competition_test = competitions_tests[1]    
    places = 5
    points_available = int(club_test["points"]) - places
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})
    data = response.data.decode()
    assert response.status_code == 200
    assert "reserved places" in data
    
    # Club can't book for futur competition if not enought places available
    competition_test = competitions_tests[2]    
    places = 6
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})
    data = response.data.decode()
    assert response.status_code == 200
    assert "because there is only" in data   
    