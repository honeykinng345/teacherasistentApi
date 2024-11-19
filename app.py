from quart import Quart, jsonify, request
import logging

from model.User import User
from preplexity_handler.perplexity_web_scrapper import PerplexityHandler
from utils.static_functions import StaticFunctions
from utils.user_handler import UserHandler
from apscheduler.schedulers.background import BackgroundScheduler

app = Quart(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(func=StaticFunctions.JobCheckUserSession, trigger="interval", seconds=900)
scheduler.add_job(func=StaticFunctions.JobInteractWithWebPage, trigger="interval", seconds=20)

scheduler.start()


#StaticFunctions.checkProxyServerWorkingOrNot()


@app.route('/')
async def home():
    return "Welcome to the Teacher Assistant API"


@app.route('/chatrequest', methods=['POST'])
async def amazon_webpage():
    data = await request.get_json()
    query = data.get('query')
    app_id = data.get('appId')

    if not query:
        return jsonify({"error": "Please provide a query parameter"}), 400
    try:
        userObject = await UserHandler.checkUserAlreadyExistOrNot(app_id)

        if isinstance(userObject, User):
            response = await PerplexityHandler.playwright_worker(user=userObject, query=query)
        else:
            # this object has error now
            return userObject

        # Return the scraped response
        return response

    except Exception as e:
        return jsonify(f"error: Error {e}"), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


