from flask import abort, render_template,jsonify, request
import json
from . import api

@api.route("/test")
def test():   
	mensaje = "OK"
	return json.dumps(mensaje)

