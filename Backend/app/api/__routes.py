from app.api.__restplus import api
from app.api.__models import pattern_model
from app.api.__parsers import pattern_request_parser

from flask_restplus import Resource
from Juggling.BasicJuggling import Pattern
from general_utils import read_config

ROUTES_CONFIG = read_config("routes_config")
ANALYZER_ROUTE = ROUTES_CONFIG["analyzer"]

juggling_namespace = api.namespace('juggling', description='All Juggling calculations')


@juggling_namespace.route(ANALYZER_ROUTE, methods=["POST"])
class PattenCollection(Resource):
    @api.doc(parser=pattern_request_parser)
    @api.marshal_with(pattern_model)
    def post(self):
        args = pattern_request_parser.parse_args()
        pattern = Pattern(args["siteswap"])
        return pattern
