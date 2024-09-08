from quart import Quart, jsonify, request
from threading import Thread
import asyncio
from datetime import datetime
from playwright.async_api import async_playwright
import logging

from preplexity_handler.perplexity_web_scrapper import PerplexityHandler
from utils.user_handler import UserHandler

app = Quart(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# # Dictionary to store user-specific Playwright instances
# browser_instances = {}
# # Create an asyncio task queue
# task_queue = asyncio.Queue()
#
#
# # Async function to get or create browser instance
# async def get_or_create_browser_instance(app_id, proxy_ip, proxy_port):
#     global browser_instances
#     if app_id in browser_instances:
#         return browser_instances[app_id]
#     else:
#         playwright = await async_playwright().start()
#         browser = await playwright.chromium.launch(headless=True)
#         context = await browser.new_context()
#         page = await context.new_page()
#         await page.goto("https://www.perplexity.ai/")
#
#         # Store the instance
#         browser_instances[app_id] = {"browser": browser, "context": context, "page": page}
#         return browser_instances[app_id]
#
#
# # Async function to run the Playwright logic
# async def playwright_worker(app_id, query):
#     try:
#         user_browser = await get_or_create_browser_instance(app_id, "123.45.67.89", "434")
#         page = user_browser["page"]
#
#         # Perform scraping actions
#         await page.screenshot(path="perplexity.png")
#         await page.fill(".overflow-auto", query)
#         await page.screenshot(path="perplexity1.png")
#
#         if await page.is_visible("button[aria-label='Submit']"):
#             await page.click("button[aria-label='Submit']")
#             await page.screenshot(path="p4.png")
#
#         # Wait and extract response
#         await page.wait_for_timeout(7000)
#         return [
#             await div.inner_text()
#             for div in await page.query_selector_all("div.prose")
#         ]
#     except Exception as e:
#         return {"error": str(e)}


@app.route('/')
async def home():
    return "Welcome to the Teacher Assistant API"


# @app.route('/chatrequest', methods=['POST'])
# async def amazon_webpage():
#     data = await request.get_json()
#     query = data.get('query')
#     app_id = data.get('appId')
#
#     if not query:
#         return jsonify({"error": "Please provide a query parameter"}), 400
#
#     try:
#         # Run the Playwright worker and wait for the result
#         response = await playwright_worker(app_id, query)
#
#         # Check if there was an error
#         if isinstance(response, dict) and "error" in response:
#             return jsonify(response), 400
#
#         # Return the scraped response
#         return jsonify({"response": response}), 200
#
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400


@app.route('/chatrequest', methods=['POST'])
async def amazon_webpage():
    data = await request.get_json()
    query = data.get('query')
    app_id = data.get('appId')

    if not query:
        return jsonify({"error": "Please provide a query parameter"}), 400
    try:
        userObject = await UserHandler.checkUserAlreadyExistOrNot(app_id)
        print(f"userObject: {userObject}, Type: {type(userObject)}")

        if isinstance(userObject, dict) and "error" in userObject:
            return jsonify(userObject), 400

        response = await PerplexityHandler.playwright_worker(user=userObject, query=query)
        # Check if there was an error
        if isinstance(response, dict) and "error" in response:
            return jsonify(response), 400

        # Return the scraped response
        return response

    except Exception as e:
        return jsonify(f"error: Error {e}"), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
