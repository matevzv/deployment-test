FROM multiarch/alpine:x86-latest-stable

# File Author / Maintainer
MAINTAINER Matevz Vucnik

RUN apk update && apk upgrade
RUN apk add python

ADD deploymentsample.py /root/hello/deploymentsample.py
ADD test.py /root/hello/test.py

# Run app
CMD python /root/hello/test.py
