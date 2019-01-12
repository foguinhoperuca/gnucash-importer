# gnu standard
.PHONY: all clean clean_soft diff-fixture installcheck build_bdist_wheel build sdist dist_test check doc
# .SILENT: clean
SHELL=/bin/sh
ifeq ($(DEB_BUILD),true)
	prefix=/usr
else
	prefix=/usr/local
endif
exec_prefix=$(prefix)
# FIXME srcdir must be setted to .
srcdir=$(prefix)/src
bindir=$(exec_prefix)/bin
libdir=$(exec_prefix)/lib
sysconfdir=$(prefix)/etc
datadir=$(prefix)/share
infodir=$(prefix)/share/doc
mandir=$(prefix)/share/man

# Custom variables
VERSION=$(shell cat gnucash_importer/version.py | tr -d __version__\ =\ \')
DEBIAN_VERSION=$(shell head -n 1 debian/changelog | egrep -o '\([0-9].*\)' | tr -d \(\) | tr -d . | grep -o '\-[0-9]*' | tr -d -)
PLANTUML=/usr/local/plantuml/plantuml.jar
BINARY_NAME=gmi
BIN=dist/$(BINARY_NAME)
DOC=dist/doc
FINALDIR=gnucash-magical-importer

FIXTURE_LEDGER=test/fixtures/test_ledger.gnucash
FIXTURE_CREDITCARD=test/fixtures/creditcard.ofx
APP_RUN_SCRIPT=gnucash_importer/run_app.py
APP_PARAMS= -gf $(FIXTURE_LEDGER) -a nubank -af $(FIXTURE_CREDITCARD)
APP_PARAMS_GENERIC= -gf $(FIXTURE_LEDGER) -a generic -af $(FIXTURE_CREDITCARD) -acf "Liabilities:Credit Card:Nubank" -act "Imbalance-BRL:nubank"

CFGS=/etc/gnucash-magical-importer /usr/local/etc/gnucash-magical-importer /usr/etc/gnucash-magical-importer $(HOME)/.gnucash-magical-importer
# TODO implement mkinstalldirs
# FIXME need / between $(bindir) and $(FINALDIR) ?!?
DIRS=$(DESTDIR)$(bindir)/$(FINALDIR) $(DESTDIR)$(libdir)/$(FINALDIR) $(DESTDIR)$(sysconfdir)/$(FINALDIR) $(DESTDIR)$(infodir)/$(FINALDIR)

all: clean build

clean:
	clear
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find test/fixtures -name 'test_ledger.gnucash.*' -exec rm --force {} +
	find doc/ -name '*.png' -exec rm --force {} +
	rm -rf debian/.debhelper/
	rm -rf debian/files
	rm -rf debian/gnucash-magical-importer.substvars
	rm -rf debian/gnucash-magical-importer/
	rm -rf build
	rm -rf dist
	rm -rf gnucash_magical_importer.egg-info
	rm -rf debian/debhelper-build-stamp
	git checkout $(FIXTURE_LEDGER)
	@echo "prefix " $(prefix) " DEB_BUILD " $(DEB_BUILD) " DEBIAN_VERSION " $(DEBIAN_VERSION)
	@echo "------------------- CLEANNED -------------------"
	@echo ""

distclean: clean
	rm -rf ../gnucash-magical-importer_$(VERSION)-$(DEBIAN_VERSION)_amd64.deb
	rm -rf ../gnucash-magical-importer-dbgsym_$(VERSION)-$(DEBIAN_VERSION)_amd64.ddeb
	rm -rf ../python3-gnucash-magical-importer_$(VERSION)-$(DEBIAN_VERSION)_amd64.buildinfo
	rm -rf ../python3-gnucash-magical-importer_$(VERSION)-$(DEBIAN_VERSION)_amd64.changes
	rm -rf ../python3-gnucash-magical-importer_$(VERSION)-$(DEBIAN_VERSION).debian.tar.xz
	rm -rf ../python3-gnucash-magical-importer_$(VERSION)-$(DEBIAN_VERSION).dsc

mostlyclean:
	clear
	find . -name 'test_ledger.gnucash.*' -exec rm --force {} +
	git checkout $(FIXTURE_LEDGER)
	@echo "------------------- CLEANNED SOFT-------------------"
	@echo ""

maintainer-clean:
	@echo "TODO implement it!!"
	@echo "prefix is: " $(prefix) " -- " $(DEB_BUILD)

# info: foo.info
# foo.info: foo.texi chap1.texi chap2.texi
#         $(MAKEINFO) $(srcdir)/foo.texi
# TODO implement awesome_bot (ruby) CHANGELOG.md --allow-ssl
info: clean
	@mkdir -p $(DOC)
	@cp -r styles $(DOC)
	@pandoc todo.org --standalone -o $(DOC)/todo.html -f org -t html --css styles/github-pandoc.css --metadata pagetitle="TODO $(VERSION)"
	@pandoc README.md --standalone -o $(DOC)/README.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="README $(VERSION)"
	@pandoc CHANGELOG.md --standalone -o $(DOC)/CHANGELOG.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="CHANGELOG $(VERSION)"
	@java -jar $(PLANTUML) doc/model.uml -o ../$(DOC)

dist: distclean
	tar -czvf ../python3-gnucash-magical-importer_$(VERSION).orig.tar.gz ../python3-gnucash-magical-importer-$(VERSION)

installdirs: mkinstalldirs
	echo "TODO implement it!"
	$(srcdir)/mkinstalldirs \
		$(DESTDIR)$(bindir) $(DESTDIR)$(datadir) \
		$(DESTDIR)$(libdir) $(DESTDIR)$(infodir) \
		$(DESTDIR)$(mandir)

# You can, also, pass PARAMS=-v to verbose output
installcheck: build setup-cfg
	@echo ""
	@echo "------------------- RUNNING -------------------"
	@echo ""
	$(BIN) $(APP_PARAMS) $(PARAMS)
	@$(MAKE) diff-fixture
	@echo ""
	@echo "------------------- FINISHED nubank account test -------------------"
	@echo ""
	@sleep 1
	$(BIN) $(APP_PARAMS_GENERIC) $(PARAMS)
	@$(MAKE) diff-fixture
	@echo ""
	@echo "------------------- FINISHED generic account test -------------------"
	@echo ""

build: clean info
	cxfreeze gnucash_importer/run_app.py --target-dir dist --target-name $(BINARY_NAME) -s

debian: dist
	dpkg-buildpackage -us -uc

build-bdist_wheel:
	python3 setup.py sdist bdist_wheel

sdist:
	python3 setup.py sdist

dist_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# TEST

# You can pass DEBUG_TEST=True to update loggin level to DEBUG. You can, also, pass PARAMS=-v to verbose output
check: clean setup-cfg test-check
test-check:
	python3 -m unittest test.test_ledger test.test_read_entry test.test_account test.test_classifier
	$(MAKE) diff-fixture
	sleep 1
	python3 $(APP_RUN_SCRIPT) $(APP_PARAMS) $(PARAMS)
	$(MAKE) diff-fixture
	sleep 1
	python3 $(APP_RUN_SCRIPT) $(APP_PARAMS_GENERIC) $(PARAMS)
	$(MAKE) diff-fixture

coverage: clean
	coverage run --source gnucash_importer/ $(APP_RUN_SCRIPT) $(APP_PARAMS)
	coverage report

uninstall: clean
	@echo "------------------- STARTING uninstall -------------------"
	rm -rf $(DESTDIR)$(bindir)/$(BINARY_NAME)
	$(foreach dir,$(DIRS),rm -rf $(dir);)
	@echo "------------------- FINISHED uninstall -------------------"
	@echo ""

install: build info uninstall
	@$(foreach dir, $(DIRS), mkdir -p $(dir);)
	@cp $(BIN) $(DESTDIR)$(bindir)/$(FINALDIR)
	@ln -s $(bindir)/$(FINALDIR)/$(BINARY_NAME) $(DESTDIR)$(bindir)/$(BINARY_NAME)
	@cp dist/libpython3.6m.so.1.0 $(DESTDIR)$(libdir)/$(FINALDIR)/
	@ln -s $(libdir)/$(FINALDIR)/libpython3.6m.so.1.0 $(DESTDIR)$(bindir)/$(FINALDIR)/libpython3.6m.so.1.0
	@cp -r dist/lib $(DESTDIR)$(libdir)/$(FINALDIR)/
	@ln -s $(libdir)/$(FINALDIR)/lib $(DESTDIR)$(bindir)/$(FINALDIR)/lib
	@cp setup.cfg $(DESTDIR)$(sysconfdir)/$(FINALDIR)/
	@cp -r $(DOC) $(DESTDIR)$(infodir)/$(FINALDIR)/
	@echo "------------------- FINISHED copy -------------------"
	@ls -lah $(DESTDIR)$(bindir)/$(BINARY_NAME)
	@$(foreach dir, $(DIRS), tree -L 1 $(dir);)

# HELPER TARGETS
# FIXME automatic get information from dev machine...
docker_build: clean
	sudo docker build -t foguinhoperuca/gnucash_magical_importer . --build-arg USE_APT_PROXY=True --build-arg APT_PROXY=192.168.1.101:8000

docker_run:
	docker run -ti foguinhoperuca/gnucash_magical_importer /bin/sh -c "make test-check"
	@echo "------------------- FINISHED docker_run -------------------"
	@echo ""

docker_prune: clean
	sudo docker system prune -a
	@echo "------------------- FINISHED docker_prune -------------------"
	@echo ""

squid-deb-proxy: clean
	sudo tail -f /var/log/squid-deb-proxy/access.log /var/log/squid-deb-proxy/cache.log /var/log/squid-deb-proxy/store.log

diff-fixture:
	@git diff HEAD $(FIXTURE_LEDGER) | grep --color=always "<gnc:count-data cd:type=\"transaction\">"

remove-cfg:
	@$(foreach cfg, $(CFGS), rm -rf $(cfg); tree -L 1 $(cfg);)

show-cfg:
	@$(foreach cfg, $(CFGS), tree -L 1 $(cfg);)

setup-cfg: clean
	@echo "------------------- RUNNING setup-cfg -------------------"
	@echo ""
	@$(foreach cfg, $(CFGS), rm -rf $(cfg); mkdir -p $(cfg);)
	@$(foreach cfg, $(CFGS), ln -s $(shell pwd)/setup.cfg $(cfg)/setup.cfg;)
	@$(foreach cfg, $(CFGS), ln -s $(shell pwd)/classifier_rules.csv $(cfg)/classifier_rules.csv;)
	@$(foreach cfg, $(CFGS), ln -s $(shell pwd)/regex_rules.csv $(cfg)/regex_rules.csv;)
	@$(foreach cfg, $(CFGS), tree -L 1 $(cfg);)
