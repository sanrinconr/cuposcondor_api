import os
from app import create_app
from waitress import serve

settings_module = os.getenv("APP_SETTINGS_MODULE")
app = create_app(settings_module)
if __name__ == "__main__":
    if os.environ.get("ENVIRONMENT","development") == "production":
        app.debug = False
        port = int(os.environ.get('PORT', 5000))
        serve(app, port=port)
    else:
        app.run(host="0.0.0.0")
