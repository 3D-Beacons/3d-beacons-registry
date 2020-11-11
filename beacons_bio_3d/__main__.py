#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import json
import argparse
from beacons_bio_3d.utils import JSONUtils, DjangoUtils

__doc__ = """
3D Beacons

Registry schema validation and utilities.
"""

RES_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
DEFAULT_SCHEMA_JSON = f"{RES_PATH}/schema.json"
DEFAULT_REGISTRY_JSON = f"{RES_PATH}/registry.json"


def main():
    """ This is the application entry point
    """

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    sub_parsers = parser.add_subparsers(dest='subparser_name', help="Available sub-commands")

    # parser for validation functions
    validate_parser = sub_parsers.add_parser("validate_schema", help="Validates the registry JSON with the defined schema.")
    validate_parser.add_argument("--schema_json", help="Path to the schema JSON", required=True)
    validate_parser.add_argument("--registry_json", help="Path to the registry JSON", required=True)

    # parser for model generation functions
    model_gen_parser = sub_parsers.add_parser("model_generate", help="Generates model JSON from registry JSON.")
    model_gen_parser.add_argument("--registry_json", help="Path to registry JSON to be converted", required=True)
    model_gen_parser.add_argument("--model_json", help="Path to output model JSON", required=True)
    model_gen_parser.add_argument(
        "--django_app",
        help="The name of Django app, this will be used to define package for model",
        default="core")

    args = parser.parse_args()

    if args.subparser_name == "validate_schema":
        JSONUtils.validate_schema(args.schema_json, args.registry_json)
    elif args.subparser_name == "model_generate":
        if JSONUtils.validate_schema(DEFAULT_SCHEMA_JSON, args.registry_json):
            # generate model json
            gen_model = DjangoUtils.generate_fixture_json(args.registry_json, django_app=args.django_app)
            with open(args.model_json, "w") as model_json_handle:
                json.dump(gen_model, model_json_handle)

        print(f"Model JSON generated to {args.model_json}")


if __name__ == "__main__":
    main()
