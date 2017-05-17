TEX=lualatex

MKDIR_P = mkdir -p

NAME=elliot_marsden
BUILD_DIR="build"
BUILD_CMD=python3 build.py
DATA_FILE=data_${NAME}.yaml
CV_TEX_TEMPLATE_FILE=cv.jtex
CV_HTML_TEMPLATE_FILE=cv.jhtml
COVER_TEX_TEMPLATE_FILE=cover.jtex
CV_OUT_FILE=cv_${NAME}
CV_HTML_FILE=${CV_OUT_FILE}.html
CV_TEX_FILE=${BUILD_DIR}/${CV_OUT_FILE}.tex
COVER_TEX_FILE=${BUILD_DIR}/cover_${NAME}.tex

all: cv_pdf cover_pdf cv_html

cv_html:
	${BUILD_CMD} -f html -t ${CV_HTML_TEMPLATE_FILE} -d ${DATA_FILE} -o ${CV_HTML_FILE}

cv_pdf: cv_tex
	${TEX} ${CV_TEX_FILE}

cover_pdf: cover_tex
	${TEX} ${COVER_TEX_FILE}

cv_tex: build_dir
	${BUILD_CMD} -f tex -t ${CV_TEX_TEMPLATE_FILE} -d ${DATA_FILE} -o ${CV_TEX_FILE}

cover_tex: build_dir
	${BUILD_CMD} -f tex -t ${COVER_TEX_TEMPLATE_FILE} -d ${DATA_FILE} -o ${COVER_TEX_FILE}

build_dir:
	${MKDIR_P} ${BUILD_DIR}
