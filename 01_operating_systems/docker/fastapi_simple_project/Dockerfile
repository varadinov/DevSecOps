FROM python:3.10
RUN pip3 install "fastapi[all]"
WORKDIR /app
ADD main.py /app/
CMD  python -m uvicorn main:app --host 0.0.0.0 --port 8000