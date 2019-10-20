from app.api.__restplus import api
from app.api.__models import pattern_model
from app.api.__parsers import pattern_request_parser, transaction_request_parser

from flask_restplus import Resource
from Juggling import *
from general_utils import read_config

ROUTES_CONFIG = read_config("routes_config")
ANALYZER_ROUTE = ROUTES_CONFIG["analyzer"]
SUGGEST_VALID_PATTERN_ROUTE = ROUTES_CONFIG["suggest_valid_pattern"]
TRANSACTIONS_ROUTE = ROUTES_CONFIG["transactions"]

juggling_namespace = api.namespace('juggling', description='All Juggling calculations')


@juggling_namespace.route(ANALYZER_ROUTE, methods=["POST"])
class PattenCollection(Resource):
    @api.doc(parser=pattern_request_parser)
    @api.marshal_with(pattern_model)
    def post(self):
        args = pattern_request_parser.parse_args()
        pattern = Pattern(args["siteswap"])
        return pattern


@juggling_namespace.route(SUGGEST_VALID_PATTERN_ROUTE, methods=["POST"])
class SuggestionsCollection(Resource):
    @api.doc(parser=pattern_request_parser)
    @api.marshal_with(pattern_model)
    def post(self):
        args = pattern_request_parser.parse_args()
        pattern = Pattern(args["siteswap"])
        fixed_pattern = suggest_valid_pattern(pattern)
        return fixed_pattern


@juggling_namespace.route(TRANSACTIONS_ROUTE, methods=["POST"])
class SuggestionsCollection(Resource):
    @api.doc(parser=transaction_request_parser)
    @api.marshal_with(pattern_model)
    def post(self):
        args = transaction_request_parser.parse_args()
        pattern1, pattern2 = SuggestionsCollection.create_patterns_for_transactions(args)
        transaction = crate_transaction_pattern(pattern1, pattern2)
        return transaction

    @staticmethod
    def create_patterns_for_transactions(args):
        results = []
        for siteswap in args.values():
            try:
                results.append(Pattern(siteswap))
            except JugglingException as e:
                e.set_siteswap(siteswap)
                raise e
        return results
