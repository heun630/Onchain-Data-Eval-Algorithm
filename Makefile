# Makefile

PYTHON = python3
SCRIPT_DIR = visualization

generate_test_data:
	$(PYTHON) tests/make_test_results.py 100 BTC active_address

show_test_table:
	$(PYTHON) $(SCRIPT_DIR)/csv_to_table.py BTC_active_address_test_data --test
