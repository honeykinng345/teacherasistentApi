class ServerProxy:
    def __init__(self, timeDate, ip: str, port: str):
        self.currentTime = timeDate
        self.ip = ip
        self.port = port
        self.userName = "dqdiwdox"
        self.password = "ygum4xbnrh62"

    def __repr__(self):
        return f"User(name={self.ip}, age={self.port})"
