import os
import unittest
import json

from six import assertRaisesRegex
from beacons_bio_3d.utils import JSONUtils, DjangoUtils, InvalidProviderException
from jsonschema import ValidationError

RES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')

class TestJSONUtils(unittest.TestCase):

    def test_schema_validator_valid_case(self):
        assert(JSONUtils.validate_schema(f"{RES_PATH}/valid_schema.json", f"{RES_PATH}/valid_registry.json"))

    def test_schema_validator_invalid_case(self):
        self.assertRaises(ValidationError, JSONUtils.validate_schema, f"{RES_PATH}/valid_schema.json", f"{RES_PATH}/invalid_registry.json")

    def test_schema_file_not_found_case(self):
        self.assertRaises(FileNotFoundError, JSONUtils.validate_schema, f"{RES_PATH}/no_schema_file", f"{RES_PATH}/valid_registry.json")

    def test_registry_file_not_found_case(self):
        self.assertRaises(FileNotFoundError, JSONUtils.validate_schema, f"{RES_PATH}/valid_schema.json", f"{RES_PATH}/no_registry_file")

    def test_invalid_providers_case(self):
        self.assertRaises(InvalidProviderException, JSONUtils.validate_schema, f"{RES_PATH}/valid_schema.json", f"{RES_PATH}/invalid_providers_registry.json")


class TestDjangoUtils(unittest.TestCase):

    def test_model_generate_valid_case(self):
        registry_json = f"{RES_PATH}/valid_full_registry.json"
        model_json = f"{RES_PATH}/valid_model.json"

        generated_model = DjangoUtils.generate_fixture_json(registry_json)
