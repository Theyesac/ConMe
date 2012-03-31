"""Root handler"""
from pyramid_handlers import action

import base as base

class RootHandler(base.Handler):
    @action(renderer='index.mako')
    def index(self):
        """Index viev."""
        return {'session': self.request.session}
