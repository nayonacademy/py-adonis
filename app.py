from adonis import AdonisAPI

app = AdonisAPI()


def home(request, response):
    response.text = "Welcome to Home page"


def about(request, response):
    response.text = "About Us pages"


def say_hello(request, response, person_name):
    response.text = f"hello {person_name}"