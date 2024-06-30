from services.Advertiser import Advertiser

class Pap (Advertiser):
    def __init__(self, url):
        super().__init__(name='pap', url=url)

    def get_links(self):
        linkClass = 'item-title'
        disagreeButtonParentSpanClass = 'sd-cmp-3jRLA'
        disagreeButtonClass = 'button.sd-cmp-1bquj'

        try:
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)

            try:
                disagreeButtonParentSpan = self.driver.find_element(self.By.CLASS_NAME, disagreeButtonParentSpanClass)
                disagreeButton = disagreeButtonParentSpan.find_element(self.By.CSS_SELECTOR, disagreeButtonClass)
                disagreeButton.click()
            except self.NoSuchElementException:
                print("Disagree button not found")
                self.driver.quit()

            links = self.driver.find_elements(self.By.CLASS_NAME, linkClass)

            return [{'link': link.get_attribute('href'), 'title': link.find_element(self.By.CSS_SELECTOR, 'span.h1').text} for link in links]

        except Exception as e:
            print("An error occurred: ", e)
            self.driver.quit()