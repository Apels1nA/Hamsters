import falcon

from resources.index import *
from resources.auth import *


def make_route(app):

    app.add_route('/', IndexController())
    app.add_route('/users', RegisterController())
    app.add_route('/login', LoginController())
    app.add_route('/logout', LogoutController())
