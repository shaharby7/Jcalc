from app.api.restplus import api
from app.api.models import pattern_model
from app.api.parsers import pattern_arguments

from flask_restplus import Resource, marshal
from flask_cors import cross_origin
from flask import request, make_response
import json

from Juggling.BasicJuggling import Pattern

juggling_namespace = api.namespace('juggling', description='All Juggling calculations')


# @juggling_namespace.route("/pattern", methods=["GET"])
# class PattenCollection(Resource):
#
#     # @cross_origin()
#     # @api.marshal_with(pattern_model)
#     def get(self):
#         siteswap = request.headers.get("siteswap")
#         pattern = Pattern(siteswap)
#         jsonified_pattern = json.dumps(pattern, default=lambda o: o.__dict__,
#                                        sort_keys=True, indent=4)
#         jsonified_pattern = {"highest_throw": 1}
#         jsonified_pattern = marshal(jsonified_pattern, pattern_model)
#         return make_response(json.dumps(jsonified_pattern), 200)

@juggling_namespace.route("/pattern", methods=["GET"])
class PattenCollection(Resource):

    @api.expect(pattern_arguments, validate=True)
    @api.marshal_with(pattern_model)
    def get(self):
        siteswap = request.headers.get("siteswap")
        pattern = Pattern(siteswap)
        return pattern.__dict__
