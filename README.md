# Welcome to the 3D-Beacons Registry

## Background
3D-Beacons is an open collaboration between providers of macromolecular structure models. The goal of this collaboration is to provide model coordinates and meta-information from all the contributing data resources in a standardized data format and on a unified platform.

![Image](https://raw.githubusercontent.com/3D-Beacons/3d-beacons-documentation/main/assets/3d-beacons-summary.png)

Schematical overview of the 3D-Beacons infrastructure

3D-Beacons consists of a Registry, a Hub/Integrator and Beacons/Hosts. The Registry is used by the Hub to lookup which API endpoints are supported by the various Beacons/Hosts. The Beacons/Hosts provide data following the 3D-Beacons data specifications ([Current version: 0.3.1](https://app.swaggerhub.com/apis/3dbeacons/3D-Beacons/0.3.1))

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

## Contributors
- Mihaly Varadi [mvaradi](https://github.com/mvaradi)
- Sreenath Nair [sreenathnair](https://github.com/sreenathnair)
