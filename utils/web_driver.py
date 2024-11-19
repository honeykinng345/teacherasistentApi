import base64
import json
import os
import random
import time
import traceback
from datetime import datetime

from fake_useragent import UserAgent
from playwright.async_api import async_playwright

from model.ServerProxy import ServerProxy
from utils.extension import proxies
from utils.json_responses import JsonResponse
from utils.static_functions import StaticFunctions

browser_instances = {}


class WebDriverHandler:
    user_drivers = {}
    proxyIp: str
    proxyPort: str

    def __init__(self, ip, port):
        self.proxyIp = ip
        self.proxyPort = port

    BROWSER_SETTINGS = [
        "--force-dark-mode",  # Enable dark mode
        "--disable-gpu",  # Disable GPU
        "--no-sandbox",  # No sandbox for security bypass
        "--disable-blink-features=AutomationControlled",  # Disable automation control
        "--disable-web-security",  # Disable web security
        "--disable-features=WebRTC",  # Disable WebRTC
        "--window-size=1920,1080",  # Window size
        "--headless=new",
        "--deny-permission-prompts",
        "--disable-notifications",
    ]

    REQUEST_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    }

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

            proxyServerInformation: ServerProxy
            if len(StaticFunctions.workingProxyList) < 0:
                time.sleep(4)
            proxyServerInformation = random.choice(StaticFunctions.workingProxyList)

            print("Enter initialize_playwright_instance")
            ua = UserAgent()
            user_agent = ua.random
            print(user_agent)
            # Initialize Playwright
            playwright = await async_playwright().start()
            browser = await playwright.chromium.launch(headless=True, args=cls.BROWSER_SETTINGS, proxy={
                "server": f"http://{proxyServerInformation.ip}:{proxyServerInformation.port}",
                "username": proxyServerInformation.userName,
                "password": proxyServerInformation.password
            })
            context = await browser.new_context(
                extra_http_headers=cls.REQUEST_HEADERS)  # Enable JS for proper page loading)
            await context.clear_cookies()
            page = await context.new_page()
            page.set_default_navigation_timeout(60000)

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
