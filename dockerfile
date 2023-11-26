FROM python:3.10
WORKDIR /home/dell/dbpython
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "src/login/__main__.py"]
