from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators


class JobAdForm(FlaskForm):
    texttotest = TextAreaField(u'', [validators.Length(min=1)],
    default="""Clinical Strength Invisible Solid is our best protection that goes on dry. It absorbs odor while releasing a scent to keep you smelling clean and feeling dry. Did you know that heat, activity, and stress can all cause you to sweat and that stress sweat smells the WORST? That's because stress sweat comes from a different gland, causing more bacteria and more odor. Clinical Strength Invisible Solid—incredible protection, no matter what the day may bring."""
