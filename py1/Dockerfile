FROM python:3.9-rc-buster

WORKDIR /app

EXPOSE 80
EXPOSE 81

RUN apt-get update 

RUN pip install --upgrade pip
COPY . /app 
RUN pip install -r requirements.txt
 

 
 
CMD python ./python_file.py