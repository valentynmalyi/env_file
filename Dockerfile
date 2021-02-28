FROM python:3.8
ENV PYTHONPATH /opt/env_file
WORKDIR /opt/env_file
RUN chmod -R 777 /opt/env_file
COPY . ./
RUN pip install -r requirements.txt
