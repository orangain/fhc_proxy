#coding: utf-8

import os
import urllib
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/weather')
def weather():
    date = request.args['date']
    city = request.args['city']

    return _get_weather(date, city)

def _get_weather(date, city):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=' + city

    f = urllib.urlopen(url)
    api_response = json.loads(f.read())

    for forecast in api_response['forecasts']:
        if forecast['dateLabel'] == date:
            return u'%sのてんきは%sです' % (date, forecast['telop'])

    return ''


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
