import flask
from blueprnt_frontend import bprnt_frontend

app = flask.Flask("kuazone")

#register blueprints
app.register_blueprint(bprnt_frontend)



if __name__ == "__main__":
    app.run()
