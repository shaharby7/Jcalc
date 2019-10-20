from flask_restplus import Api
from Juggling import JugglingException

api = Api(version='1.0', title='Jcalc API',
          description='All Juggling calculations one needs')


@api.errorhandler
def default_error_handler(e):
    if isinstance(e, JugglingException):
        data = {"success": False,
                "message": "||".join(e.args),
                "problematic_beat": e.problematic_beat,
                "siteswap": e.siteswap}
        return data, 200

    data = {"message": "||".join(e.args),
            'trace_back': repr(e),
            "error_type": type(e).__name__}
    return data, 500
