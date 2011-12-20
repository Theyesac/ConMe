"""Handlers package"""

def add_handlers(config):
    # Root Handler
    config.add_handler('index', '/',
                       '.root:RootHandler', action='index')
