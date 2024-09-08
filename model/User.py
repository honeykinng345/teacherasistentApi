from playwright.async_api import Browser, Page, BrowserContext


class User:
    webDriverHandler: Browser
    webDriverPage: Page
    webDriverContext: BrowserContext
    response: dict

    def __init__(self, uid, proxyIP, webDevBrowser,webPage,webContext):
        self.userId = uid
        self.proxyIP = proxyIP
        self.webDriverHandler = webDevBrowser
        self.webDriverPage = webPage
        self.webDriverContext = webContext

