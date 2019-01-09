# coding:utf-8
import json
import pytest

@pytest.fixture
def create_and_load_schema_as_json():
    def _create_and_load_schema_as_json(schema, payload):
        json_result = json.dumps(payload)
        result = schema().loads(json_result)
        return result

    return _create_and_load_schema_as_json
