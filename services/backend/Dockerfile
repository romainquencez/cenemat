FROM python:3.11-buster

WORKDIR /app

# set environment variables
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy  requirements
COPY requirements*.txt ./

# upgrade packages
RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements-dev.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# expose server port
EXPOSE 80

# executing command
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
