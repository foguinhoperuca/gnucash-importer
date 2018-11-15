all: clean run

run:
	time python3 gnucash_importer.py -gf example/test_ledger.gnucash -a nubank -af example/local/nubank-2016-10.ofx -v; git diff HEAD example/test_ledger.gnucash

clean:
	clear
	rm example/test_ledger.gnucash.*
	git checkout example/test_ledger.gnucash
