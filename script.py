from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

def get_headlines():
    user_pass_dict = {'user':'USERNAME',
                      'passwd':'PASSWORD',
                      'api_type':'json'}
    scss = requests.Session()
    scss.headers.update({'User-Agent': 'I am testing the alexa: sentdex'})
    scss.post('https://www.reddit.com/dev/api/', data = user_pass_dict)
    time.sleep(1)
    url = 'https://www.reddit.com/r/worldnews/.json?limit=10'
    html = scss.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '...'.join([i for i in titles])
    return titles

@app.route('/')
def homepage():
    return "hi there, how are u doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there!, would you like to open dashboards?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headlines_msg = 'The  available dashboards are: {}'.format(headlines)
    return statement(headlines_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Alright then! See you later!'
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)