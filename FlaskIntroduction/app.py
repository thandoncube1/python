from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r', self.id


# Setting up the database using Alchemy
with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    print(task_id)
    todo = Todo.query.get_or_404(task_id)

    try:
        db.session.delete(todo)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting that task.'


@app.route('/update/<int:task_id>', methods=['POST', 'GET'])
def update(task_id):
    task = Todo.query.get_or_404(task_id)

    if request.method == 'POST':
        # Take the task content and save the input from the form
        task.content = request.form['content']

        try:
            # no need to add, commit the change to the same id
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error updating the task'
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)