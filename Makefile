PY=python3
TEX=lualatex

TEX_BUILD_FILE=build_tex.py
HTML_BUILD_FILE=build_html.py
DATA_FILE=data_$(NAME).yaml
NAME=elliot_marsden
CV_TEX_TEMPLATE_FILE=cv.jtex
CV_HTML_TEMPLATE_FILE=cv.jhtml
COVER_TEX_TEMPLATE_FILE=cover.jtex
CV_OUT_FILE=cv_$(NAME)
CV_HTML_FILE=$(CV_OUT_FILE).html
CV_TEX_FILE=build/$(CV_OUTFILE).tex
COVER_TEX_FILE=build/cover_$(NAME).tex

all: cv_pdf cover_pdf

cv_html:
	$(PY) $(HTML_BUILD_FILE) -t $(CV_HTML_TEMPLATE_FILE) -d $(DATA_FILE) -o $(CV_HTML_FILE)

cv_pdf: cv_tex
	$(TEX) $(CV_TEX_FILE)

cover_pdf: cover_tex
	$(TEX) $(COVER_TEX_FILE)

cv_tex:
	$(PY) $(TEX_BUILD_FILE) -t $(CV_TEX_TEMPLATE_FILE) -d $(DATA_FILE) -o $(CV_TEX_FILE)

cover_tex:
	$(PY) $(TEX_BUILD_FILE) -t $(COVER_TEX_TEMPLATE_FILE) -d $(DATA_FILE) -o $(COVER_TEX_FILE)
