# Pulls the official base image
FROM python:3.11

# Copy project files to the destination file
COPY . /usr/src/app/
COPY static/ /usr/src/app/

# Set work directory
WORKDIR /usr/src/app

# Set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

VOLUME /static/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
