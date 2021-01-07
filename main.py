from src.app.helper.connect_cache import app
from src.app.Controller.Controllers import MerchantIds
from flask_cors import CORS
import logging

app.register_blueprint(MerchantIds)
logging.basicConfig(level=logging.INFO)
logging.getLogger('flask_cors').level = logging.DEBUG

CORS(MerchantIds, resources=r'/api/*')

if __name__ == "__main__":
    app.run(debug=True)


