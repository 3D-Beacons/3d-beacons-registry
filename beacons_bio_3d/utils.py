import os
import json
import jsonschema
from jsonschema.exceptions import ValidationError


class DjangoUtils:
    """ This is the utils class for Django
    """

    def generate_fixture_json(input_registry_json, django_app="core"):
        registry = json.load(open(input_registry_json))
        model = []

        for provider in registry["providers"]:
            model.append(
                {
                    "model": f"{django_app}.Provider",
                    "pk": provider["providerId"],
                    "fields": {
                        "name": provider["providerName"],
                        "description": provider["providerDescription"],
                        "url": provider["providerUrl"],
                        "base_service_url": provider["baseServiceUrl"]
                    }
                }
            )

        for service in registry["services"]:
            model.append({
                "model": f"{django_app}.Service",
                "fields": {
                    "service_type": service["serviceType"],
                    "provider": service["provider"],
                    "access_point": service["accessPoint"]
                }
            })

        return model


class JSONUtils:
    """ This is the utils class for JSON
    """

    def validate_schema(schema_json, registry_json):
        """ Function to validate registry JSON against defined schema

        Args:
            schema_json (str): Path to schema JSON
            registry_json (str): Path to registry JSON

        Raises:
            FileNotFoundError: Raised when registry or schema JSON files are not present
        """
        if not os.path.exists(schema_json):
            raise FileNotFoundError("Schema JSON does not exists")

        if not os.path.exists(registry_json):
            raise FileNotFoundError("Registry JSON does not exists")

        schema = json.load(open(schema_json))
        instance = json.load(open(registry_json))

        try:
            jsonschema.validate(instance, schema=schema)
        except ValidationError as e:
            raise e

        # validate if provider field in services is valid
        dict_provider = dict()

        for provider in instance["providers"]:
            dict_provider[provider["providerId"]] = True

        unmatched_providers = []

        for service in instance["services"]:
            t_provider = service["provider"]
            if not dict_provider.get(t_provider):
                unmatched_providers.append(t_provider)

        if unmatched_providers:
            raise InvalidProviderException(unmatched_providers)

        print("Validation successful")
        return True


class InvalidProviderException(Exception):
    """ Exception raised when provider id in services sections are not present in providers list

    Attributes:
        providers -- List of invalid providers found
    """

    def __init__(self, providers):
        self.providers = providers
        super().__init__(f"Invalid providers: {self.providers}")
