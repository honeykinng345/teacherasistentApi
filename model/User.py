from datetime import datetime

from playwright.async_api import Browser, Page, BrowserContext


class User:

    def __init__(self, uid, proxyIP, webDevBrowser, webPage, webContext, dateTime: datetime,firstAttempt: bool):
        self.userId = uid
        self.proxyIP = proxyIP
        self.webDriverHandler = webDevBrowser
        self.webDriverPage = webPage
        self.webDriverContext = webContext
        self.dateTime = dateTime
        self.fistTime = firstAttempt
