import base64
import random
import traceback
from datetime import datetime

from model import User
import time

from utils.json_responses import JsonResponse


class PerplexityHandler:

    @classmethod
    async def playwright_worker(cls, user: User, query: str):
        try:
            if user.fistTime:
                return await cls.isFirstAttempt(user, query)
            else:
                return await cls.reuseExistingBrowser(user, query)

        except Exception as e:
            traceback_str = traceback.format_exc()
            return JsonResponse.getErrorResponse(
                message=f"Error in playwright_worker {e}\n TraceCallBack: {traceback_str}", code=400)

    @classmethod
    async def isFirstAttempt(cls, user: User, query: str):
        page = user.webDriverPage
        screenshot_bytes = await page.screenshot(path="perplexity.png")

        encoded_screenshot = base64.b64encode(screenshot_bytes).decode()

        # Log it so you can see the base64 data in Render logs
        print(f"Screenshot (base64): {encoded_screenshot}")

        await page.wait_for_selector(".overflow-auto")  # wait for up to 60 seconds
        await page.type(".overflow-auto", query)
        time.sleep(1)

        await page.screenshot(path="perplexity1.png")

        # if await page.is_visible("button svg[data-icon='xmark']"):
        #     await page.click("button svg[data-icon='xmark']")

        await page.wait_for_timeout(12000)

        await page.screenshot(path="perplexity35.png")

        # Dismiss dialog by clicking the cross button
        if await page.is_visible("button svg[data-icon='xmark']"):
            await page.click("button svg[data-icon='xmark']")

        if await page.is_visible("button[aria-label='Submit']"):
            await page.click("button[aria-label='Submit']")
            await page.screenshot(path="p4.png")

        await page.screenshot(path="perplexity34.png")

        # Wait and extract response
        time.sleep(random.uniform(9, 10))
        divs = await page.query_selector_all("div.prose")
        responseList = [await div.inner_text() for div in divs]
        return JsonResponse.getSuccessResponse(responseList, "Received response", 1, 200)

    @classmethod
    async def reuseExistingBrowser(cls, user: User, query: str):
        page = user.webDriverPage
        screenshot_bytes = await page.screenshot(path="exestingUser.png")
        # Scroll down by 1000 pixels
        cls.checkButtonVisibility(page)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        await page.wait_for_selector(".overflow-auto")  # wait for up to 60 seconds
        await page.type(".overflow-auto", query)
        cls.checkButtonVisibility(page)

        time.sleep(3)
        await page.click("button[aria-label='Submit']")
        cls.checkButtonVisibility(page)
        time.sleep(random.uniform(9, 10))
        divs = await page.query_selector_all("div.prose")
        responseList = [await div.inner_text() for div in divs]
        return JsonResponse.getSuccessResponse(responseList, "Received response", 1, 200)

    @classmethod
    def checkButtonVisibility(cls, page):
        close_button = page.locator('button[data-testid="close-modal"]')
        # Check if the close button is visible (dialog appeared)
        if close_button.is_visible():
            # Click the close button to dismiss the dialog
            close_button.click()
            print("Dialog dismissed.")
        else:
            print("Dialog not present.")

# class PerplexityHandler:
#
#     @classmethod
#     def scrape_amazon_webpage(self, query, user: User):
#         try:
#             #browser = user.webDriverHandler
#             #context = browser.new_context()
#             page = user.webDriverPage
#
#             page.screenshot(path="perplexity.png")
#
#             # Interact with the page (sending query to search input)
#             page.fill(".overflow-auto", query)
#             page.screenshot(path="perplexity1.png")
#
#             # Check if button is visible and interact with it
#             if checkButtonIsVisibleOrNot(page, "p2"):
#                 page.click("button[aria-label='Submit']")
#                 page.screenshot(path="p4.png")
#             else:
#                 page.wait_for_timeout(12000)
#                 if checkButtonIsVisibleOrNot(page, "p3"):
#                     page.click(".bg-super")
#                     page.screenshot(path="p5.png")
#
#             page.wait_for_timeout(7000)
#             page.screenshot(path="perplexity6.png")
#
#             # Extract text from divs
#             responseList = [div.inner_text() for div in page.query_selector_all("div.prose")]
#
#             return JsonResponse.getSuccessResponse(responseList, "Received response", 1, 200)
#
#         except Exception as e:
#             with open("PreplexException.txt", "a") as f:
#                 current_datetime = datetime.now()
#                 f.write(f"{current_datetime}: Exception in scrape_amazon_webpage(): \n{e}")
#             return JsonResponse.getErrorResponse("Error Model not Working", 2)
#
#
# def checkButtonIsVisibleOrNot(page, imageName):
#     try:
#         submit_button = page.query_selector("button[aria-label='Submit']")
#         if submit_button and submit_button.is_visible():
#             page.screenshot(path=f"{imageName}.png")
#             return True
#         else:
#             print("Button is either not visible or not enabled.")
#             return False
#     except Exception as e:
#         print(f"Error while checking button visibility: {e}")
#         return False
