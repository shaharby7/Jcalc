from app.api.restplus import api
from app.api.models import pattern_model
from app.api.parsers import pattern_request_parser

from flask_restplus import Resource
from Juggling.BasicJuggling import Pattern

juggling_namespace = api.namespace('juggling', description='All Juggling calculations')


@juggling_namespace.route("/debugger", methods=["POST"])
class PattenCollection(Resource):
    @api.doc(parser=pattern_request_parser)
    @api.marshal_with(pattern_model)
    def post(self):
        args = pattern_request_parser.parse_args()
        pattern = Pattern(args["siteswap"])
        return pattern
