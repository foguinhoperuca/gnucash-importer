<!-- Link's references -->
<!-- TODO plan it correctly!! -->
[HEAD_COMMIT]: https://github.com/foguinhoperuca/gnucash_magical_importer/commits/master "HEAD on master."
[v0.1.0]: https://github.com/foguinhoperuca/gnucash_magical_importer/commit/ "v0.1.0"
[debian_v0.1.0]: ../../doc/queues.org
[tarball_v0.1.0]: http://gnucash-importer.jeffersoncampos.eti.br/db/importer/commits/9f4ee55
[pypi_v0.1.0]: http://gnucash-importer.jeffersoncampos.eti.br/db/importer/commits/3b872ca

# Changelog #

All notable changes to this project will be documented in this file. More details in [README](README.md).

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/foguinhoperuca/gnucash_magical_importer/blob/master/todo.org "Detailed tasks.") ##

Here are the scope to be released. See [todo.org](todo.org) for more details.

* Implement UI with ncurse/web view
* Dist package in debian (stable), ubuntu (ppa/snap) and pypi (wheel)
* Create data file
* Implement abstract class
* Implement classifier
* Write log to file
* Gnu man page
* Publish about software in gnucash forum, blogpost, vivaolinux.com.br, etc
* Fix integration with C lib to get total number of transactions

## [0.1.0][v0.1.0][HEAD][HEAD_COMMIT] - 2018-12-26 ##

Basic funcional version with importing data.
Closes #1

### Latest File Release ###

* [debian binary..0.1.0][debian-binary_v0.1.0]
* [tarball........0.1.0][tarbal_v0.1.0]
* [pypi...........0.1.0][pypi_v0.1.0]

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
* Make this package debian friendly
* Create bin version
