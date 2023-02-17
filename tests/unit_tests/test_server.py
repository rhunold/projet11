
    
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



# If the competition date has passed, show an error message
def test_cant_reserve_past_competition(client, clubs_tests, competitions_tests):
    club_test = clubs_tests[0]['name']
    competition_test = competitions_tests[0]['name']

    response = client.get(f'/book/{competition_test}/{club_test}')
    data = response.data.decode()
    assert response.status_code == 200
    assert "This competition has already taken place" in data
    
    
# If the competition date has not been passed, allow to book places
def test_can_reserve_futur_competition(client, clubs_tests, competitions_tests):
    club_test = clubs_tests[0]['name']
    competition_test = competitions_tests[1]['name']

    response = client.get(f'/book/{competition_test}/{club_test}')
    data = response.data.decode()
    assert response.status_code == 200
    assert "Places available" in data
    
    
# Update Club point after booking
def test_update_club_points_after_booking(client, clubs_tests, competitions_tests):
    club_test = clubs_tests[1]
    competition_test = competitions_tests[1]
    places = 1
    points_available = int(club_test["points"]) - places
    response = client.post('/purchasePlaces', data={"club": club_test["name"],
                                                    "competition": competition_test["name"],
                                                    "places": places})

    data = response.data.decode()

    assert response.status_code == 200
    assert f'{points_available}' in data
    

# Test display list_clubs page
def test_display_list_clubs_page(client, clubs_tests):
    club_test = clubs_tests[1]    
    response = client.get("/list_clubs")
    data = response.data.decode()
    assert f"{clubs_tests[0]['name']}" in data
    assert response.status_code == 200

# Test logout