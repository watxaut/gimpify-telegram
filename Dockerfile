FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk update && apk add build-base && apk add g++ libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev
RUN apk --no-cache add cmake clang clang-dev make gcc g++ libc-dev linux-headers
RUN apk --no-cache add jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python", "./main.py" ]