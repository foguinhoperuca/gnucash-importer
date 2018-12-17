# gnu standard
.PHONY: all clean clean_soft diff-fixture installcheck build_bdist_wheel build sdist dist_test check doc
# .SILENT: clean
SHELL=/bin/sh
# FIXME Use make prefix=/usr <TARGET> for debian package build
prefix=/usr
exec_prefix=$(prefix)
# FIXME srcdir must be setted to .
srcdir=$(prefix)/src
bindir=$(exec_prefix)/bin
libdir=$(exec_prefix)/lib
# FIXME for debian installation, the sysconfdir must be /etc/gnucash-magical-importer/
sysconfdir=$(prefix)/etc
datadir=$(prefix)/share
infodir=$(prefix)/share/doc
mandir=$(prefix)/share/man
# DESTDIR=$(HOME)/

# Custom variables
VERSION=$(shell cat gnucash_importer/version.py | tr -d __version__\ =\ \')
FIXTURE_LEDGER=test/fixtures/test_ledger.gnucash
FIXTURE_CREDITCARD=test/fixtures/creditcard.ofx
PLANTUML=/usr/local/plantuml/plantuml.jar
BINARY_NAME=gnucash_magical_importer
BIN=dist/$(BINARY_NAME)

APP_RUN_SCRIPT=gnucash_importer/run_app.py
APP_PARAMS= -gf $(FIXTURE_LEDGER) -a nubank -af $(FIXTURE_CREDITCARD)
APP_PARAMS_GENERIC= -gf $(FIXTURE_LEDGER) -a generic -af $(FIXTURE_CREDITCARD) -acf "Liabilities:Credit Card:Nubank" -act "Imbalance-BRL:nubank"

all: clean build

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
	rm -rf debian/debhelper-build-stamp
	git checkout $(FIXTURE_LEDGER)
	@echo "------------------- CLEANNED -------------------"
	@echo ""

clean_soft:
	clear
	find . -name 'test_ledger.gnucash.*' -exec rm --force {} +
	git checkout $(FIXTURE_LEDGER)
	@echo "------------------- CLEANNED SOFT-------------------"
	@echo ""

distclean: clean
	rm -rf ../python3-gnucash-magical-importer-$(VERSION).tar.gz

mostlyclean:
	@echo "TODO implement it!!"
	@echo "FIXME can replace clean_soft?!?"

maintainer-clean:
	@echo "TODO implement it!!"

# info: foo.info
# foo.info: foo.texi chap1.texi chap2.texi
#         $(MAKEINFO) $(srcdir)/foo.texi

dist: distclean
	tar -czvf ../python3-gnucash-magical-importer_$(VERSION).orig.tar.gz ../python3-gnucash-magical-importer-$(VERSION)

installdirs: mkinstalldirs
	echo "TODO implement it!"
	$(srcdir)/mkinstalldirs \
		$(DESTDIR)$(bindir) $(DESTDIR)$(datadir) \
		$(DESTDIR)$(libdir) $(DESTDIR)$(infodir) \
		$(DESTDIR)$(mandir)

# You can, also, pass PARAMS=-v to verbose output
installcheck: build
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

diff-fixture:
	@git diff HEAD $(FIXTURE_LEDGER) | grep --color=always "<gnc:count-data cd:type=\"transaction\">"

build: clean
	cxfreeze gnucash_importer/run_app.py --target-dir dist --target-name $(BINARY_NAME) -s

build_bdist_wheel:
	python3 setup.py sdist bdist_wheel

build_debian:
	dpkg-buildpackage -us -uc

sdist:
	python3 setup.py sdist

dist_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# TEST

# You can pass DEBUG_TEST=True to update loggin level to DEBUG
# You can, also, pass PARAMS=-v to verbose output
check:
	python3 -m unittest test.test_ledger test.test_read_entry test.test_account
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

doc: clean
	@mkdir -p build/doc
	@cp -r styles build/doc/
	@pandoc todo.org --standalone -o build/doc/todo.html -f org -t html --css styles/github-pandoc.css --metadata pagetitle="TODO $(VERSION)"
	@pandoc README.md --standalone -o build/doc/README.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="README $(VERSION)"
	@pandoc CHANGELOG.md --standalone -o build/doc/CHANGELOG.html -f gfm -t html --css styles/github-pandoc.css --metadata pagetitle="CHANGELOG $(VERSION)"
	@java -jar $(PLANTUML) doc/model.uml

squid-deb-proxy: clean
	sudo tail -f /var/log/squid-deb-proxy/access.log /var/log/squid-deb-proxy/cache.log /var/log/squid-deb-proxy/store.log

# FIXME automatic get information from dev machine...
docker_build: clean
	sudo docker build -t foguinhoperuca/gnucash_magical_importer . --build-arg USE_APT_PROXY=True --build-arg APT_PROXY=192.168.1.101:8000

docker_run:
	docker run -ti foguinhoperuca/gnucash_magical_importer /bin/sh -c "make check"
	@echo "------------------- FINISHED docker_run -------------------"
	@echo ""

docker_prune: clean
	sudo docker system prune -a
	@echo "------------------- FINISHED docker_prune -------------------"
	@echo ""

uninstall: clean
	@echo "------------------- STARTING manual_clean_bin -------------------"
	rm -rf $(DESTDIR)$(bindir)/gnucash_magical_importer
	rm -rf $(DESTDIR)$(bindir)/gnucash-magical-importer/
	rm -rf $(DESTDIR)$(libdir)/gnucash-magical-importer/
	rm -rf $(DESTDIR)$(sysconfdir)/gnucash-magical-importer/
	@echo "------------------- FINISHED manual_clean_bin -------------------"
	@echo ""

# FIXME use python3 setup.py install --prefix=/usr to install correctly
install: uninstall build
	@mkdir -p $(DESTDIR)$(bindir)/gnucash-magical-importer/
	@mkdir -p $(DESTDIR)$(libdir)/gnucash-magical-importer/
	@mkdir -p $(DESTDIR)$(sysconfdir)/gnucash-magical-importer/
	@cp dist/gnucash_magical_importer $(DESTDIR)$(bindir)/gnucash-magical-importer/
	@ln -s $(DESTDIR)$(bindir)/gnucash-magical-importer/gnucash_magical_importer $(DESTDIR)$(bindir)/gnucash_magical_importer
	@cp dist/libpython3.6m.so.1.0 $(DESTDIR)$(bindir)/gnucash-magical-importer/
	@cp -r dist/lib $(DESTDIR)$(bindir)/gnucash-magical-importer/ # FIXME not working in $(DESTDIR)$(libdir) yet!!
	@cp setup.cfg $(DESTDIR)$(sysconfdir)/gnucash-magical-importer/	 # FIXME test if program can found .cfg
	@echo "------------------- FINISHED copy -------------------"
	@ls -lah $(DESTDIR)$(bindir)/gnucash_magical_importer
	@tree -L 1 $(DESTDIR)$(bindir)/gnucash-magical-importer
	@tree -L 1 $(DESTDIR)$(libdir)/gnucash-magical-importer
	@tree -L 1 $(DESTDIR)$(sysconfdir)/gnucash-magical-importer
