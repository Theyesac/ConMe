"""User handler"""
from pyramid_handlers import action

import base as base

class UserHandler(base.Handler):
    @action(renderer='user/view.mako')
    def view(self):
        """User viev."""
        id = self.request.matchdict['id']
        return {'id':id}
