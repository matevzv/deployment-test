FROM mateu/debian:wheezy-i386

# File Author / Maintainer
MAINTAINER Matevz Vucnik

RUN apt-get update
RUN apt-get install python

ADD deploymentsample.py /root/hello/deploymentsample.py
ADD test.py /root/hello/test.py

# Run app
CMD python /root/hello/test.py
