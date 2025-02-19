from cerberus import Validator
from flask import Request

def events_link_creator_validator(request: Request) -> None:
    body = request.json
    if not body:
        raise Exception('Invalid request body')

    validator = Validator({
        'data': {
            'type': 'dict',
            'schema': {
                'inscrito_id': {'type': 'integer', 'required': True},
                'evento_id': {'type': 'integer', 'required': True}
            }
        }
    })

    response = validator.validate(body)

    if not response:
        raise Exception(validator.errors)
