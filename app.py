from flask import Flask, request
from db import stores, items
from flask_smorest import Api #This is to add better error handling

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
import uuid

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

