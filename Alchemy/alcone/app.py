from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello Samuel Oyerinde everyday is christmas'



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)