FROM python:3.11-slim

#nonroot
RUN adduser --disabled-password --gecos "" appuser
WORKDIR /app

#install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy app
COPY src ./src

ENV 	PYTHONPATH=/app \
	PORT=8000 \
	APP_VERSION=dev

EXPOSE 8000
USER appuser

CMD ["gunicorn", "-b", "0.0.0.0:8000", "src.app:app"]
