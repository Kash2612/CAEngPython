FROM python:3.12
# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

# For running our application
CMD ["python3", "manage.py", "runserver", "--host", "0.0.0.0","--port","8000"]