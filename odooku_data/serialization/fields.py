from odooku_data.serialization.base import BaseFieldSerializer


class FieldSerializer(BaseFieldSerializer):

    def serialize(self, record, context):
        return record.read([self.field_name])[0][self.field_name]

    def deserialize(self, values, context):
        value = values[self.field_name]
        if isinstance(value, str):
            value = value.encode('utf-8', 'replace').decode('utf-8')
        return value
