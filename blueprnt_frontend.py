import flask

bprnt_frontend = flask.Blueprint(__name__,"bprnt_frontend")


@bprnt_frontend.route("/about")
def about():
    return flask.render_template("about.html")

@bprnt_frontend.route("/contact")
def contact():
    return flask.render_template("contact.html")

@bprnt_frontend.route("/enroll")
def enroll():
    return flask.render_template("enroll.html")

@bprnt_frontend.route("/")
def index():
    return flask.render_template("index.html")



