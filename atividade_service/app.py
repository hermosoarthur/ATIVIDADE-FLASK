
from config import db
from controllers.atividade_controller import atividade_bp
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(atividade_bp, url_prefix='/atividades')

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
