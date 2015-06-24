from flask import Blueprint, render_template


pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def index():
    data = {}
    data['trees'] = ['oak', 'fir', 'ash']
    data['sections'] = ['leaves', 'roots', 'rings']
    data['years'] = list(range(1975, 1980))

    return render_template('pages/index.html', data=data)

