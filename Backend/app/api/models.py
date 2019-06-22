from flask_restplus import fields
from app.api.restplus import api

pattern_model = api.model('Pattern', {
    'highest_throw': fields.String(required=True, description='requested siteswap')
})
