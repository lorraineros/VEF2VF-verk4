import os
from flask import Flask, render_template, make_response

app = Flask(__name__,)

frettir= [
    [0,"Hello user",
     "How are you my friend?, Do you like my project? :)" 
     ], 
    [1,"Lets talk about baseball",
     " Baseball is a sport that dates back as far as 1744 and formats of the game have been in place until the modern era today. The game is predominantly big in North America, Canada and Japan. The game is played worldwide with the pinnacle of sport coming from the World Series of Baseball. Ironically, this event is only competed by North American teams."
     ],
    [2,"Lets talk about Basketball",
     "Basketball is a team sport where two teams, usually consisting of five players on each team, play against each other on a rectangular court. The objective is to get the ball through a hoop mounted high on a backboard on the opponent's side of the court, while preventing the opponent from shooting it into your team's hoop. It is a very popular sport worldwide, played with a round and usually orange ball that bounces. Basketball players mainly use skills such as dribbling, shooting, running, and jumping."
     ]
    ]

@app.route('/')
def Homepage():
    return render_template('index.tpl', frettir=frettir)

@app.route('/frett/<int:id>')
def newspage(id):
    return render_template('frett.tpl', frett=frettir[id], nr=id)

@app.route('/about')
def About():
    return render_template('about.tpl')

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.tpl'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, use_reloader=True)