"""User handler"""
from pyramid_handlers import action

import base as base

from conme.models import DBSession, User
from conme.forms.user import RegistrationForm

class UserHandler(base.Handler):
    @action(renderer='user/view.mako')
    def view(self):
        """User viev."""
        id = self.request.matchdict['id']
        return {'id':id}

    @action(renderer='user/register.mako')
    def register(self):
    	"""Register view."""
        user = User(name=None, email=None)
    	form = RegistrationForm(self.request.POST)
        if self.request.method == 'POST' and form.validate():
            user.name = form.name.data
            user.password = form.password.data
            user.email = form.email.data
            DBSession.add(user)

    	return {'form':form}
