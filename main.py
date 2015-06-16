"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template
from wechat_formatter.formatter import bp_wechat_formatter

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__, static_folder='common')

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# blueprints
app.register_blueprint(bp_wechat_formatter)



@app.route('/')
def wechat_format():
    """Return a friendly HTTP greeting."""
    return 'Hello World'




@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
