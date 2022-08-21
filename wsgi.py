from app import app

#if script is executed then starts the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')