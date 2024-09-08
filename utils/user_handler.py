from datetime import datetime

from model.User import User
from utils.global_objects import Global
from utils.json_responses import JsonResponse
from utils.web_driver import WebDriverHandler

userObject: User  # Initialize the global variable at the module level


class UserHandler:
    userObject: User

    @classmethod
    async def checkUserAlreadyExistOrNot(cls, appId):
        try:
            with open("ScreenFlow.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: initialize_playwright_instance\n")

            global userObject

            if appId not in Global.user_map:
                webDriver = WebDriverHandler(ip="123.45.67.89", port="434")

                getBrowserData = await webDriver.initialize_playwright_instance(appId, webDriver.proxyIp, webDriver.proxyPort)
                browser = getBrowserData["browser"]
                page = getBrowserData["page"]
                context = getBrowserData["context"]
                Global.user_map[appId] = User(appId, "12345", webDevBrowser=browser, webPage=page, webContext=context)
                userObject = Global.user_map[appId]
                return userObject
            else:
                with open("ScreenFlow.txt", "a") as f:
                    current_datetime = datetime.now()
                    f.write(f"{current_datetime}:getExistingUser()\n{Global.user_map[appId]}")
                return Global.user_map[appId]

        except Exception as e:
            return JsonResponse.getErrorResponse(message=f"Error in checkUserAlreadyExistOrNot {e}", code=400)


    #
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
    #         response_list = [await div.inner_text() for div in await page.query_selector_all("div.prose")]
    #
    #         return response_list
    #     except Exception as e:
    #         return {"error": str(e)}
    # geonodeList = cls.getProxyListFromGeonode()
    # sorted_data = sorted(geonodeList.data, key=lambda datum: datum.speed)
    # if len(Global.user_map.values()) >= 1:
    #     userObject = None
    #     for geonodeObject in geonodeList.data:
    #
    #         for getUser in Global.user_map.values():
    #             if getUser.proxyIP != geonodeObject.ip and geonodeObject.speed <= 7:
    #                 webDriver = WebDriverHandler(ip=geonodeObject.ip, port=geonodeObject.port)
    #                 Global.user_map[appId] = User(appId, geonodeObject.ip,
    #                                               webDriver.initialize_chrome_driver(appId, webDriver.proxyIp,
    #                                                                                  webDriver.proxyPort
    #                                                                                  , geonodeObject.protocols[0].value))
    #                 isMatch = True
    #                 userObject = Global.user_map[appId]
    #                 break
    #         if isMatch:
    #             break
    #
    # else:
    #     if sorted_data[0].speed <= 7:
    #         webDriver = WebDriverHandler(ip=sorted_data[0].ip, port=sorted_data[0].port)
    #         Global.user_map[appId] = User(appId, sorted_data[0].ip,
    #                                       webDriver.initialize_chrome_driver(appId, webDriver.proxyIp,
    #                                                                          webDriver.proxyPort,
    #                                                                          sorted_data[0].protocols[0].value))
    #         isMatch = True
    #         userObject = Global.user_map[appId]

    # if not isMatch:
    #     raise Exception(JsonResponse.getErrorResponse("No Server Found", 500))

    # else:
    #     return userObject

    # # Define the function to call the external API
    # @classmethod
    # def getProxyListFromGeonode(cls):
    #     url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
    #     try:
    #         httpRequestHandler = HttpRequestHandler(url)
    #         response = httpRequestHandler.getRequest()
    #         if response:
    #             # Create an instance of MyModel using the parsed data
    #             return JsonParser.parse_geonode_proxy_servers(response)
    #
    #     except Exception as e:
    #         # Handle exceptions such as connection errors or timeouts
    #         with open("GeneralException.txt", "a") as f:
    #             current_datetime = datetime.now()
    #             f.write(f"{current_datetime}: Exception in getProxyListFromGeonode(): {e}\n")
    #         raise Exception(JsonResponse.getErrorResponse("Something went wrong", 500))
