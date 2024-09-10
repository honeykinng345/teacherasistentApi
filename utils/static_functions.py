import time
from datetime import datetime, timedelta
from random import random
from typing import List
from apscheduler.schedulers.background import BackgroundScheduler


import requests
from requests.auth import HTTPProxyAuth

from model import User
from model.ServerProxy import ServerProxy
from utils.global_objects import Global


class StaticFunctions:
    workingProxyList: List[ServerProxy] = []
    scheduler = BackgroundScheduler()

    proxy_list = [
        "38.154.227.167:5868:dqdiwdox:ygum4xbnrh62",
        "45.127.248.127:5128:dqdiwdox:ygum4xbnrh62",
        "64.64.118.149:6732:dqdiwdox:ygum4xbnrh62",
        "167.160.180.203:6754:dqdiwdox:ygum4xbnrh62",
        "166.88.58.10:5735:dqdiwdox:ygum4xbnrh62",
        "173.0.9.70:5653:dqdiwdox:ygum4xbnrh62",
        "45.151.162.198:6600:dqdiwdox:ygum4xbnrh62",
        "204.44.69.89:6342:dqdiwdox:ygum4xbnrh62",
        "173.0.9.209:5792:dqdiwdox:ygum4xbnrh62",
        "206.41.172.74:6634:dqdiwdox:ygum4xbnrh62"
    ]

    test_url = "https://www.google.com/"

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
                response = requests.get(cls.test_url, proxies=proxies, auth=auth, timeout=8)
                if response.status_code == 200:
                    serverProxyInfo = ServerProxy(datetime.now(), ip, port)
                    cls.workingProxyList.append(serverProxyInfo)
                    print(f"Working: {proxy}")
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
                del Global.user_map[user_key]  # Remove user from the dictionary

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





