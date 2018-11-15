all: clean run

clean:
	clear
	rm example/test_ledger.gnucash.*
	git checkout example/test_ledger.gnucash

test: clean test_verbose

# TODO use gnu time
run:
	python3 gnucash_importer.py -gf example/test_ledger.gnucash -a nubank -af example/local/nubank-2016-10.ofx

run_verbose:
	python3 gnucash_importer.py -gf example/test_ledger.gnucash -a nubank -af example/local/nubank-2016-10.ofx -v

test_verbose: run_verbose
	git diff HEAD example/test_ledger.gnucash
