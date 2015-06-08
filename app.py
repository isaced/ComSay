from flask import Flask
from views.index import index

app = Flask(__name__)

app.register_blueprint(index)

if __name__ == '__main__':
    app.debug = True
    app.run()
