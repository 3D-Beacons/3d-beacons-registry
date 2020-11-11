from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name = '3d-beacons-registry',
    version = version,
    license = license,
    author = 'Protein Data Bank in Europe',
    author_email = 'pdbehelp@ebi.ac.uk',
    url = 'https://github.com/3D-Beacons/3d-beacons-registry',
    description = 'Registry project for 3D Beacons and utilities',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        'six',
        'jsonschema'
    ],
    test_suite = 'tests',
    entry_points = {
	    'console_scripts': [
	        'beacons_bio_3d = beacons_bio_3d.__main__:main',
	    ]
	}
)