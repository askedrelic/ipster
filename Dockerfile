FROM python:3.12-slim

WORKDIR /app
COPY main.py /app

EXPOSE 80
CMD ["python", "main.py", "80"]
