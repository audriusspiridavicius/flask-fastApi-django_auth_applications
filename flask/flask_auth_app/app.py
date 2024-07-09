from flask_auth_app import create_app



if __name__ == "__main__":
    app = create_app()
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True)
    app.run(
    host='127.0.0.1', port="5000", debug=True,
    ssl_context=('cert.pem', 'key.pem')
)       