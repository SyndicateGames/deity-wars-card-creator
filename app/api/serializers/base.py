import marshmallow
from marshmallow import Schema
from marshmallow.fields import Marshaller

from app.utils.exceptions import HTTPError


def handle_error(schema, error, obj):
    msg = ''
    for field, error in error.iteritems():
        msg += '{field} - {error}\n'.format(
            field=field,
            error=','.join(error)
        )
    raise HTTPError(400, msg)


class BaseSchema(Schema):
    """Base class for serializers.

    Main purposes:
    1. Validation of the resource
    2. Conversion lowercase_with_underscores <> camelCase
    """
    __error_handler__ = handle_error

    def serialize(self, items, many=True):
        """Serialize a list of resources."""
        return self.dump(items, many).data


class BaseMarshaller(Marshaller):
    """Extends the marshmallow.fields.Marshaller.

    Include `skip_missing=True` as default for serialization.
    """
    def serialize(self, *args, **kwargs):
        kwargs['skip_missing'] = True
        return super(BaseMarshaller, self).serialize(*args, **kwargs)

marshmallow.fields.Marshaller = BaseMarshaller
