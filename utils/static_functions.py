import time
from datetime import datetime, timedelta
from enum import Enum
import random
from typing import List
from apscheduler.schedulers.background import BackgroundScheduler

import requests
from requests.auth import HTTPProxyAuth

from model import User
from model.ServerProxy import ServerProxy
from utils.global_objects import Global


# Enum for Speed Categories
class SpeedCategory(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class StaticFunctions:
    workingProxyList: List[ServerProxy] = [
        ServerProxy(datetime.now(), "gw.dataimpulse.com", '10058', speed_category="Heigh", response_time="123"),
        ServerProxy(datetime.now(), "gw.dataimpulse.com", '10000', speed_category="Heigh", response_time="123"),
        ServerProxy(datetime.now(), "gw.dataimpulse.com", '10041', speed_category="Heigh", response_time="123"),
        ServerProxy(datetime.now(), "gw.dataimpulse.com", '10039', speed_category="Heigh", response_time="123"),
        ServerProxy(datetime.now(), "gw.dataimpulse.com", '10012', speed_category="Heigh", response_time="123"),
        ServerProxy(datetime.now(), "gw.dataimpulse.com", '10013', speed_category="Heigh", response_time="123"),
        ServerProxy(datetime.now(), "gw.dataimpulse.com", '10014', speed_category="Heigh", response_time="123"),

    ]
    scheduler = BackgroundScheduler()

    proxy_list = [

        "gw.dataimpulse.com:10000:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10001:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10002:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10003:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10004:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10005:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10006:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10007:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10008:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10009:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10010:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10011:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10012:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10013:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10014:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10015:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10016:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10017:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10018:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10019:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10020:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10021:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10022:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10023:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10024:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10025:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10026:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10027:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10028:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10029:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10030:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10031:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10032:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10033:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10034:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10035:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10036:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10037:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10038:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10039:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10040:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10041:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10042:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10043:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10044:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10045:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10046:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10047:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10048:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10049:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10050:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10051:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10052:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10053:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10054:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10055:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10056:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10057:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10058:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10059:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10060:6e4162a6906dc79e20fa:33e81c17912ec20d",
        "gw.dataimpulse.com:10061:6e4162a6906dc79e20fa:33e81c17912ec20d"

    ]


    test_url = "https://api.ipify.org/"

    @classmethod
    def categorize_speed(cls, response_time):
        """Categorize speed based on response time."""
        if response_time < 1:
            return SpeedCategory.HIGH
        elif 1 <= response_time <= 3:
            return SpeedCategory.MEDIUM
        else:
            return SpeedCategory.LOW

    @classmethod
    def checkProxyServerWorkingOrNot(cls):
        cls.workingProxyList.clear()
        for proxy in cls.proxy_list:
            ip, port, username, password = proxy.split(':')
            proxy_url = f"http://{ip}:{port}"
            proxies = {
                "http": proxy_url,
            }
            auth = HTTPProxyAuth(username, password)
            try:
                start_time = datetime.now()  # Start time before request
                response = requests.get(cls.test_url, proxies=proxies, auth=auth, timeout=8)
                response_time = (datetime.now() - start_time).total_seconds()  # Calculate response time

                if response.status_code == 200:
                    speed_category = cls.categorize_speed(response_time)
                    serverProxyInfo = ServerProxy(datetime.now(), ip, port, speed_category=speed_category,
                                                  response_time=response_time)
                    cls.workingProxyList.append(serverProxyInfo)
                    print(f"Working: {proxy} Speed:{speed_category.name}")
                else:
                    print(f"Not Working: {proxy} (Status Code: {response.status_code})")
            except requests.RequestException as e:
                print(f"Not Working: {proxy} (Error: {e})")

    @classmethod
    def JobCheckUserSession(cls):
        current_time = datetime.now()

        # Iterate through a copy of the dict to avoid modifying it while iterating
        for user_key, user in list(Global.user_map.items()):
            # Calculate the difference
            time_diff = current_time - user.dateTime

            # Check if the difference is less than or equal to 15 minutes
            if time_diff <= timedelta(minutes=15):
                print(f"Removing user {user_key} from the session map due to inactivity.")
                user.webDriverContext.close()
                del Global.user_map[user_key]  # Remove user from the dictionary

    @classmethod
    def JobInteractWithWebPage(cls):

        # Iterate through a copy of the dict to avoid modifying it while iterating
        try:
            if len(Global.user_map.items()) > 0:
                for user_key, user in list(Global.user_map.items()):
                    page = user.webDriverPage

                    page.evaluate("window.scrollBy(0, 1000);")
                    time.sleep(1)
                    # Scroll up by 1000 pixels
                    page.evaluate("window.scrollBy(0, -1000);")
                    time.sleep(2)
                    print(f"Auto Interaction With Web Page {user.userId}")

        except Exception as e:
            print(f" Exception in : JobInteractWithWebPage \n {e}")

    @classmethod
    def get_random_high_speed_proxy(cls):
        # Separate proxies by speed category


        high_speed_proxies = [proxy for proxy in cls.workingProxyList if proxy.speed_category == SpeedCategory.HIGH]
        medium_speed_proxies = [proxy for proxy in cls.workingProxyList if
                                proxy.speed_category == SpeedCategory.MEDIUM]
        low_speed_proxies = [proxy for proxy in cls.workingProxyList if proxy.speed_category == SpeedCategory.LOW]


        # Try to get a random proxy, prioritizing high speed, then medium, and finally low
        if high_speed_proxies:
            return random.choice(high_speed_proxies)
        elif medium_speed_proxies:
            return random.choice(medium_speed_proxies)
        elif low_speed_proxies:
            return random.choice(low_speed_proxies)
        else:
            return None  # No working proxies available

    # Calculate the difference

    # @classmethod
    # def checkListLength(cls):
    #     print("Checking proxy server...")
    #     if len(cls.workingProxyList) > 0:
    #         print("Working proxy list found, adjusting interval to 3600 seconds.")
    #         cls.scheduler.modify_job('check_proxy', trigger='interval', seconds=3600)
    #     else:
    #         print("No proxies found, adjusting interval to 1 second.")
    #         cls.scheduler.modify_job('check_proxy', trigger='interval', seconds=1)
    #
    #     cls.checkProxyServerWorkingOrNot()


