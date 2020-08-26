from waypi import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host=app.config["FLASK_DOMAIN"], port=app.config["FLASK_PORT"])
