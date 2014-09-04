import os

class NotFoundError(Exception):
	def __init__(self, message):
		self.value = message

class Route(object):
	def __init__(self, route_str):
		self.__route_list =  [uri for uri in route_str.split('/') if uri != '\n' and uri != '' ]
		if route_str == '/\n':
			self.__template = 'index.tpl'
		else:
			self.__template = '-'.join(self.__route_list) + '.tpl'
	def matches_uri(self, uri):
		uri_list  = [uri_element for uri_element in uri.split('/') if uri_element != '\n' and uri_element != '' ]

		if len(uri_list) != (len(self.__route_list)):
			return False
		for i in range(0, len(uri_list)):
			if self.__route_list[i][0] == '[':
				continue
			if self.__route_list[i] != uri_list[i]:
				return False
		return True

	@property
	def template(self):
		return self.__template

class Router(object):
	def __init__(self, route_strings):
		self.__routes = []
		route_strings = os.path.dirname(os.path.abspath(__file__)) + '/' + route_strings

		with open(route_strings, 'r') as routes_file:
			for route_str in routes_file:
				self.__routes.append(Route(route_str))

	def route_for_uri(self, uri):
			for route in self.__routes:
				if route.matches_uri(uri) == True:
					return route
			raise NotFoundError("Route wasn't found for given uri.")
# + ' | '.join(route.template for route in self.__routes)