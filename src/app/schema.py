from marshmallow import fields, Schema, validate, ValidationError
from marshmallow.validate import OneOf


class PayloadValidate(Schema):

    def basic_no_check(mobile):
        if "+" in mobile:
            raise ValidationError("Please remove + sign from phone no.")
        for n in mobile:
            if not n.isdigit():
                raise ValidationError("Please provide valid phone no.")

    id_number = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    gender = fields.Str(
        validate=[OneOf(['Female', 'Male', 'Transgender'])], required=True)
    # image_url = fields.Url(required=True, relative=True)
    mobile = fields.Str(
        validate=[validate.Length(min=10), validate.Length(max=10), basic_no_check], required=True)
