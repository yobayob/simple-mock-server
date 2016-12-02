from app import app
from flask import request, Response, jsonify
from simple_mock_server.core import *


@app.route('/mock/reset/', methods=['DELETE'])
def reset():
    MockStorage().reset_storage()
    return jsonify({
        'answer': 'all clean'
    })


@app.route('/mock/add/', methods=['PUT'])
def receiver():
    MockStorage().register(**request.json)
    return jsonify({
        'answer': 'object added'
    })


@app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH'])
def catch_all(path):
    req = Request(request)
    obj = MockStorage().get(path, req)
    if obj is not None:
        MockStorage().unregister(obj)
        return Response(status=obj.response.status_code,
                        content_type=obj.response.content_type,
                        response=obj.response.data,
                        headers={'mock-path': path})


    return Response('Mock object is not found\n'
                    'URL: %s' % path, status=404)
