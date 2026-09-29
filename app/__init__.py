import os
from flask import Flask, jsonify
from flask_cors import CORS

from config import config
from app.database import init_db
from app.routes import sayfa_bp, api_bp


def create_app(config_adi=None):
    
    config_adi = config_adi or os.environ.get("FLASK_ENV_NAME", "default")

    app = Flask(__name__)

  
    app.config.from_object(config[config_adi])


    CORS(app, origins=app.config["CORS_ORIGINS"])


    init_db(app)

    # 4) Blueprint'leri kaydet; API'ye /api öneki veriliyor
    app.register_blueprint(sayfa_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

   
    @app.route("/health")
    def health():
        return jsonify({"basari": True, "durum": "aktif"})


    return app