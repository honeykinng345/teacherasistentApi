import random
import time
from datetime import datetime
from fake_useragent import UserAgent
from playwright.async_api import async_playwright
from model.ServerProxy import ServerProxy
from utils.json_responses import JsonResponse
from utils.static_functions import StaticFunctions


class WebDriverHandler:
    user_drivers = {}
    proxyIp: str
    proxyPort: str

    def __init__(self, ip, port):
        self.proxyIp = ip
        self.proxyPort = port

    @classmethod
    async def initialize_playwright_instance(cls, appId, proxyIp, proxyPort):
        try:
            proxyServerInformation: ServerProxy
            if len(StaticFunctions.workingProxyList) < 0:
                time.sleep(4)
            proxyServerInformation = random.choice(StaticFunctions.workingProxyList)

            # Initialize Playwright
            playwright = await async_playwright().start()
            browser = await playwright.chromium.launch(headless=True, args=[
                "--force-dark-mode",  # Enable dark mode
                "--disable-gpu",  # Disable GPU
                "--no-sandbox",  # No sandbox for security bypass
                "--disable-blink-features=AutomationControlled",  # Disable automation control
                "--disable-web-security",  # Disable web security
                "--disable-features=WebRTC",  # Disable WebRTC
                "--window-size=1920,1080",  # Window size
            ], proxy={
                "server": f"http://{proxyServerInformation.ip}:{proxyServerInformation.port}",
                "username": proxyServerInformation.userName,
                "password": proxyServerInformation.password
            })
            context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                                                           "Chrome/91.0.4472.124 Safari/537.36",
                                                viewport={"width": 1920, "height": 1080},  # Set window size
                                                java_script_enabled=True)  # Enable JS for proper page loading)
            page = await context.new_page()

            # browser = playwright.chromium.launch(headless=False, args=["--force-dark-mode"])  # Enable dark mode)
            #
            #
            # context = browser.new_context()  # Each context is like a new browser instance
            dictBrowser = {"browser": browser,
                           "context": context,
                           "page": page}

            await page.goto("https://www.perplexity.ai/")

            return dictBrowser

        except Exception as e:
            with open("ScreenFlow.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: initialize_playwright_instance Exception\n")
                f.write(f"{current_datetime}: {str(e)}\n")
                print(f"Error initialize_playwright_instance {e}")

                return JsonResponse.getErrorResponse(message=e, code=400)
