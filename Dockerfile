# Pulls the official base image
FROM python:3.11

# Set work directory
WORKDIR /usr/src/app

# Copy project files to the destination file
COPY . /usr/src/app/

# Set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

# Expose port 8000 for accessing the application
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
