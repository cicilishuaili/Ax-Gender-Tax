from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators


class JobAdForm(FlaskForm):
    texttotest = TextAreaField(u'', [validators.Length(min=1)],
    default="""Dry Idea Anti-Perspirant Deodorant Roll-On Unscented 3.25 oz Dry Idea Unscented Roll On Deodorant uses an excellent formula to keep your skin protected throughout the day. It's hypoallergenic and comes with vitamin E to revitalize your skin. This 3.25 fl oz Dry Idea roll on product is soft and easy to apply. Dry Idea Anti-Perspirant Deodorant Roll-On Unscented 3.25 Oz: Hypoallergenic Unscented deodorant gives you pulse activated wetness protection. Up to 72 hour odor protection. Simple to apply Made with vitamin E for your skin""")
