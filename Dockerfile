FROM python:3.14-slim

WORKDIR /app
COPY script2.py .

ENV TERM=xterm
ENV PYTHONUNBUFFERED=1

CMD ["python", "script2.py"]