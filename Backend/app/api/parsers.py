from .restplus import api

pattern_request_parser = api.parser()
pattern_request_parser.add_argument('siteswap', type=str, required=True, help="For example - 531")
