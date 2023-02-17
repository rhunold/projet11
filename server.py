import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("Email not found !")
        return render_template("index.html")
    else:
        return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
  
        if foundClub and foundCompetition:
            competition_date = datetime.datetime.strptime(foundCompetition['date'], "%Y-%m-%d %H:%M:%S")
            today = datetime.datetime.now()
            if today > competition_date:
                flash("This competition has already taken place. Please choose another one.")
                return render_template('welcome.html', club=foundClub, competitions=competitions)
            else:
                return render_template('booking.html',club=foundClub,competition=foundCompetition)
    except IndexError:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    
    if placesRequired <= 0:
        flash("You can reserve less than 1 place.")
        return render_template('booking.html', club=club, competition=competition)
    elif placesRequired > int(club["points"]):
        flash("You don't have enought points.")
        return render_template('booking.html', club=club, competition=competition)
    elif placesRequired > 12:
        flash("You can't reserve more than 12 places for a competition.")
        return render_template('booking.html', club=club, competition=competition)    
    elif placesRequired > int(competition['numberOfPlaces']):
        flash(f"You can't reserve {places_required} because there is only {competition['numberOfPlaces']} available.")
        return render_template('booking.html', club=club, competition=competition)
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        club["points"] = int(club["points"]) - placesRequired
        flash("Great-booking complete!")
        flash(f"{competition['name']} reserved places: {placesRequired}")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route("/list_clubs")
def list_clubs():
    return render_template("list_clubs.html", clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8000, debug=True)