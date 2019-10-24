FROM python

RUN mkdir -p /opt/aioinjector
WORKDIR /opt/aioinjector

COPY . .

RUN pip install -r requirements.txt
RUN make coverage-deep