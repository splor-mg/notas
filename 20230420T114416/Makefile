RESOURCES := $(shell jq -r .resources[].name datapackage.json)
DATA_FILES := $(shell jq -r .resources[].path datapackage.json)
REPORTS := $(addsuffix .json, $(addprefix reports/, $(RESOURCES)))

all: ingest validate

ingest: $(DATA_FILES)

$(DATA_FILES): data/%.csv: data/raw/%.csv
	rsync --itemize-changes --checksum data/raw/* data/

validate: $(REPORTS)

$(REPORTS): reports/%.json: data/%.csv datapackage.json
	frictionless validate --json --resource-name $* datapackage.json > $@
