# Build Simple Python server with uwsgi

The complete official document of uwsgi is here [Python/WSGI applications](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)     

```pip install uwsgi```

First write a wsgi application. we can start with hello world

```python
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
```
save it as adonis.py
It a single Python function and a "application" is a function name that is default of uwsgi Python loader

Deploy it on HTTP port 8080

```
uwsgi --http :8080 --wsgi-file adonis.py
```