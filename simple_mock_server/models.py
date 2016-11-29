from app import app
import simplejson


class MockRequest(object):

    def __init__(self, method='GET', content_type='application/json',
                 params=None, data=None):
        self.params = {}
        if params:
            self.params = params
        self.method = method
        self.data = data
        self.content_type = content_type

    def check_params(self, **params):
        """
        checking GET-params
        # TODO: fix bug with list get-params
        """
        if self.params and not all([str(v) == params.get(k)
                                    for k, v in self.params.items()]):
            return False
        return True


class MockResponse(object):

    def __init__(self, data='OK', status_code=200,
                 content_type='application/json'):
        self.content_type = content_type
        self.data = self._parse_data(data)
        self.status_code = status_code

    def _parse_data(self, data):
        if 'json' in self.content_type:
            data = simplejson.dumps(data)
        elif isinstance(data, (dict, list)):
            data = repr(data)
        return data


class MockObjects(object):

    def __init__(self, url, request, response):
        self.url = url
        self.request = MockRequest(**request)
        self.response = MockResponse(**response)
        app.mock.append(self)

    @staticmethod
    def get(path, req):
        for obj in reversed(app.mock):
            if obj.url == path \
            and req.method == obj.request.method \
            and req.get_json() == obj.request.data \
            and obj.request.check_params(**req.args.to_dict()):
                return obj
        return None

    def __repr__(self):
        return 'Mock object for %s' % self.url