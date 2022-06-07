from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ ='todos' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f'<Person ID: {self.id}, name:{self.name}>'

# db.create_all() since we are using flask-migrate no need to use db_create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello Big ' + person.name 


if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0", port=3000)

