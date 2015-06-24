from flask import Flask
from .tree_workshop import tree_mold
from .pages import pages_bp


app = Flask(__name__)

app.register_blueprint(pages_bp)
app.register_blueprint(tree_mold, url_prefix="/oak")
app.register_blueprint(tree_mold, url_prefix="/fir")
app.register_blueprint(tree_mold, url_prefix="/ash")