from flask_restplus import Api

api = Api(version='1.0', title='Jcalc API',
          description='All Juggling calculations one needs')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    return {'message': message}, 500
