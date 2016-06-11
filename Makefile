PY=python3
TEX=lualatex

MKDIR_P = mkdir -p

NAME=elliot_marsden
BUILD_DIR="build"
TEX_BUILD_FILE=build_tex.py
HTML_BUILD_FILE=build_html.py
DATA_HTML_FILE=data_${NAME}_html.yaml
DATA_TEX_FILE=data_${NAME}_tex.yaml
CV_TEX_TEMPLATE_FILE=cv.jtex
CV_HTML_TEMPLATE_FILE=cv.jhtml
COVER_TEX_TEMPLATE_FILE=cover.jtex
CV_OUT_FILE=cv_${NAME}
CV_HTML_FILE=${CV_OUT_FILE}.html
CV_TEX_FILE=${BUILD_DIR}/${CV_OUT_FILE}.tex
COVER_TEX_FILE=${BUILD_DIR}/cover_${NAME}.tex

all: cv_pdf cover_pdf

cv_html:
	${PY} ${HTML_BUILD_FILE} -t ${CV_HTML_TEMPLATE_FILE} -d ${DATA_HTML_FILE} -o ${CV_HTML_FILE}

cv_pdf: cv_tex
	${TEX} ${CV_TEX_FILE}

cover_pdf: cover_tex
	${TEX} ${COVER_TEX_FILE}

cv_tex: build_dir
	${PY} ${TEX_BUILD_FILE} -t ${CV_TEX_TEMPLATE_FILE} -d ${DATA_TEX_FILE} -o ${CV_TEX_FILE}

cover_tex: build_dir
	${PY} ${TEX_BUILD_FILE} -t ${COVER_TEX_TEMPLATE_FILE} -d ${DATA_TEX_FILE} -o ${COVER_TEX_FILE}

build_dir:
	${MKDIR_P} ${BUILD_DIR}
