<!-- build command: pandoc CHANGELOG.md --standalone -o CHANGELOG.html -f gfm -t html --css vimwiki.css --metadata pagetitle="CHANGELOG v1.1.0" -->
<!-- awesome_bot CHANGELOG.md --allow-ssl -->

<!-- Link's references -->
<!-- TODO plan it correctly!! -->
[file_01]: ../../data/cmdb/test_import_desktops.csv
[file_04]: ../../doc/queues.org
[9f4ee56]: http://gnucash-importer.jeffersoncampos.eti.br/db/importer/commits/9f4ee55
[3b872cd]: http://gnucash-importer.jeffersoncampos.eti.br/db/importer/commits/3b872ca

# Changelog #

All notable changes to this project will be documented in this file. More details in [README](README.md).

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased] ##

Here are the scope to be released. See [todo.org](todo.org) for more details.

* Implement UI with ncurse
* Make this package debian friendly
* Create bin version

## [0.1.0][HEAD] - 2018-XX-XX ##

Basic funcional version.

### Latest Commit's Hashes ###

* [data/cmdb/test_import_desktops..:][file_01] [9f4ee55][9f4ee55]
* [doc/queues......................:][file_04] [3b872ca][3b872ca]

### Added ###

* Implemented import transactions from ofx to gnucash
* Implemented tests and fixtures
* Added a build tool (GNU Build System)
* Made this package pypi friendly
* Implementeted a config file
* Added support to logging
* Added this changelog to manage releases
* Implemented basic tests with unittest
* Added basic documentation to source code
* Added support to use docker
* Added use of Travis-CI
