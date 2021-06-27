""" Module Docs
	by Using MappyRouter you will be used class based resource in flask
"""

import os

class MappyRouter():
    def register(self, api, routes, parent_route="/"):
        """ Registering new route to main path
			Input
				api Should be API that defined in flask run.py
				routes Array of route
				parent By default the path is /
        """
        for route in routes:
            path = os.path.join(parent_route, route['path'])
            if "children" in route:
                self.register(api, route['children'], parent_route=path)
            else:
                if "payload" in route:
                    api.add_resource(route['component'], path,
                    				endpoint=route['endpoint'],
                    				resource_class_kwargs=route['payload'])
                else:
                    api.add_resource(route['component'], path, endpoint=route['endpoint'])

    @classmethod
    def route(cls, path, component, endpoint, payload={}):
        """ Building Simple Route """
        return {
            "path" : path,
            "component" : component,
            "endpoint" : endpoint,
            "payload" : payload
        }
