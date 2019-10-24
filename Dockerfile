FROM python:3.8.0

RUN mkdir -p /opt/aioinjector
WORKDIR /opt/aioinjector

COPY . .

RUN pip install -r requirements.txt
RUN make coverage-deep