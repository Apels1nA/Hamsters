import falcon
import hashlib

from schemas.user import UserManageSchema
from models.user import User
from libs.decorators import with_body_params
from config import config


class RegisterController(object):

    @with_body_params(UserManageSchema)
    def on_post(self, req, resp):
        user = User()
        user.email = req.parsed['email']
        user.login = req.parsed['login']
        password = req.parsed['password']+config['secure']['salt_password']
        user.password = hashlib.sha256(password.encode()).hexdigest()

        try:
            user.save()
        except Exception:
            raise falcon.HTTPUnauthorized()


class LoginController(object):
    def on_post(self, req, resp):
        email = req.parsed['email']
        password = req.parsed['password']+config['secure']['salt_password']

        try:
            user = (
                User
                .select(User.id)
                .where(User.email == email)
                .where(User.password == hashlib.sha256(password.encode()).hexdigest())
                .get()
            )
        except Exception:
            raise falcon.HTTPUnauthorized()
        

class LogoutController(object):
    def on_get():
        remove_session(req.parsed['user_session'])