# Python'un hafif bir versiyonunu temel al
FROM python:3.10-slim

# Uygulama klasörünü oluştur
WORKDIR /app

# Gerekli kütüphane listesini kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tüm kodları konteynırın içine kopyala
COPY . .

# Uygulamayı 5000 portunda çalıştır
CMD ["python", "web_service.py"]
