PY=python3
TEX=lualatex

BUILDFILE=build.py
DATAFILE=data_$(NAME).yaml
NAME=elliot_marsden
CVTEMPLATEFILE=cv.jtex
COVERTEMPLATEFILE=cover.jtex
CVTEXFILE=build/cv_$(NAME).tex
COVERTEXFILE=build/cover_$(NAME).tex

all: cv_pdf cover_pdf

cv_pdf: cv_tex
	$(TEX) $(CVTEXFILE)

cover_pdf: cover_tex
	$(TEX) $(COVERTEXFILE)

cv_tex:
	$(PY) $(BUILDFILE) -t $(CVTEMPLATEFILE) -d $(DATAFILE) -o $(CVTEXFILE)

cover_tex:
	$(PY) $(BUILDFILE) -t $(COVERTEMPLATEFILE) -d $(DATAFILE) -o $(COVERTEXFILE)
