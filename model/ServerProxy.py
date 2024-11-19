class ServerProxy:
    def __init__(self, timeDate, ip: str, port: str,speed_category, response_time):
        self.currentTime = timeDate
        self.ip = ip
        self.port = port
        self.userName = "6e4162a6906dc79e20fa"
        self.password = "33e81c17912ec20d"
        self.speed_category = speed_category
        self.response_time = response_time

    def __repr__(self):
        return f"User(name={self.ip}, age={self.port})"
