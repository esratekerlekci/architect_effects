import sqlite3
from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError


sayfa_bp = Blueprint("sayfa", __name__)
api_bp = Blueprint("api", __name__)


MAKS_UZUNLUK = {"isim": 100, "telefon": 20, "mesaj": 500, "stil": 50}


@sayfa_bp.route("/")
def index():
    return render_template("index.html")


@sayfa_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    veri = request.get_json(silent=True) or {}
    mesaj = (veri.get("mesaj") or "").strip()
    gecmis = veri.get("gecmis") or []

    if not mesaj:
        return jsonify({"basari": False, "hata": "Mesaj boş olamaz."}), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)
        return jsonify({"basari": True, "cevap": cevap})
    except AIServiceError:
        return jsonify({"basari": False, "hata": "Asistan şu an yanıt veremiyor, lütfen biraz sonra tekrar deneyin."}), 503


@api_bp.route("/leads", methods=["POST"])
def lead_kaydet():
    veri = request.get_json(silent=True) or {}
    alanlar = {alan: (veri.get(alan) or "").strip() for alan in MAKS_UZUNLUK}

    if not alanlar["isim"] or not alanlar["telefon"]:
        return jsonify({"basari": False, "hata": "İsim ve telefon zorunludur."}), 400

    for alan, sinir in MAKS_UZUNLUK.items():
        if len(alanlar[alan]) > sinir:
            return jsonify({"basari": False, "hata": f"{alan} en fazla {sinir} karakter olabilir."}), 400

    try:
        lead_ekle(
            alanlar["isim"],
            alanlar["telefon"],
            alanlar["mesaj"] or None,
            alanlar["stil"] or None,
        )
        return jsonify({"basari": True, "mesaj": "Bilgileriniz kaydedildi, teşekkürler!"}), 201
    except sqlite3.Error:
        return jsonify({"basari": False, "hata": "Kayıt sırasında bir sorun oluştu."}), 500


@api_bp.route("/leads", methods=["GET"])
def lead_listele():
    try:
        leadler = tum_leadler()
        # Wix Repeater her satırda _id alanı ister.
        for lead in leadler:
            lead["_id"] = str(lead["id"])
        return jsonify({"basari": True, "leads": leadler})
    except sqlite3.Error:
        return jsonify({"basari": False, "hata": "Kayıtlar okunamadı."}), 500