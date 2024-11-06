from app import create_app
from models.main_model import db
import os

app = create_app()

if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()
    port = int(os.getenv("FLASK_PORT", 5000)) 
    app.run(debug=True, port=port)