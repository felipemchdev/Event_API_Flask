from cerberus import Validator


def events_creator_validator(resquest:any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {"type": "string", "required": True , "empty": False}   
            }
        }
    })

    response = body_validator.validate(resquest.json)
    
    if response is False:
        print(body_validator.errors)