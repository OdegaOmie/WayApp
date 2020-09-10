from waypi import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host=app.config["FLASK_DOMAIN"], port=app.config["FLASK_PORT"])


        # {
        #     "first_name": "tom",
        #     "last_name": "Tomius",
        #     "email": "user2@domain.com",
        #     "password": "$pbkdf2-sha256$20000$l7K2NkbIWUupNWbsPWfsfQ$Sdu1CfUgRJn5Ep.nEixbkWVpk69zbFTDRBN1QS01D3I"
        # }