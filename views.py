from flask import render_template, request, redirect
from main import app, db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/petprofile')
def petprofile():
    return render_template('petprofile.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/petsignin')
def petsignin():
    return render_template('petsignin.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/petedit')
def petedit():
    return render_template('petedit.html')

@app.route('/form')
def form():
    return render_template('form.html')