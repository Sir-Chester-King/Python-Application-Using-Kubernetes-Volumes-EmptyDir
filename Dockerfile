FROM python:latest

# Attributes for MetaData
LABEL authors = "Nicola Ricciardi"

WORKDIR /Docker_Directory
COPY . .

# Set the PYTHONPATH to include the "Docker_Directory" directory
ENV PYTHONPATH "${PYTHONPATH}:/Docker_Directory"

# Ensure the storage directory exists
RUN mkdir -p /Docker_Directory/Storage

# Start application
CMD ["python", "./Main_Code/main.py"]