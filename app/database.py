import sqlite3
from flask import current_app


def get_db():

    baglanti = sqlite3.connect(current_app.config["DATABASE_URL"])
    baglanti.row_factory = sqlite3.Row
    return baglanti


def init_db(app):
  
    with app.app_context():
        baglanti = get_db()
        baglanti.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                isim    NVARCHAR(100) NOT NULL,
                telefon NVARCHAR(20) NOT NULL,
                mesaj   NVARCHAR(500),
                stil    NVARCHAR(50),
                tarih   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        baglanti.commit()
        baglanti.close()


def lead_ekle(isim, telefon, mesaj=None, stil=None):

    baglanti = get_db()
    try:
        baglanti.execute(
            "INSERT INTO leads (isim, telefon, mesaj, stil) VALUES (?, ?, ?, ?)",
            (isim, telefon, mesaj, stil),
        )
        baglanti.commit()
    finally:
        baglanti.close()


def tum_leadler():

    baglanti = get_db()
    try:
        satirlar = baglanti.execute("SELECT * FROM leads ORDER BY id DESC").fetchall()
        return [dict(satir) for satir in satirlar]
    finally:
        baglanti.close()