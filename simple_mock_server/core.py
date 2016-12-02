import simplejson


class Request(object):
    """
    Wrapper on request
    fix bug flask with nonexistent json
    """

    def __init__(self, request):
        self.request = request

    def get_json(self):
        try:
            return self.request.get_json()
        except:
            return None

    def __getattr__(self, item):
        return getattr(self.request, item)


class MockStorage(object):
    """
    Singleton for storage mock
    """

    storage = None
    mocks = list()

    def __new__(cls):
        if MockStorage.storage is None:
            MockStorage.storage = object.__new__(cls)
        return MockStorage.storage

    def register(self, **kwargs):
        mock = MockObject(**kwargs)
        self.mocks.append(mock)

    def unregister(self, mock):
        self.mocks.remove(mock)

    def get(self, path, req):
        for obj in reversed(self.mocks):
            if obj.url == path \
            and req.method == obj.request.method \
            and req.get_json() == obj.request.data \
            and obj.request.check_params(**req.args.to_dict()):
                return obj
        return None

    def reset_storage(self):
        self.mocks = []


class MockRequest(object):
    """
    Data for mock request
    params - GET params
    """

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


class MockObject(object):

    def __init__(self, url, request, response):
        self.url = url
        self.request = MockRequest(**request)
        self.response = MockResponse(**response)

    def __repr__(self):
        return 'Mock object for %s' % self.url