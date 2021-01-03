from api import API

app = API()


def home(request, response):
    response.text = "Welcome to Home page"


def about(request, response):
    response.text = "About Us pages"


def say_hello(request, response, person_name):
    resp.text = f"hello {person_name}"