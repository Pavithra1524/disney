from flask import Flask, render_template, request, redirect, jsonify, url_for
from utils.db import db
from models.movies import *
from static.images import  *
from static.videos import *

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True

db.init_app(flask_app)
with flask_app.app_context():
    db.create_all()

@flask_app.route('/')
def home():
        return render_template('home.html')

@flask_app.route('/index')
def index():
    return render_template('index.html')

@flask_app.route('/inde')
def inde():
    return render_template('indexx.html')

@flask_app.route('/login')
def login():
    login = Login.query.all()
    return render_template('login.html', content=login)

@flask_app.route('/logout')
def logout():
    return render_template('logout.html')

@flask_app.route('/exit')
def exit():
    return render_template('exit.html')

@flask_app.route('/subscript')
def subscript():
     return render_template('subscript.html')

@flask_app.route('/movies')
def movies():
     movies = Movies.query.all()
     return render_template('movies.html', content=movies)

@flask_app.route('/moviess')
def moviess():
     movies = Movies.query.all()
     return render_template('moviess.html', content=movies)

@flask_app.route('/add-movies')
def add_movies():
    return render_template('add_movies.html')

@flask_app.route('/add')
def add():
    return render_template('add.html')

@flask_app.route('/buy')
def buy():
    buynow = Buynow.query.all()
    return render_template('buy.html',content = buynow)

@flask_app.route('/action')
def action():
    return render_template('action.html')

@flask_app.route('/adventure')
def adventure():
    return render_template('adventure.html')

@flask_app.route('/horror')
def horror():
    return render_template('horror.html')

@flask_app.route('/national')
def national():
    return render_template('national.html')

@flask_app.route('/actions')
def actions():
    return render_template('actions.html')

@flask_app.route('/adventures')
def adventures():
    return render_template('adventures.html')

@flask_app.route('/horrors')
def horrors():
    return render_template('horrors.html')

@flask_app.route('/nationals')
def nationals():
    return render_template('nationals.html')

@flask_app.route('/submit', methods=['POST'])
def submit():
    movies_director = request.form['movies_director']
    movies_cast = request.form['movies_cast']
    movies_country = request.form['movies_country']
    movies_title = request.form['movies_title']
    movies_description = request.form['movies_description']
    movies_release_year = request.form['movies_release_year']
    movies= request.form.get('id')
    record = Movies.query.get(movies)
    if record:
            record.movies_title = movies_title
            record.movies_description = movies_description
            record.movies_release_year = movies_release_year
            record.movies_director = movies_director
            record.movies_cast = movies_cast
            record.movies_country = movies_country
    else:
            new_movies = Movies(title=movies_title, description=movies_description, release_year=movies_release_year, director = movies_director, cast = movies_cast, country = movies_country )
            db.session.add(new_movies)
    db.session.commit()
    return redirect(url_for('movies'))

@flask_app.route('/submitt', methods=['POST'])
def submitt():
    movies_director = request.form['movies_director']
    movies_cast = request.form['movies_cast']
    movies_country = request.form['movies_country']
    movies_title = request.form['movies_title']
    movies_description = request.form['movies_description']
    movies_release_year = request.form['movies_release_year']
    movies= request.form.get('id')
    record = Movies.query.get(movies)
    if record:
            record.movies_title = movies_title
            record.movies_description = movies_description
            record.movies_release_year = movies_release_year
            record.movies_director = movies_director
            record.movies_cast = movies_cast
            record.movies_country = movies_country
    else:
            new_movies = Movies(title=movies_title, description=movies_description, release_year=movies_release_year, director = movies_director, cast = movies_cast, country = movies_country )
            db.session.add(new_movies)
    db.session.commit()
    return redirect(url_for('moviess'))

@flask_app.route('/submi' ,methods=['POST'])
def submi():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    card_name = form_data.get('card_name')
    card_number = form_data.get('card_number')
    expiry_date = form_data.get('expiry_date')
    card_cvv = form_data.get('card_cvv')

    buynow = Buynow(name=card_name, card_number=card_number, expiry_date=expiry_date, cvv=card_cvv)
    db.session.add(buynow)
    db.session.commit()
    print("submitted successfully")
    return redirect('/inde')

@flask_app.route('/sub', methods=['POST'])
def sub():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    email = form_data.get('email')
    password = form_data.get('password')
    login = Login(email=email, password=password)
    db.session.add(login)
    db.session.commit()
    print("submitted successfully")
    return redirect('/index')

@flask_app.route('/subm', methods=['POST'])
def subm():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")
    register_name = form_data.get('register_name')
    register_email = form_data.get('register_email')
    register_password = form_data.get('register_password')
    register = Register(name=register_name, email=register_email, password=register_password)
    db.session.add(register)
    db.session.commit()
    print("submitted successfully")
    return redirect('/login')

@flask_app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete_user(id):
    movies = Movies.query.get(id)
    print("movies: {}".format(movies))

    if not movies:
        return jsonify({'message': 'movie not found'}), 404
    try:
        db.session.delete(movies)
        db.session.commit()
        return jsonify({'message': 'movie deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the data {}'.format(e)}), 500

@flask_app.route('/update_movies/<int:id>', methods=['GET', 'POST'])
def update_movies(id):
    movies = Movies.query.get_or_404(id)
    print(movies.id)
    if not movies:
        return jsonify({'message': 'movies not found'}), 404

    if request.method == 'POST':
        try:
            print("form data: ",request.form)
            movies.director = request.form.get('movies_director',movies.director)
            movies.cast = request.form.get('movies_cast',movies.cast)
            movies.country = request.form.get('movies_country',movies.country)
            movies.title = request.form.get('movies_title',movies.title)
            movies.description = request.form.get('movies_description',movies.description)
            movies.release_year = request.form.get('movies_release_year',movies.release_year)

            db.session.commit()
            return redirect(url_for('movies'))

        except Exception as e:
            db.session.rollback()
            return "there is an issue while updating the record"
    return render_template('edit.html', movies=movies)

@flask_app.route('/update_moviess/<int:id>', methods=['GET', 'POST'])
def update_moviess(id):
    movies = Movies.query.get_or_404(id)
    print(movies.id)
    if not movies:
        return jsonify({'message': 'movies not found'}), 404

    if request.method == 'POST':
        try:
            print("form data: ",request.form)
            movies.director = request.form.get('movies_director',movies.director)
            movies.cast = request.form.get('movies_cast',movies.cast)
            movies.country = request.form.get('movies_country',movies.country)
            movies.title = request.form.get('movies_title',movies.title)
            movies.description = request.form.get('movies_description',movies.description)
            movies.release_year = request.form.get('movies_release_year',movies.release_year)

            db.session.commit()
            return redirect(url_for('moviess'))

        except Exception as e:
            db.session.rollback()
            return "there is an issue while updating the record"
    return render_template('editt.html', movies=movies)

if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )
