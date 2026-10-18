PAPER := paper/main

.PHONY: all paper verify clean

all: paper

paper:
	cd paper && tectonic -X compile main.tex

verify:
	cd verify && python3 ek_core.py && python3 ek_more.py && python3 ek_dual.py

clean:
	rm -rf paper/.preview paper/*.aux paper/*.log paper/*.out verify/__pycache__
