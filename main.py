from flask_cors import CORS
import logging
from src.app.api.api import *
from src.app.helper.redis_cache import app

app.register_blueprint(MerchantIds)
logging.basicConfig(level=logging.INFO, filename = "global.log")
logging.getLogger('flask_cors').level = logging.DEBUG

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == "__main__":
    app.run(debug=True)


