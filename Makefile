FIXTURE_LEDGER=test/fixtures/test_ledger.gnucash

all: clean run

clean:
	clear
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name 'test_ledger.gnucash.*' -exec rm --force {} +
	git checkout $(FIXTURE_LEDGER)

test: clean test_verbose

# TODO use gnu time
run:
	python3 gnucash_importer/__init__.py -gf $(FIXTURE_LEDGER) -a nubank -af test/fixtures/creditcard.ofx

build:
	python3 setup.py sdist bdist_wheel

dist_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

run_verbose:
	python3 gnucash_importer/__init__.py -gf $(FIXTURE_LEDGER) -a nubank -af test/fixtures/creditcard.ofx -v

test_verbose: run_verbose
	git diff HEAD $(FIXTURE_LEDGER)

pytest: clean
	python3 -m unittest test.test_ledger test.test_read_entry test.test_account

pyfocus: clean
	DEBUG_TEST=True python3 -m unittest test.test_account
