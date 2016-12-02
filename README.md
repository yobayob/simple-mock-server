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

Request:
```
method: PUT
url: /mock/add/
content-type: application/json
```

Body:
```json
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

Request:
```
method: POST
url: /test
content-type: application/json
```

Body:
```json 
    {
         "foo":"bar"
    }
```

Answer: 
```json
    {
        "ole": "ole"
    }

```

### reset mock

Request:
```
method: DELETE
url: /mock/reset/
content-type: *
```

## XML

### put xml-mock

Request:
```
method: PUT
url: /mock/add/
content-type: application/json
```

Body:
```json
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

Request:
```
method: POST
url: /test
content-type: application/xml
```

Body:
```xml
<foo>bar</foo>
```

Answer:
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<root>
     <answer type="dict">
         <bar type="int">123</bar>
         <ole type="str">ole</ole>
     </answer>
</root>
```

### reset mock

Request:
```
method: DELETE
url: /mock/reset/
content-type: *
```

Thank you so much :)