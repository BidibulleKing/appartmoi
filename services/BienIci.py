from services.Advertiser import Advertiser

class BienIci (Advertiser):
    def __init__(self, url):
        super().__init__(name='bienici', url=url)

    def get_links(self):
        linkClass = 'detailedSheetLink'
        titleClass = 'ad-overview-details__ad-title--small'
        agreeButtonId = 'didomi-notice-agree-button'

        try:
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)

            try:
                agreeButton = self.driver.find_element(self.By.ID, agreeButtonId)
                agreeButton.click()
            except self.NoSuchElementException:
                print("Agree button not found")
                self.driver.quit()

            links = self.driver.find_elements(self.By.CLASS_NAME, linkClass)

            return [{'link': link.get_attribute('href'), 'title': link.find_element(self.By.CLASS_NAME, value=titleClass).text} for link in links]

        except Exception as e:
            print("An error occurred: ", e)
            self.driver.quit()