"""Handlers package"""

def add_handlers(config):
	# Root Handler
	config.add_handler('index', '/',
					   '.root:RootHandler', action='index')
	config.add_handler('user_login', '/user/login',
					   '.user:UserHandler', action='login')
	config.add_handler('user_register', '/user/register',
					   '.user:UserHandler', action='register')
	config.add_handler('user_view', '/user/{name}',
					   '.user:UserHandler', action='view')
