default: test

clean-pyc:
	@find . -iname '*.py[co]' -delete
	@find . -iname '__pycache__' -delete

clean-pytest:
	rm -rf .pytest_cache

clean-dist:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info

clean: clean-pyc clean-pytest clean-dist

analyze:
	pip install flake8
	# stop the build if there are Python syntax errors or undefined names
	flake8 --count --select=E9,F63,F7,F82 --show-source --statistics ./beacons_bio_3d
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=migrations ./beacons_bio_3d

test:
	pip install pytest-cov pytest-xdist
	pytest --cov-config=.coveragerc --cov-report=html --cov=beacons_bio_3d .

dist: clean
	python3 setup.py sdist
	python3 setup.py bdist_wheel

version: dist
	python3 setup.py --version

license: dist
	python3 setup.py --license