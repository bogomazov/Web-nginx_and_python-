import sys
sys.path.append('/home/dev/www/website')

from router.router import *
from jinja2 import Environment, PackageLoader

ROUTER = Router("routes.conf")
TEMPLATE_ENV = Environment(loader=PackageLoader(__name__, 'templates'))

class Response:
	status = ''
	body = ''

def application(env, start_response):
	headers = []
	try:
		process_request(env)
	except Exception as e:
		process_exception(e)

	headers.append(('Content-Type','text/html'))
	headers.append(('Content-Length', str(len(Response.body))))
	start_response(Response.status, headers)
	return [Response.body]

def process_request(env):
	try:
		route = ROUTER.route_for_uri(env['PATH_INFO'])
	except NotFoundError:
		raise

	template = TEMPLATE_ENV.get_template(route.template)
	NAVIGATION = [ "news", "category", "articles" ]
	template_vars = { 
					 "user_name" : "bogomazz",
	                 "text" : "A simple inquiry of function.",
	                 "navigation" : NAVIGATION
	               }

	
	Response.status = '200 OK'
	Response.body = template.render(template_vars).encode('utf-8')

def process_exception(exception):
	if isinstance(exception, NotFoundError):
		Response.status = 'HTTP/1.1 404 Not Found'
		Response.body = "404 Page not found."




