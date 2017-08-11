FROM armv7/armhf-ubuntu:xenial

# File Author / Maintainer
MAINTAINER Matevz Vucnik

RUN apt-get update
RUN apt-get install -y python

ADD deploymentsample.py /root/hello/deploymentsample.py
ADD test.py /root/hello/test.py

# Run app
CMD python /root/hello/test.py
