from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.controller.main_controller.MainController import *

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(flask_app)

# Global, save the document tone
document_tone = ''

# Check if it's the first time to run
FIRST_TIME_RUNNING = True


class Todo(db.Model):
    """
    Database
    4 column, id, screen_name, content, tone
    """
    id = db.Column(db.Integer, primary_key=True)
    screenname = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    tone = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


# TODO: clean the database every time!!!
@flask_app.route('/', methods=['POST', 'GET'])
def index():
    global FIRST_TIME_RUNNING
    # When it's the first time to run, clean database.
    if (FIRST_TIME_RUNNING):
        db.create_all()
        db.drop_all()
        FIRST_TIME_RUNNING = False
    global document_tone
    # when the method is POST(button clicked)
    if request.method == 'POST':
        # clean the database(the table)
        db.drop_all()
        db.create_all()
        # get screen name
        target_screen_name = ''
        target_screen_name += '@'
        target_screen_name += request.form['screen_name']
        # Initialize Controller
        main_controller = MainController()
        # set screen name
        main_controller.get_screen_name(target_screen_name)
        # try to analyze and get result
        try:
            original_result = main_controller.get_tone_analysis_result()
        except Exception:
            return redirect('/')
        # process the analyze result and put it in the database.
        content = ''
        tone = ''
        # ERROR!!!
        try:
            document_tone = original_result["document_tone"]['tones'][0]['tone_name']
        except:
            print(document_tone)
        for r in original_result["sentences_tone"]:
            content += r["text"]
            for r2 in r["tones"]:
                tone += r2["tone_name"]
            if tone == '':
                tone += 'Not Recognized.'
            # build a new line in database
            new_line = Todo(screenname=target_screen_name, content=content, tone=tone)
            content = ''
            tone = ''
            # put the new line in session
            try:
                db.session.add(new_line)
            except:
                return 'db.session.add(new_line) fail!!'
        # try to commit the session
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue committing in db'
    # if the method is not POST, update the page with the data in database
    else:
        results = []
        try:
            results = Todo.query.order_by(Todo.id).all()
        except:
            return render_template('index.html', results=results, document_tone=document_tone)
        return render_template('index.html', results=results, document_tone=document_tone)


if __name__ == "__main__":
    flask_app.run(debug=True)
