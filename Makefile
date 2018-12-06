.PHONY: all clean clean_soft run run_verbose run_generic run_cxfreeze build_bdist_wheel build_cxfreeze sdist dist_test unittest unittest_debug doc
# .SILENT: clean
FIXTURE_LEDGER=test/fixtures/test_ledger.gnucash
FIXTURE_CREDITCARD=test/fixtures/creditcard.ofx
PLANTUML=/usr/local/plantuml/plantuml.jar
VERSION=$(shell cat gnucash_importer/version.py | tr -d __version__\ =\ \')
BINARY_NAME=gnucash_magical_importer # A **magical** name!! ;)
BIN=dist/$(BINARY_NAME)
APP_RUN_SCRIPT=gnucash_importer/run_app.py
APP_PARAMS= -gf $(FIXTURE_LEDGER) -a nubank -af $(FIXTURE_CREDITCARD)
APP_PARAMS_GENERIC= -gf $(FIXTURE_LEDGER) -a generic -af $(FIXTURE_CREDITCARD) -acf "Liabilities:Credit Card:Nubank" -act "Imbalance-BRL:nubank"

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

# TODO use gnu time
run: clean
	python3 $(APP_RUN_SCRIPT) $(APP_PARAMS)

run_verbose: clean
	python3 $(APP_RUN_SCRIPT) $(APP_PARAMS) -v
	git diff HEAD $(FIXTURE_LEDGER)
	$(MAKE) clean

run_generic: clean
	python3 $(APP_RUN_SCRIPT) $(APP_PARAMS_GENERIC)

run_cxfreeze: build_cxfreeze
	@echo ""
	@echo "------------------- RUNNING -------------------"
	@echo ""
	$(BIN) $(APP_PARAMS)
	git diff HEAD $(FIXTURE_LEDGER)

build_bdist_wheel:
	python3 setup.py sdist bdist_wheel

build_cxfreeze: clean
	cxfreeze gnucash_importer/run_app.py --target-dir dist --target-name $(BINARY_NAME)

sdist:
	python3 setup.py sdist

dist_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

unittest: clean
	python3 -m unittest test.test_ledger test.test_read_entry test.test_account

unittest_debug: clean
	DEBUG_TEST=True python3 -m unittest test.test_account

doc: clean
	mkdir -p build/doc
	cp -r styles build/doc/
	pandoc todo.org --standalone -o build/doc/todo.html -f org -t html --css styles/github-pandoc.css --metadata pagetitle="TODO $(VERSION)"
	pandoc README.md --standalone -o build/doc/README.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="README $(VERSION)"
	pandoc CHANGELOG.md --standalone -o build/doc/CHANGELOG.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="CHANGELOG $(VERSION)"
	java -jar $(PLANTUML) doc/model.uml

travis_ci: clean
	find / -name "libgncmod-app-utils.so"
	python3 travis_ci.py
