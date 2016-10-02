import os,json

from twilio import twiml
from twilio.rest import TwilioRestClient
from flask import Flask, render_template, request, redirect, make_response, Response
# from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from time import time
from random import random
from watson_developer_cloud import ToneAnalyzerV3


TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
USER_NUMBER = os.environ.get('USER_NUMBER', None)
IBM_USERNAME = os.environ.get('IBM_USERNAME', None)
IBM_PASSWORD = os.environ.get('IBM_PASSWORD', None)

app = Flask(__name__)
twilio_client = TwilioRestClient()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/userdb'
# db = SQLAlchemy(app)

tone_analyzer = ToneAnalyzerV3(
   username=IBM_USERNAME,
   password=IBM_PASSWORD,
   version='2016-05-19')

# Create our database model
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True)
#     phone = db.Column(db.String(10), unique=True)
#     entries = db.relationship('Entry', backref='users',
#                                 lazy='dynamic')

#     def __init__(self, email):
#         self.email = email

#     def __repr__(self):
#         return '<E-mail %r>' % self.email

#  class Prompt(db.Model):
#    __tablename__ = "prompts"
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(120), unique=True)

# class Entry(db.Model):
#     __tablename__ = "entries"
#     id = db.Column(db.Integer, primary_key=True)
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     # prompt_id = db.Column(db.Integer, db.ForeignKey('prompt.id'))
#     anger_response = db.Column(db.Numeric)
#     disgust_response = db.Column(db.Numeric)
#     fear_response = db.Column(db.Numeric)
#     joy_resposne = db.Column(db.Numeric)
#     sadness_response = db.Column(db.Text)
#     recevied_date = db.Column(db.DateTime)

#     def __init__(self, anger, disgust, fear, joy, sadness, pub_date=None):
#         self.prompt_id = prompt_id
#         if pub_date is None:
#             pub_date = datetime.utcnow()
#         self.pub_date = pub_date
#         self.anger_response = anger
#         self.disgust_response = disgust
#         self.fear_response = fear
#         self.joy_resposne = joy
#         self.sadness_response = sadness

    # def __repr__(self):
    #     return '< %r>' % self.email

def analyze_tone(text):
    # print tone_analyzer.tone(text=text)
    print(json.dumps(tone_analyzer.tone(text=text), indent=2))
    return
    # return tone_json['document_tone']['tone_categories']

    # anger_response = document_tone['']
 #    disgust_response = db.Column(db.Numeric)
 #    fear_response = db.Column(db.Numeric)
 #    joy_resposne = db.Column(db.Numeric)
 #    sadness_response = db.Column(db.Text)

@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/twilio', methods=['GET','POST'])
def twilio_post():
    response = twiml.Response()
    
    # if request.form['From'] == USER_NUMBER:
    message = request.form['Body']

    if "Hi" in message:
        response.message("Hey there, how is your day going?")
        return str(response)
    elif 'bad' in message:
        analyze_tone(message)
        response.message("Aw, I'm sorry to hear that. I hope your day improves!")
        return str(response)
    elif 'good' in message:
        analyze_tone(message)
        response.message("That's great! Keep it up!")
        return str(response)
    elif 'later' in message:
        analyze_tone(message)
        response.message("Fiiiiiine. ;) Talk to you later today!")
        return str(response)
    elif 'chance' in message:
        analyze_tone(message)
        response.message("Good Luck! But remember if we win, I get a cut of the prize...")
        return str(response)
    elif 'nervous' in message:
        analyze_tone(message)
        response.message("Don't be nervous, you're doing great!")
        return str(response)
    else:
        response.message("Noted. Anything else?")
        analyze_tone(message)
        
    return Response(response.toxml(), mimetype="text/xml"), 200


# def display_results(data):
#     data = json.loads(str(data))
    
#     document_tone = 
#     for i in data['document_tone']['tone_categories']:
#         print(i['category_name'])
#         print("-" * len(i['category_name']))
#         for j in i['tones']:
#             print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
#         print()
#     print()




if __name__ == '__main__':
    app.debug = True
    app.run()