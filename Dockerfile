FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /mangas/
WORKDIR /mangas
COPY requirements.txt /mangas/
RUN pip install -r requirements.txt
COPY . /mangas/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8000