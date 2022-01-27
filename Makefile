all: build

build:
	pdflatex main.tex


clean:
	rm -f *.toc *.log *.out *.pdf *.aux

