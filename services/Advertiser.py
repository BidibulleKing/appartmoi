class Advertiser:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def get_name(self):
        return self.name
    
    def get_url(self):
        return self.url

    def set_name(self, name):
        self.name = name

    def set_url(self, url):
        self.url = url

    def set_selenium_dependencies(self, driver, By, NoSuchElementException):
        self.driver = driver
        self.By = By
        self.NoSuchElementException = NoSuchElementException