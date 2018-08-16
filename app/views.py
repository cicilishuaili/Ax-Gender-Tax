from flask import Flask
from flask import render_template, redirect, request
from wtforms.validators import ValidationError
import datetime
from app import app, db
from forms import JobAdForm
from models import JobAd, CodedWordCounter
from wordlists import *
import dill as pickle
from nltk.classify import NaiveBayesClassifier


@app.route('/', methods=['GET', 'POST'])
def home():
    form = JobAdForm()
    if request.method == "POST" and form.validate_on_submit():
        ad = JobAd(form.texttotest.data)
        return redirect('results/{0}'.format(ad.hash))
    return render_template('home.html',
                          form=form)

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/methods')
def methods():
    return render_template('methods.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/results/<ad_hash>')
def results(ad_hash):
    job_ad = JobAd.query.get_or_404(ad_hash)
    masculine_coded_words, feminine_coded_words = job_ad.list_words()
    return render_template('results.html', job_ad=job_ad,
        masculine_coded_words=masculine_coded_words,
        feminine_coded_words=feminine_coded_words,
        explanation=explanations[job_ad.coding])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
