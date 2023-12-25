import pytest

from jsonschema import validate, exceptions


class Assert:
    @staticmethod
    def validate_schema(instance: dict, schema: dict) -> None:
        try:
            # Check validity of JSON data using CATEGORY_SCHEMA schema
            validate(instance, schema)
            print("JSON-данные валидны по схеме.")
        except exceptions.ValidationError as e:
            pytest.fail(f"JSON-данные не соответствуют схеме: {e}")
