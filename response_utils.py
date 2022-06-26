from flask import Response, make_response, render_template
import json

def render_html_template(page, data=None):
	return make_response(render_template(page, data=data))

class ResponseUtil():
	status = ""

	def __init__(self, status, code):
		self.status = status
		self.code = code

	def json_message_response(self, message):
		return Response(json.dumps({
			"status": self.status,
			"code": self.code,
			"message": message
		}), mimetype="application/json")

	def json_data_response(self,name, data):
		return Response(json.dumps({
			"status": self.status,
			"code": self.code,
			name : data
		}), mimetype="application/json")

	def json_data(self, data):
		return Response(json.dumps({
			"data": data
		}), status = self.code, mimetype="application/json")


	def json_message(self, message):
		return Response(json.dumps({
			"message": message
		}), status = self.code, mimetype="application/json")

	
	