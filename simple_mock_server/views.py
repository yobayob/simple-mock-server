from app import app
from flask import request, Response, jsonify
import simplejson
from simple_mock_server.models import *


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


@app.route('/mock/reset/', methods=['DELETE'])
def reset():
    app.mock = []
    return jsonify({
        'answer': 'all clean'
    })


@app.route('/mock/add/', methods=['PUT'])
def receiver():
    MockObjects(**request.json)
    return jsonify({
        'answer': 'object added'
    })


@app.route('/', methods=['GET', 'POST', 'PUT'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT'])
def catch_all(path):
    req = Request(request)
    obj = MockObjects.get(path, req)
    if obj is not None:
        return Response(status=obj.response.status_code,
                        content_type=obj.response.content_type,
                        response=obj.response.data,
                        headers={'mock-path': path})


    return Response('Mock object is not found\n'
                    'URL: %s' % path, status=404)
