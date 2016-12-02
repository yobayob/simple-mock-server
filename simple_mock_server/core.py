import simplejson
from xml.etree.ElementTree import ElementTree
import xmltodict
import dicttoxml


class Request(object):
    """
    Wrapper on request
    fix bug flask with nonexistent json
    """

    def __init__(self, request):
        self.method = request.method
        self.content_type = request.content_type
        self.path = request.path
        self.request = request
        self.params = request.args
        self.data = self._parse_data()

    def get_json(self):
        try:
            return self.request.get_json()
        except:
            return None

    def get_xml(self):
        try:
            data = xmltodict.parse(self.request.data, process_namespaces=True)
            return dict(data)
        except:
            return None

    def _parse_data(self):
        data = None
        if 'json' in self.content_type:
            data = self.get_json()
        elif 'xml' in self.content_type:
            data = self.get_xml()
        elif self.request.data == b'':
            data = None
        elif self.request.data:
            data = self.request.data
        return data

    def __getattr__(self, item):
        return getattr(self.request, item)

    def as_dict(self):
        return {
            'url': self.path,
            'method': self.method,
            'params': self.params,
            'content_type': self.content_type,
            'data': self.data
        }


class WrongRequestStorage(object):
    storage = None
    requests = list()

    def __new__(cls):
        if WrongRequestStorage.storage is None:
            WrongRequestStorage.storage = object.__new__(cls)
        return WrongRequestStorage.storage

    def register(self, req):
        self.requests.append(req)

    def reset_storage(self):
        self.requests = []


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

    def get(self, req):
        for obj in reversed(self.mocks):
            if (obj.url==req.path):
                if(req.data != obj.request.data):
                    print(req.content_type)
                    print(req.data)
                    print(obj.request.data)
            if obj.url == req.path \
            and req.method == obj.request.method \
            and req.content_type == obj.request.content_type \
            and req.data == obj.request.data \
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

    def as_dict(self):
        return {
            'params': self.params,
            'method': self.method,
            'data': self.data,
            'content_type': self.content_type
        }


class MockResponse(object):

    def __init__(self, data=None, status_code=200,
                 content_type='application/json'):
        self.content_type = content_type
        self.data = self._parse_data(data)
        self.status_code = status_code

    def _parse_data(self, data):
        if data:
            if 'json' in self.content_type:
                data = simplejson.dumps(data)
            if 'xml' in self.content_type:
                data = dicttoxml.dicttoxml(data)
            elif isinstance(data, (dict, list)):
                data = repr(data)
        return data

    def as_dict(self):
        return {
            'status_code': self.status_code,
            'data': self.data,
            'content_type': self.content_type
        }


class MockObject(object):

    def __init__(self, url, request, response):
        self.url = url
        self.request = MockRequest(**request)
        self.response = MockResponse(**response)

    def as_dict(self):
        return {
            'url': self.url,
            'request': self.request.as_dict(),
            'response': self.response.as_dict()
        }
