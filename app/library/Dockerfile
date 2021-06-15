FROM python:3.8.5

WORKDIR /app
RUN pip install -r requirements.txt
COPY ./ /app

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]