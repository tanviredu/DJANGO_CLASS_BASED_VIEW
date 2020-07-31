FROM ubuntu
RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install django
RUN pip3 install django-crispy-forms
RUN pip3 install django misaka
RUN pip3 install Pillow
EXPOSE 8888

