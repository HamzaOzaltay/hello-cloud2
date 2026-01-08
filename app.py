from flask import Flask, render_template_string, request
import os
import psycopg2

app = Flask(__name__)

# Burayı birazdan Render'dan alacağımız linkle değiştireceğiz
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://hamza:ZY8FH80XLY7wTK43bigODSXIc3KVto8p@dpg-d5davbruibrs73fs3ivg-a.oregon-postgres.render.com/hello_cloud3_db_005b")

HTML = """
<!doctype html>
<html>
<head><title>Hüseyin Hamza Özaltay</title></head>
<body>
    <h1>Buluttan Selam!</h1>
    <form method="POST">
        <input type="text" name="isim" placeholder="Adını yaz" required>
        <button type="submit">Gönder</button>
    </form>
    <h3>Ziyaretçiler:</h3>
    <ul>
        {% for ad in isimler %}
        <li>{{ ad }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

def connect_db():
    return psycopg2.connect(DATABASE_URL)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT)")
    if request.method == "POST":
        isim = request.form.get("isim")
        if isim:
            cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s)", (isim,))
            conn.commit()
    cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
    isimler = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return render_template_string(HTML, isimler=isimler)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
