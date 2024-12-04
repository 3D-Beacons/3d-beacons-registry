# Welcome to the 3D-Beacons Registry

## Publication
**3D-Beacons: Decreasing the gap between protein sequences and structures through a federated network of protein structure data resources**<br> 
[Mihaly Varadi](https://github.com/mvaradi), [Sreenath Nair](https://github.com/sreenathnair), [Ian Sillitoe](https://github.com/orgs/3D-Beacons/people/sillitoe), [Gerardo Tauriello](https://github.com/orgs/3D-Beacons/people/gtauriello), Stephen Anyango, [Stefan Bienert](https://github.com/orgs/3D-Beacons/people/bienchen), Clemente Borges, Mandar Deshpande, Tim Green, Demis Hassabis, Andras Hatos, Tamas Hegedus, Maarten L Hekkelman, Robbie Joosten, John Jumper, Agata Laydon, Dmitry Molodenskiy, Damiano Piovesan, Edoardo Salladini, Steven L. Salzberg, Markus J Sommer, Martin Steinegger, Erzsebet Suhajda, Dmitri Svergun, Luiggi Tenorio-Ku, Silvio Tosatto, Kathryn Tunyasuvunakool, [Andrew Mark Waterhouse](https://github.com/orgs/3D-Beacons/people/awaterho), Augustin Žídek, Torsten Schwede, Christine Orengo, Sameer Velankar<br>
3 August 2022; BioRxiv https://doi.org/10.1101/2022.08.01.501973

## Background

3D-Beacons is an open collaboration between providers of macromolecular structure models. The goal of this collaboration
is to provide model coordinates and meta-information from all the contributing data resources in a standardized data
format and on a unified platform.

![Image](https://www.ebi.ac.uk/pdbe/pdbe-kb/3dbeacons/assets/img/overview.png)

**Schematical overview of the 3D-Beacons infrastructure**

3D-Beacons consists of a Registry, a Hub and Beacons who host Clients. The Registry is used by
the [3D-Beacons Hub](https://github.com/3D-Beacons/3d-beacons-hub-api) to look up which API endpoints are supported by
the various Beacons. The Beacons provide data according to the 3D-Beacons data
specifications ([GitHub link](https://github.com/3D-Beacons/3d-beacons-specifications/blob/production/oas3.yaml)). The Hub collates
the data from the Beacons and expose it via Hub API endpoints.

### Current 3D-Beacons

- [AlphaFold](https://alphafold.ebi.ac.uk)
- [AlphaFill](https://alphafill.eu/)
- [BFVD](https://bfvd.foldseek.com/)
- [Genome3D](http://genome3d.eu/)
- [isoform.io](https://www.isoform.io/)
- [Protein Data Bank in Europe](https://pdbe.org)
- [Protein Data Bank in Europe - Knowledge Base](https://pdbe-kb.org)
- [Protein Ensemble Database](https://proteinensemble.org/)
- [SWISS-MODEL](https://swissmodel.expasy.org/)

## About the 3D-Beacons Registry

The 3D-Beacons Registry records meta-information about all the contributing partner resources, and lists the API
endpoints that they support. In other words, looking at the registry will give specific information on which API
endpoints provide what data from which data resource.

The Registry is implemented as a JSON object that complies with the schema specification, which is also included in this
repository.

These are available in `resources` folder in the repository. To add or change a registry entry, make the relevant
changes in `resources/registry.json` which should comply with schema defined in `resources/schema.json`.

There is also an installable Python package in this repository which provides utilities like schema validation. Please
follow the installation section below for installing the Python package.

## Linking a new data resource to 3D-Beacons Network

Data providers who are interested in making their macromolecule structures available through the 3D-Beacons Network
should follow the following steps:

1. Contact the 3D-Beacons consortium
2. Review the [API specifications](https://github.com/3D-Beacons/3d-beacons-specifications/blob/production/oas3.yaml) for sharing metadata
3. Implement API endpoints or set up an instance of
   the [3D-Beacons Client](https://github.com/3D-Beacons/3d-beacons-client)
4. Review the `resources/registry.json` file in this repository
5. Update the `resources/registry.json` file to include information on your data resource and your API endpoint URLs
6. Create a pull request for the `development` branch with your updated `resources/registry.json` file

### 1. Contact the 3D-Beacons consortium

3D-Beacons is an open consortium, and we welcome new data providers who would like to make their experimentally
determined or theoretical macromolecule structures available through the 3D-Beacons Network.

To ensure that the network provides access to relevant data, we require new prospective data providers to contact us
before linking their data to 3D-Beacons. Please send an email to Sameer Velankar (sameer@ebi.ac.uk) or Christine
Orengo (c.orengo@ucl.ac.uk) to initiate discussions.

### 2. Review the [API specifications](https://github.com/3D-Beacons/3d-beacons-specifications/blob/production/oas3.yaml) for sharing metadata

The 3D-Beacons Network provides access to metadata regarding macromolecule structures in a unified format. This means
that every data provider has to expose information in the same data format. We define the accepted data schemas in the
[3D-Beacons API specification](https://github.com/3D-Beacons/3d-beacons-specifications/blob/production/oas3.yaml) on GitHub.

Please review this specification, and identify the schemas that fit the data you would like to make accessible via
3D-Beacons. For example, if you want to make your structures discoverable based on a UniProt identifier, then the
endpoints with `/uniprot/{qualifier}.json` are relevant for you.

### 3. Implement API endpoints or set up an instance of the [3D-Beacons Client](https://github.com/3D-Beacons/3d-beacons-client)

After reviewing the API specifications and deciding what data you will make available, and which data schema you will
use, the next step is to either implement the selected API endpoints in a REST API, or to take advantage of
the [3D-Beacons Client](https://github.com/3D-Beacons/3d-beacons-client), which can be installed locally and includes a
pre-packaged and ready-to-use implementation of certain API endpoints. For more information on this, please visit the [3D-Beacons Client](https://github.com/3D-Beacons/3d-beacons-client) repository.

### 4. Review the `resources/registry.json` file in this repository

Once your metadata is exposed via API endpoints that comply with the [3D-Beacons API specification](https://github.com/3D-Beacons/3d-beacons-specifications/blob/production/oas3.yaml), you should review the `resources/registry.json` file in this repository. This file contains all the information needed by the [3D-Beacons Hub API](https://github.com/3D-Beacons/3d-beacons-hub-api) for linking your API endpoints to the 3D-Beacons Network.

The registry has two main data blocks: 1.) `providers` and 2.) `services`.

The `providers` contains information that describes your data resource. We use this information to let users know where to look for the original sources of data.

An example item in the `providers` list would look like this:

```
{
   "providerId": "alphafold",
   "providerName": "AlphaFold Protein Structure Database",
   "providerDescription": "AlphaFold is an AI system developed by DeepMind that predicts a protein’s 3D structure from its amino acid sequence. It regularly achieves accuracy competitive with experiment.",
   "providerUrl": "https://alphafold.ebi.ac.uk/",
   "baseServiceUrl": "https://alphafold.ebi.ac.uk/api/",
   "devBaseServiceUrl": "https://dev.alphafold.ebi.ac.uk/api/",
   "providerLogo": "https://alphafold.ebi.ac.uk/assets/img/dm-logo.png"
}
```

The `services` contains information about what API endpoints are implemented by which data provider.

An example item in the `services` list would look like this:

```
{
   "serviceType": "summary",
   "provider": "alphafold",
   "accessPoint": "uniprot/summary/"
},
```

Together, the `providers` and `services` data blocks tell the 3D-Beacons Hub API that in the example above, AlphaFold DB provides access to their data by implementing the `summary` API endpoint, which they serve on the URL `https://alphafold.ebi.ac.uk/api/uniprot/summary/`

### 5. Update the `resources/registry.json` file

The next step is to fork this repository (
i.e. [https://github.com/3D-Beacons/3d-beacons-registry](https://github.com/3D-Beacons/3d-beacons-registry)) and edit
the `resources/registry.json` file by adding a new item in the `providers` list and listing all the API endpoints you implemented in the `services` list. 

**NOTE**: If you don't have a production setup at this point, set same value for `baseServiceUrl` as `devBaseServiceUrl`.

### 6. Create a pull request for the `development` branch

Finally, please create a pull request so that we can merge your version of the `resources/registry.json` file to our `development` branch. We will then test the updated file, and also test all the API endpoints you specified in the `services` list of the `resources/registry.json` file.

As part of testing the API endpoints, we will perform stress testing of all the API endpoints you provide. We will also validate the data format against the [3D-Beacons API specification](https://github.com/3D-Beacons/3d-beacons-specifications/blob/production/oas3.yaml), and test if the [3D-Beacons Hub API](https://github.com/3D-Beacons/3d-beacons-hub-api) can concatenate data.

Once done, we proceed to merge the updates into the `master` branch, at which point your data resource will become officially linked to the 3D-Beacons Network.

## Installation

### Prerequisites

Below are the list of softwares/tools for the utilities to properly run in the environment.

Python 3.7+

**Note**

Because [Python 2.7 supports ended January 1](https://pythonclock.org/), 2020, new projects should consider supporting
Python 3 only, which is simpler than trying to support both. As a result, support for Python 2.7 in this project has
been dropped.

### Setup the environment

Setup a Python virtual environment and install required packages.

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Now install the project dependencies.

```
(venv) $ make dev_deps
```

Install the package

```
(venv) $ pip install .
```

## Usage

The installed package can be used to validate `registry.json` against the defined schema. Both the files are available
in `resources` folder.

```
(venv) $ beacons_bio_3d validate_schema --schema_json resources/schema.json --registry_json resources/registry.json
```

## Contributors

- Sreenath Nair - _Initial work_ - [sreenathnair](https://github.com/sreenathnair)
- Mihaly Varadi - _Initial work_ - [mvaradi](https://github.com/mvaradi)

See also the list of [contributors](https://github.com/3D-Beacons/3d-beacons-registry/contributors) who participated in
this project.

### How to contribute

This repository is open to contributions. Please fork the repository and send pull requests.
