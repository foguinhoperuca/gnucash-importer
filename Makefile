.PHONY: all clean test run generic build dist_test run_verbose test_verbose pytest pyfocus doc
# .SILENT: clean
FIXTURE_LEDGER=test/fixtures/test_ledger.gnucash
PLANTUML=/usr/local/plantuml/plantuml.jar
VERSION=$(shell cat gnucash_importer/version.py | tr -d __version__\ =\ \')

all: clean run

clean:
	clear
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name 'test_ledger.gnucash.*' -exec rm --force {} +
	find doc/ -name '*.png' -exec rm --force {} +
	rm -rf build
	rm -rf dist
	rm -rf gnucash_importer.egg-info
	git checkout $(FIXTURE_LEDGER)
	@echo "------------------- CLEANNED -------------------"
	@echo ""

clean_soft:
	clear
	find . -name 'test_ledger.gnucash.*' -exec rm --force {} +
	git checkout $(FIXTURE_LEDGER)
	@echo "------------------- CLEANNED SOFT-------------------"
	@echo ""

test: clean test_verbose

# TODO use gnu time
run:
	python3 gnucash_importer/__init__.py -gf $(FIXTURE_LEDGER) -a nubank -af test/fixtures/creditcard.ofx

run_verbose:
	python3 gnucash_importer/__init__.py -gf $(FIXTURE_LEDGER) -a nubank -af test/fixtures/creditcard.ofx -v

generic: clean
	python3 gnucash_importer/__init__.py -gf $(FIXTURE_LEDGER) -a generic -af test/fixtures/creditcard.ofx -acf "Liabilities:Credit Card:Nubank" -act "Imbalance-BRL:nubank"

build:
	python3 setup.py sdist bdist_wheel

build_pyinstaller: clean
	pyinstaller gnucash_importer/run_app.py -n gnucash_magical_importer --onefile

run_build: build
	dist/gnucash_importer-0.1.0-py3-none-any.whl

run_build_pyinstaller:
	@echo ""
	@echo "------------------- RUNNING -------------------"
	@echo ""
	dist/gnucash_magical_importer -gf $(FIXTURE_LEDGER) -a generic -af test/fixtures/creditcard.ofx -acf "Liabilities:Credit Card:Nubank" -act "Imbalance-BRL:nubank"

sdist:
	python3 setup.py sdist

dist_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

test_verbose: run_verbose
	git diff HEAD $(FIXTURE_LEDGER)
	$(MAKE) clean

pytest: clean
	python3 -m unittest test.test_ledger test.test_read_entry test.test_account

pyfocus: clean
	DEBUG_TEST=True python3 -m unittest test.test_account

doc: clean
	mkdir -p build/doc
	cp -r styles build/doc/
	pandoc todo.org --standalone -o build/doc/todo.html -f org -t html --css styles/github-pandoc.css --metadata pagetitle="TODO $(VERSION)"
	pandoc README.md --standalone -o build/doc/README.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="README $(VERSION)"
	pandoc CHANGELOG.md --standalone -o build/doc/CHANGELOG.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="CHANGELOG $(VERSION)"
	java -jar $(PLANTUML) doc/model.uml
