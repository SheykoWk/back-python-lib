# def app (environ. start_response):
#     response_body = b"Hello World"
#     status = "200 ok"
#     start_response(status, headers=[])
#     return iter([response_body])

from api import API
app = API(templates_dir="templates")

def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)


app.add_exception_handler(custom_exception_handler)

@app.route("/home")
def home(request, response):
    response.text = "Hello from home"

@app.route("/about")
def about(request, response):
    response.text = "Hello from about"

@app.route("/hello/{name}")
def say_hello(request, response, name):
    response.text = f"Hello {name}"


@app.route("/sum/{num1}/{num2}")
def sum(request, response, num1, num2):
    total = int(num1) + int(num2)
    response.text = f"{num1} + {num2} = {total}"

@app.route("/book")
class BookResource:
    def get(self, req, res):
        res.text = "Books Page"
    
    def post(self, req, res):
        res.text = "Create books"

def handler(rea, res):
    res.text = "testing handler"

@app.route("/template")
def template_handler(req,res):
    res.body = app.template(
        "index.html", context={"name" : "Sh3ywork", "title": "My personal framework", "author": "sh3yk0"}
    ).encode()

