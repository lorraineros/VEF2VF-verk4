import os
from flask import Flask, render_template, make_response

app = Flask(__name__,)

frettir= [
    [0,"Kitten Sees Itself In The Mirror For The First Time",
     "The world is a strange place for a newborn kitten - everything is huge and confusing, and you learn new things everyday. This little cutie named Wiske had an absolutely adorable reaction to her first time seeing a mirror, when she clearly couldn't tell what was going on.",
     "some@email.com"
     ], 
    [1,"Cats With Human Mouths",
     "It may look like something from the depths of your worst nightmares, but Cats With Human Mouths is actually pretty hilarious. Even if it will haunt you for days.",
     "some2@email.com"
     ],
    [2,"Cats Vs. Their Own Shadows",
    "Many cats don't quite understand the laws of physics, meaning the can often think their own shadow is an enemy cat ready to pounce, rather than the absence of light caused by their own bodies.",
    "some3@email.com"
     ],
    [3,"Cats Witness Ceiling Fan Spinning for First Time",
    "When this cat owner turned on his ceiling fan in his bedroom for the first time, his one-year-old cats were astonished to see the magnificent spinning machine of wonder that took place above them",
    "some4@email.com"
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