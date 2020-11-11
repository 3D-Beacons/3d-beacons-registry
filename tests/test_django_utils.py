import os
import unittest
import json
from beacons_bio_3d.utils import JSONUtils, DjangoUtils, InvalidProviderException
from jsonschema import ValidationError

RES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')

class TestDjangoUtils(unittest.TestCase):

    def test_model_generate_valid_case(self):
        registry_json = f"{RES_PATH}/valid_full_registry.json"
        model_json = f"{RES_PATH}/valid_model.json"
        generated_model = DjangoUtils.generate_fixture_json(registry_json)
        valid_model = json.load(open(model_json))
        
        self.assertEqual(valid_model, generated_model)

