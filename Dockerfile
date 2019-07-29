FROM python:3.6
# Set up code directory
RUN mkdir -p /usr/src/app/trinity
WORKDIR /usr/src/app/trinity

COPY . /usr/src/app/trinity
RUN apt-get update
RUN apt-get install libsnappy-dev -y
RUN pip install -e .[dev]  --no-cache-dir
RUN pip install -U trinity --no-cache-dir
#RUN cd .. && git clone http://github.com/cd4761/eth-ecc.git && cd eth-ecc && python setup.py install
#RUN find . -name \*.pyc -delete

RUN echo "Type \`trinity\` to boot or \`trinity --help\` for an overview of commands"

EXPOSE 30303 30303/udp
#ENTRYPOINT ["trinity"]
