from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app is for /router
# db is for /model


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

db = SQLAlchemy(app)
db.create_all()

app.run(debug=True)