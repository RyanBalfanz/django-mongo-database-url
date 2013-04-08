build:
	python setup.py sdist

clean:
	rm -rf ./dist
	rm -rf *.egg-info
	find . -name *.pyc -delete

register:
	python setup.py register

test:
	python test_dj_mongo_database_url.py

upload:
	python setup.py upload
