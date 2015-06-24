# An example
from flask import Blueprint

tree_mold = Blueprint('mold', __name__)

@tree_mold.route('/')
def tree_index():
    return 'Tree index page'

@tree_mold.route('/leaves/')
def leaves():
    return 'This tree has leaves'

@tree_mold.route('/roots/')
def roots():
    return 'And roots as well'

@tree_mold.route('/rings/')
@tree_mold.route('/rings/<int:year>/')
def rings(year=None):
    if year is None:
        year = '[this is the index page for rings.]'
    return 'Looking at the rings for {year}'.format(year=year)