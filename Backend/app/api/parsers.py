from flask_restplus import reqparse

pattern_arguments = reqparse.RequestParser()
pattern_arguments.add_argument('siteswap', type=str, required=True)
