.PHONY: init sync collection collect index clobber black clean prune
.SECONDARY:
.DELETE_ON_ERROR:

DATASET_NAMES=local-plan
DATASET_FILES=dataset/local-plan.csv
PROTOTYPE_DATA=dataset/local-plan-data.csv

LOG_FILES=$(wildcard collection/log/*/*.json)
LOG_FILES_TODAY=collection/log/$(shell date +%Y-%m-%d)/

all: collect collection

collection: collection/index.json

collect:	$(DATASET_FILES)
	python3 bin/collector.py $(DATASET_NAMES)

collection/index.json: bin/index.py $(DATASET_FILES) $(LOG_FILES)
	python3 bin/index.py

dataset/local-plan.csv:	$(PROTOTYPE_DATA)
	python3 bin/local-plan.py < $(PROTOTYPE_DATA) > $@

$(PROTOTYPE_DATA):
	@-mkdir -p dataset
	curl -qs 'https://local-plans-prototype.herokuapp.com/local-plans/local-plan-data.csv' > $@

black:
	black .

clobber::
	rm -rf $(LOG_FILES_TODAY) $(PROTOTYPE_DATA)

init::
	pip3 install -r requirements.txt
