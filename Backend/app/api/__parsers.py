from .__restplus import api

pattern_request_parser = api.parser()
pattern_request_parser.add_argument('siteswap', type=str, required=True, help="For example - 531")

transaction_request_parser = api.parser()
transaction_request_parser.add_argument('siteswap_1', type=str, required=True, help="For example - 444")
transaction_request_parser.add_argument('siteswap_2', type=str, required=True, help="For example - 651")
