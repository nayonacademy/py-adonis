# Build Simple Python web server with uwsgi

## Web server
How the webserver work. Just imagine how our own python framework webserver will work

![web server](images/web-server.svg "web server")

photo credit : [mozila](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)

The complete official document of uwsgi is here [Python/WSGI applications](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)     

```
pip install uwsgi
```

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