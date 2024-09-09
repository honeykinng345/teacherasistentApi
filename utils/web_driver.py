import base64
import json
import os
import random
import time
import traceback
from datetime import datetime

from fake_useragent import UserAgent
from playwright.async_api import async_playwright

from utils.extension import proxies
from utils.json_responses import JsonResponse

browser_instances = {}


class WebDriverHandler:
    user_drivers = {}
    proxyIp: str
    proxyPort: str

    def __init__(self, ip, port):
        self.proxyIp = ip
        self.proxyPort = port

    async def get_or_create_browser_instance(self, proxy_ip, proxy_port):
        global browser_instances
        if self not in browser_instances:
            playwright = await async_playwright().start()
            browser = await playwright.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto("https://www.perplexity.ai/")

            # Store the instance
            browser_instances[self] = {
                "browser": browser,
                "context": context,
                "page": page,
            }
        return browser_instances[self]

    @classmethod
    async def initialize_playwright_instance(cls, appId, proxyIp, proxyPort):
        try:
            with open("ScreenFlow.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: initialize_playwright_instance\n")

            print("Enter initialize_playwright_instance")
            ua = UserAgent()
            user_agent = ua.random
            print(user_agent)
            # Initialize Playwright
            playwright = await async_playwright().start()
            browser = await playwright.chromium.launch(headless=True, proxy={
                "server": "http://gw.dataimpulse.com:823",
                "username": "6e4162a6906dc79e20fa",
                "password": "33e81c17912ec20d"
            })
            context = await browser.new_context(user_agent=str(user_agent))
            page = await context.new_page()

            # Proxy settings
            proxy = {
                "server": f"http://{proxyIp}:{proxyPort}",
                "username": "proxy_user",
                "password": "proxy_pass"
            }

            # browser = playwright.chromium.launch(headless=False, args=["--force-dark-mode"])  # Enable dark mode)
            #
            #
            # context = browser.new_context()  # Each context is like a new browser instance
            dictBrowser = {"browser": browser,
                           "context": context,
                           "page": page}
            print(dictBrowser)

            await page.goto("https://www.perplexity.ai/")

            screenshot_bytes = await page.screenshot(path="perplexity.png")

            encoded_screenshot = base64.b64encode(screenshot_bytes).decode()

            # Log it so you can see the base64 data in Render logs
            print(f"Screenshot (base64When Lunch): {encoded_screenshot}")

            return dictBrowser

        except Exception as e:
            with open("ScreenFlow.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: initialize_playwright_instance Exception\n")
                f.write(f"{current_datetime}: {str(e)}\n")
                print(f"Error initialize_playwright_instance {e}")

                return JsonResponse.getErrorResponse(message=e, code=400)
