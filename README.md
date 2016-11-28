# simple-mock-server

Python mock server for testing

## Usage

### run server

```
python manage.py run
```

### put mock

```
method: PUT
url: /mock/add/
content-type: application/json

body: 
    {   
        "url":"test",
        "request": {
            "method":"POST",
            "content_type": "application/json",
            "data":{
                "foo":"bar"
            }
        },
        "response":{
            "status_code": 200,
            "content_type": "application/json",
            "data": {
                "ole": "ole"
            }
        }
    }
```

### get mock

```
method: POST
url: /test
content-type: application/json

body: 
    {
         "foo":"bar"
    }

answer: 
    {
        "ole": "ole"
    }

```

### reset mock

```
method: DELETE
url: /mock/reset/
content-type: *
```

Thank you so much :)