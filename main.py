from bottle import route, run, template, request, redirect, Bottle
from controllers.user_controller import UserController
from controllers.movie_controller import MovieController
from bottle import static_file


app = Bottle()
movie_controller = MovieController()
user_controller = UserController()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@app.route('/')
def index():
    return template('index') 

movie_controller.setup_routes(app)

user_controller.setup_routes(app)

@app.route("/logon", method="post")
def checking_logon():
    if user_controller.validating_user():
        return redirect("/")
    return template("logon")


run(host='localhost', port=8080, debug=True, reloader=True, app=app)
