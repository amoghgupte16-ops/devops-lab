FROM python:3.12-slim

WORKDIR /app

COPY health_report.py .

CMD ["python", "health_report.py"]