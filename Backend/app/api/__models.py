from flask_restplus import fields
from app.api.__restplus import api

import json


class ComplexClassField(fields.Raw):

    def format(self, value):
        jsonified_pattern = json.dumps(value, default=lambda o: o.__dict__,
                                       sort_keys=True, indent=4)
        return jsonified_pattern


pattern_model = api.model('Pattern', {
    'siteswap': fields.String(required=True),
    'beatmap': ComplexClassField(required=True),
    'highest_throw': fields.String(required=True),
    'problems': ComplexClassField(required=True)
})
