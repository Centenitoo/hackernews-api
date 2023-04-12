FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /Hackernews/
WORKDIR /Hackernews
COPY requirments.txt /Hackernews/
RUN pip install -r requirments.txt
COPY . /Hackernews/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8000