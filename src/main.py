from flask import Flask

from application import views

# This could be done in init
app = Flask(__name__, template_folder='./application/templates')

app.add_url_rule('/', 'home', view_func=views.home)

app.add_url_rule('/index', 'index', view_func=views.index)

# Errors
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
