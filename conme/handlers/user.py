"""User handler"""
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid_handlers import action

import base as base

from conme.models import DBSession, User
from conme.forms.user import LoginForm, RegistrationForm

class UserHandler(base.Handler):
    @action(renderer='user/view.mako')
    def view(self):
        """User viev."""
        name = self.request.matchdict['name']
        user = User.by_name(name=name)
        return {'user':user}

    @action(renderer='user/login.mako')
    def login(self):
        form = LoginForm(self.request.POST)
        session = self.request.session
        if self.request.method == 'POST' and form.validate():
            user = User.by_name(name=form.name.data)

            if user and user.check_password(form.password.data):
                usersession = {'name': user.name}
                session["user"] = usersession
                session.save()
                return HTTPFound(location = route_url('index', self.request))

        return {'form': form}


    @action(renderer='user/register.mako')
    def register(self):
    	"""Register view."""
        # Still need to handle existing name/email errors properly
        user = User(name=None, password='', email=None)
    	form = RegistrationForm(self.request.POST)
        if self.request.method == 'POST' and form.validate():
            user.name = form.name.data
            user.password = form.password.data
            user.email = form.email.data
            DBSession.add(user)
            return HTTPFound(location = route_url('user_view', self.request, name=user.name))

        return {'form':form}
