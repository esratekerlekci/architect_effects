from app import create_app

app = create_app()

if __name__ == "__main__":
    # Mac'te 5000 portunu AirPlay kullandığı için 5001 seçildi.
    app.run(port=5001, debug=app.config["DEBUG"])