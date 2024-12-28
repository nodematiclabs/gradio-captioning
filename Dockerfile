FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN python -c "from transformers import pipeline; pipeline('image-to-text', model='Salesforce/blip-image-captioning-large')"

CMD ["python", "app.py"]