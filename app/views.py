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
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
import pandas as pd
import os
from bokeh.models import HoverTool
from bokeh.models import Span
from bokeh.models import Arrow, NormalHead
from bokeh.models import Label
from bokeh.models import ColumnDataSource, PrintfTickFormatter, LabelSet
from bokeh.plotting import figure
import numpy as np

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

    cd = os.getcwd()
    with open(cd+"/app/wordsDF.pkl", 'rb') as f:
        words_df = pickle.load(f)

    HI_words_df = words_df[(abs(words_df.ratio.values)>10) | (abs(words_df.coef.values)>2)| ((words_df.coef.values)>2)]

    if job_ad.gender == "pink":
        coded_words = feminine_coded_words
    elif job_ad.gender == "blue":
        coded_words = masculine_coded_words
    else:
        coded_words = masculine_coded_words + feminine_coded_words

    label_words_df = words_df[(words_df.word.isin(coded_words)) & (words_df.coef.values>0)]

    min_x = HI_words_df.ratio.values.min()
    min_y = HI_words_df.coef.values.min()
    max_x = HI_words_df.ratio.values.max()
    #max_y = HI_words_df.coef.values.max()
    max_y = 6

    p = figure(x_range=(min_x-40, max_x+10), y_range=(min_y-1, max_y+1), title="High Impact Words in Deodorant Descriptions",
              plot_width=600, plot_height=600, background_fill_color='#F0F0F0',border_fill_color='#F0F0F0')

    p.ray(x=[0], y=[0], length=0, angle=0, line_width=1, line_color='black')
    p.ray(x=[0], y=[0], length=0, angle=np.pi, line_width=1, line_color='black')
    p.ray(x=[0], y=[0], length=0, angle=np.pi*3/2, line_width=1, line_color='black')
    p.ray(x=[0], y=[0], length=0, angle=np.pi*1/2, line_width=1, line_color='black')

    p.scatter(x='ratio',y='coef',alpha = 1, size = 8,
           color = 'deeppink', source=ColumnDataSource(label_words_df[label_words_df.gender=='f']))
    p.scatter(x='ratio',y='coef',alpha = 1, size = 8,
           color = 'deepskyblue', source=ColumnDataSource(label_words_df[label_words_df.gender=='m']))
    p.scatter(x='ratio',y='coef', legend = "Female",alpha = 0.7, size = 4,
           color = 'deeppink', source=ColumnDataSource(HI_words_df[HI_words_df.gender=='f']))
    p.scatter(x='ratio',y='coef', legend = "Male", alpha = 0.7, size = 4,
           color = 'deepskyblue', source=ColumnDataSource(HI_words_df[HI_words_df.gender=='m']))

    if job_ad.gender == "pink" or job_ad.gender == "purple":
        labels_f = LabelSet(x='ratio', y='coef', text='word', level='glyph',
        x_offset = -2, text_align = 'right',text_font_size="10pt",
        source=ColumnDataSource(label_words_df[label_words_df.gender=='f']))
        p.add_layout(labels_f)
    elif job_ad.gender == "blue" or job_ad.gender == "purple":
        labels_m = LabelSet(x='ratio', y='coef', text='word', level='glyph',
        x_offset = 2, text_font_size="10pt",
        source=ColumnDataSource(label_words_df[label_words_df.gender=='m']))
        p.add_layout(labels_m)

    p.yaxis.axis_line_color = None
    p.xaxis.axis_line_color = None
    p.yaxis.major_tick_line_color = None
    p.xaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.minor_tick_line_color = None
    p.outline_line_color = None

    p.xaxis.axis_label = "Gender Likelihood Ratio"
    p.yaxis.axis_label = "Relative Impact on Price"
    p.yaxis.axis_label_text_font_style = 'bold'
    p.xaxis.axis_label_text_font_style = 'bold'
    p.xaxis.axis_label_text_font_size = '1em'
    p.xaxis.major_label_text_font_size = '1em'
    p.yaxis.axis_label_text_font_size = '1em'
    p.yaxis.major_label_text_font_size = '1em'
    p.title.text_font_size = '1.3em'
    p.xaxis[0].formatter = PrintfTickFormatter(format="%uX")
    p.legend.location = "bottom_right"
    p.legend.label_text_font_size = '1em'
    p.legend.background_fill_color = '#F0F0F0'
    p.legend.border_line_color = None
    p.legend.background_fill_alpha = 0

    #p.xgrid.grid_line_color = None
    #p.ygrid.grid_line_color = None
    hover = HoverTool(
                tooltips=[
                    ('word', '@word')])
    p.add_tools(hover)

    p.add_layout(Arrow(end=NormalHead(size=10,fill_color='#A9A9A9',line_color='#A9A9A9'),
                       x_start=min_x-18, y_start=max_y, x_end=min_x-20, y_end=max_y))
    p.add_layout(Arrow(end=NormalHead(size=10,fill_color='#A9A9A9',line_color='#A9A9A9'),
                       x_start=min_x-22, y_start=max_y-0.2, x_end=min_x-22, y_end=max_y-0.1))
    p.add_layout(Arrow(end=NormalHead(size=10,fill_color='#A9A9A9',line_color='#A9A9A9'),
                       x_start=max_x, y_start=max_y, x_end=max_x+2, y_end=max_y))
    p.add_layout(Arrow(end=NormalHead(size=10,fill_color='#A9A9A9',line_color='#A9A9A9'),
                       x_start=min_x-22, y_start=min_y-0.2, x_end=min_x-22, y_end=min_y-0.3))
    notes_f = Label(x=min_x-16, y=max_y-0.16,text='More Likely Female',text_color='#A9A9A9')
    notes_x = Label(x=min_x-20, y=max_y-0.38,text='Higher Cost',text_align='right',angle=np.pi/2,text_color='#A9A9A9')
    notes_y = Label(x=min_x-19.5, y=min_y,text='Lower Cost',angle=np.pi/2,text_color='#A9A9A9')
    notes_m = Label(x=max_x-2, y=max_y-0.16,text='More Likely Male',text_align='right',text_color='#A9A9A9')
    p.add_layout(notes_x)
    p.add_layout(notes_f)
    p.add_layout(notes_y)
    p.add_layout(notes_m)

    script, div = components(p)

    resources = INLINE.render()

    html = render_template('results.html', job_ad=job_ad,
        masculine_coded_words=masculine_coded_words,
        feminine_coded_words=feminine_coded_words,
        explanation=explanations[job_ad.coding],
        gender=job_ad.gender,
        plot_script=script, plot_div=div, resources=resources)
    return encode_utf8(html)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
