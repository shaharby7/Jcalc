from flask_restplus import Api
from Juggling import JugglingException

api = Api(version='1.0', title='Jcalc API',
          description='All Juggling calculations one needs')


@api.errorhandler
def default_error_handler(e):
    json = {"message": "||".join(e.args), 'trace_back': repr(e), "error_type": type(e).__name__}
    if isinstance(e, JugglingException):
        json.update({"problematic_beat": e.problematic_beat})
    return json, 500
