from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quote()
    pitches=Pitches.query.all()
    identification = Pitches.user_id
    posted_by = User.query.filter_by(id=identification).first()
    user = User.query.filter_by(id=current_user.get_id()).first()

    recent_post = Pitches.query.order_by(desc(Pitches.id)).all()

    return render_template('pitches.html', quote=quote, pitches=pitches, posted_by=posted_by, user=user, recent_post=recent_post)