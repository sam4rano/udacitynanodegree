import sys
from flask import Flask, render_template, request, abort, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

db = SQLAlchemy(app)

class Todos(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'
 
db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
  error = False
  body = {}
  try:
    description = request.get_json()['description']
    todo = Todos(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
    
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if error:
    abort(400)
  else:
    return jsonify(body)
  # return redirect(url_for('index'))

@app.route('/')
def index():
  return render_template('index.html', data=Todos.query.all())


#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(debug=True, use_debugger=False, use_reloader=True, host="0.0.0.0", port=3000)