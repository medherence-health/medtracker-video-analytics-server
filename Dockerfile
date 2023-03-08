FROM python:3.6.13

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000
EXPOSE 8501

COPY . .
RUN python scripts/download_models.sh

CMD ["uvicorn", "manage:app", "--host","0.0.0.0", "--port","4000"]
