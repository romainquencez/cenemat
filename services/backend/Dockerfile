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
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements-dev.txt

# for migrations
COPY migrations .
COPY pyproject.toml .

COPY src/ .

# expose server port
EXPOSE 5000

# executing command
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
