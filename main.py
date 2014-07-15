__author__ = 'rm'

import bottle

app = bottle.Bottle()


@app.get('/')
@bottle.jinja2_view('homepage.html')
def get_homepage():
    return {'title': 'Homepage'}


@app.get('/tasks/cron/daily/parser')
def cron_daily_parse():
    pass


app.run(server='gae', debug=False)