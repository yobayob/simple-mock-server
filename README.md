# simple-mock-server

Python mock server for testing.

### Deploy

```
virtualenv -p python 3.5 .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py run
```

## JSON

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

## XML

### put xml-mock

```
method: PUT
url: /mock/add/
content-type: application/json

{   
    "url":"test",
    "request": {
        "method":"POST",
        "content_type": "application/xml",
        "data":{
            "foo":"bar"
        }
    },
    "response":{
        "status_code": 200,
        "content_type": "application/xml",
        "data": {
			"answer": {
				"ole":"ole",
				"bar": 123
			}
		}
    }
}
```

### get mock

```
method: POST
url: /test
content-type: application/xml

body:
<foo>bar</foo>

answer:
<?xml version="1.0" encoding="UTF-8" ?>
<root>
     <answer type="dict">
         <bar type="int">123</bar>
         <ole type="str">ole</ole>
     </answer>
</root>
```

### reset mock

```
method: DELETE
url: /mock/reset/
content-type: *
```

Thank you so much :)