from flask import Flask, render_template, request, redirect, flash
from database import *
import random
from werkzeug.utils import secure_filename
# from werkzeug.wsgi import LimitedStream
#
#
# class StreamConsumingMiddleware(object):
#
#     def __init__(self, app):
#         self.app = app
#
#     def __call__(self, environ, start_response):
#         stream = LimitedStream(environ['wsgi.input'],
#                                int(environ['CONTENT_LENGTH'] or 0))
#         environ['wsgi.input'] = stream
#         app_iter = self.app(environ, start_response)
#         try:
#             stream.exhaust()
#             for event in app_iter:
#                 yield event
#         finally:
#             if hasattr(app_iter, 'close'):
#                 app_iter.close()


app = Flask(__name__)
app.secret_key = '\x84\xef\xe5\x0c-Cc\x82\xf4l}\x9c\n\xd8\xbf\xf5;\x7fT\xf0\x15\xeb\xb0\xc0'
UPLOAD_FOLDER = '/home/kngine/submissions'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DB = Storage()
app.config['MAX_CONTENT_LENGTH'] = 250 * 1024 * 1024
# app.wsgi_app = StreamConsumingMiddleware(app.wsgi_app)

portfolio = [
    {'title': "Kngine'17", 'caption': 'To Infinity and Beyond', 'href': 'kngine17.jpg'},
    {'title': "Kngine'15", 'caption': 'The ultimatum of IT', 'href': 'kngine15.jpg'},
    {'title': "Kngine'13", 'caption': '4th Generation of IT', 'href': 'kngine13.jpg'},
    {'title': "Kngine'12", 'caption': 'For The Next Generation Of IT', 'href': 'Kngine12.jpg'},
]

lectures = [{'name': 'Malinda Alahakoon', 'img': 'malinda.jpg', 'caption': 'YouTuber @TechTrackShow',
             'facebook': 'https://www.facebook.com/MalindaOnline', 'twitter': 'https://twitter.com/malindaonline',
             'linkedin': '#'},
            {'name': 'Chanux Bro', 'img': 'chanux.jpg', 'caption': "Sri Lanka's Biggest Youtuber",
             'facebook': 'https://www.facebook.com/chanuxbropage', 'twitter': 'http://twitter.com/ChanuxBro',
             'linkedin': '#'},
            ]

sponsors = ['IIT']

competitions = [
    {'name': 'CyberCombat Vol. 2', 'id': 'cybercombat', 'info': 'Gaming competition', 'register': True},
    {'name': 'Pixelate', 'id': 'pixelate', 'info': 'Graphic Designing competition', 'register': True},
    {'name': 'Assemblage', 'id': 'assemblage', 'info': 'PC Assembling competition', 'register': False},
    {'name': 'Hyperlink', 'id': 'hyperlink', 'info': 'Web Designing competition', 'register': True},
    {'name': 'Scripter', 'id': 'scripter', 'info': 'Programming competition', 'register': True},
    {'name': 'Intellect', 'id': 'intellect', 'info': 'Quiz competition', 'register': False},
]

memes = ['rage.html', 'omgwhy.html', 'troll.html', 'wantdrink.html']


@app.route('/')
def homepage():
    # random.shuffle(portfolio)
    random.shuffle(lectures)
    random.shuffle(competitions)
    random.shuffle(memes)
    return render_template('home.html', portfolio=portfolio, lectures=lectures, competitions=competitions, memes=memes,
                           sponsors=sponsors)


@app.route('/register/CyberCombat/', methods=['POST'])
def register_gaming():
    try:
        if request.method == 'POST':
            q = 'INSERT INTO CyberCombat('
            for i in [i.replace('-', ' ').title() for i in list(request.form.keys())]:
                q += '`{}`, '.format(i)
            q = q[:-2] + ') VALUES('
            for _ in list(request.form.keys()):
                q += '?, '
            q = q[:-2] + ')'
            DB.put(q, tuple(request.form.values()))
            flash("Thanks for Registering Hope to See you at Kngine'18")
        else:
            flash('Invalid Request')
        return redirect(request.referrer)
    except Exception as e:
        LOG.log.exception(e)
        flash("Something Went Wrong Try again in a Bit")
        flash("If this continue happen please contact us")


@app.route('/register/Pixelate/', methods=['POST'])
def register_pixelate():
    try:
        if request.method == 'POST':
            dataDict = request.form.to_dict(flat=True)
            dataDict['Competition'] = 'Pixelate'
            LOG.log.info(str(request.files))
            LOG.log.info(str(dataDict))
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(get_dir(dataDict, file.filename))
            else:
                flash('Bad File Type only zip files are allowed')
                return redirect(request.referrer)
            dataDict['File Dir'] = get_dir(dataDict, file.filename)
            q = 'INSERT INTO Competitions('
            for i in [i.replace('-', ' ').title() for i in list(dataDict.keys())]:
                q += '`{}`, '.format(i)
            q = q[:-2] + ') VALUES('
            for _ in list(dataDict.keys()):
                q += '?, '
            q = q[:-2] + ')'
            DB.put(q, tuple(dataDict.values()))
            flash("Thanks you for Registering in Pixelate")
            flash("Hope to See you at Kngine'18")
        else:
            flash('Invalid Request')
        return redirect(request.referrer)
    except Exception as e:
        LOG.log.exception(e)
        flash("Something Went Wrong Try again in a Bit")
        flash("If this continue happen please contact us")


@app.route('/register/Hyperlink/', methods=['POST'])
def register_hyperlink():
    try:
        if request.method == 'POST':
            dataDict = request.form.to_dict(flat=True)
            dataDict['Competition'] = 'Hyperlink'
            LOG.log.info(str(request.files))
            LOG.log.info(str(dataDict))
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(get_dir(dataDict, file.filename))
            else:
                flash('Bad File Type only zip files are allowed')
                return redirect(request.referrer)
            dataDict['File Dir'] = get_dir(dataDict, file.filename)
            q = 'INSERT INTO Competitions('
            for i in [i.replace('-', ' ').title() for i in list(dataDict.keys())]:
                q += '`{}`, '.format(i)
            q = q[:-2] + ') VALUES('
            for _ in list(dataDict.keys()):
                q += '?, '
            q = q[:-2] + ')'
            DB.put(q, tuple(dataDict.values()))
            flash("Thanks you for Registering in Hyperlink")
            flash("Hope to See you at Kngine'18")
        else:
            flash('Invalid Request')
        return redirect(request.referrer)
    except Exception as e:
        LOG.log.exception(e)
        flash("Something Went Wrong Try again in a Bit")
        flash("If this continue happen please contact us")


@app.route('/register/Scripter/', methods=['POST'])
def register_scripter():
    try:
        if request.method == 'POST':
            dataDict = request.form.to_dict(flat=True)
            dataDict['Competition'] = 'Scripter'
            LOG.log.info(str(request.files))
            LOG.log.info(str(dataDict))
            file = request.files['file']

            if file and allowed_file(file.filename):
                file.save(get_dir(dataDict, file.filename))
            else:
                flash('Bad File Type only zip files are allowed')
                return redirect(request.referrer)
            dataDict['File Dir'] = get_dir(dataDict, file.filename)
            q = 'INSERT INTO Competitions('
            for i in [i.replace('-', ' ').title() for i in list(dataDict.keys())]:
                q += '`{}`, '.format(i)
            q = q[:-2] + ') VALUES('
            for _ in list(dataDict.keys()):
                q += '?, '
            q = q[:-2] + ')'
            DB.put(q, tuple(dataDict.values()))
            flash("Thanks you for Registering in Scripter")
            flash("Hope to See you at Kngine'18")
        else:
            flash('Invalid Request')
        return redirect(request.referrer)
    except Exception as e:
        LOG.log.exception(e)
        flash("Something Went Wrong Try again in a Bit")
        flash("If this continue happen please contact us")


@app.route('/contact/', methods=['POST'])
def contact():
    try:
        if request.method == 'POST':
            q = 'INSERT INTO Contact('
            for i in [i.title() for i in list(request.form.keys())]:
                q += '`{}`, '.format(i)
            q = q[:-2] + ') VALUES('
            for _ in list(request.form.keys()):
                q += '?, '
            q = q[:-2] + ')'
            DB.put(q, tuple(request.form.values()))
            flash("We Got The Message We will Reach Back to you ASAP")
        else:
            flash('Invalid Request')
        return redirect(request.referrer)
    except Exception as e:
        LOG.log.exception(e)
        flash("Something Went Wrong Try again in a Bit")
        flash("If this continue happen please contact by Number")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in 'zip'


def get_dir(data, filename):
    up_dir = os.path.join(UPLOAD_FOLDER, data['Competition'])
    up_dir = os.path.join(up_dir, secure_filename('{}_{}'.format(data['competitor-name'], data['project-name'])))
    if not os.path.exists(up_dir):
        os.makedirs(up_dir)
    up_dir = os.path.join(up_dir, secure_filename(filename))
    return up_dir


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
