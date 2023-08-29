FROM python:3.8-slim

COPY requirements.txt .

WORKDIR /1_💻_Laptop

COPY . ./

RUN pip install  --no-cache-dir -r requirements.txt 

EXPOSE 8051

CMD ["streamlit","run", "--server.port", "8051", "--server.address", "0.0.0.0", "1_💻_Laptop.py"]


