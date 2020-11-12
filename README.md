# Welcome to the 3D-Beacons Registry

## Background
3D-Beacons is an open collaboration between providers of macromolecular structure models. The goal of this collaboration is to provide model coordinates and meta-information from all the contributing data resources in a standardized data format and on a unified platform.

![Image](https://raw.githubusercontent.com/3D-Beacons/3d-beacons-documentation/main/assets/3d-beacons-summary.png)

**Schematical overview of the 3D-Beacons infrastructure**

3D-Beacons consists of a Registry, a Hub and Beacons who host Clients. The Registry is used by the Hub to look up which API endpoints are supported by the various Beacons. The Beacons provide data according to the 3D-Beacons data specifications ([Current version: 0.3.1](https://app.swaggerhub.com/apis/3dbeacons/3D-Beacons/0.3.1)). The Hub collates the data from the Beacons and expose it via Hub API endpoints.

### Current 3D-Beacons
- [FoldX](http://foldxsuite.crg.eu/)
- [Genome3D](http://genome3d.eu/)
- [Protein Data Bank in Europe](https://pdbe.org)
- [Protein Data Bank in Europe - Knowledge Base](https://pdbe-kb.org)
- [Protein Ensemble Database](https://proteinensemble.org/)
- [SWISS-MODEL](https://swissmodel.expasy.org/)

## About the 3D-Beacons Registry
The 3D-Beacons Registry records meta-information about all the contributing partner resources, and lists the API endpoints that they support. In other words, looking at the registry will give specific information on which API endpoints provide what data from which data resource.

The Registry is implemented as a JSON object that complies with the schema specification, which is also included in this repository.

These are available in `resources` folder in the repository. To add or change a registry entry, make the relevant changes in `resources/registry.json` which should comply with schema defined in `resources/schema.json`.

There is also an installable Python package in this repository which provides utilities like schema validation. Please follow the installation section below for installing the Python package.

## Installation

### Prerequisites
Below are the list of softwares/tools for the utilities to properly run in the environment.


Python 3.7+

**Note**

Because [Python 2.7 supports ended January 1](https://pythonclock.org/), 2020, new projects should consider supporting Python 3 only, which is simpler than trying to support both. As a result, support for Python 2.7 in this project has been dropped.

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

The installed package can be used to validate `registry.json` against the defined schema. Both the files are available in `resources` folder.

```
(venv) $ beacons_bio_3d validate_schema --schema_json resources/schema.json --registry_json resources/registry.json
```

## Contributors
- Mihaly Varadi - _Initial work_ - [mvaradi](https://github.com/mvaradi)
- Sreenath Nair - _Initial work_ - [sreenathnair](https://github.com/sreenathnair)

See also the list of [contributors](https://github.com/3D-Beacons/3d-beacons-registry/contributors) who participated in this project.

### How to contribute
This repository is open to contributions. Please fork the repository and send pull requests.
