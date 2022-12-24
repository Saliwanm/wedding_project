FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /wedding_project
WORKDIR /wedding_project
ADD . /wedding_project/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /wedding_project/