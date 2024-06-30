class DataManager:
    def __init__(self, links: list, advertiser_name: str, json):
        self.links = links
        self.advertiser_name = advertiser_name
        self.json = json

    def save_old_data(self):
        with open('old_links.json', 'r') as file:
            data = self.json.load(file)
            old_links = data.get(self.advertiser_name).get('listing')

        # get links that are not already in the old links
        new_links = [link for link in self.links if link['link'] not in [item['url'] for item in old_links]]
        del old_links

        with open('old_links.json', 'w') as file:
            for link in new_links:
                data.get(self.advertiser_name).get('listing').append({'url': link['link'], 'title': link['title']})

            self.json.dump(data, file, indent=4)

    def save_data(self):
        with open('data.json', 'r') as file:
            data = self.json.load(file)
        
        with open('old_links.json', 'r') as file:
            old_links = self.json.load(file).get(self.advertiser_name).get('listing')
            new_links = [link for link in self.links if link['link'] not in [item['url'] for item in old_links]]
            del old_links

        with open('data.json', 'w') as file:
            data.get(self.advertiser_name).get('listing').clear()

            for link in new_links:
                data.get(self.advertiser_name).get('listing').append({'url': link['link'], 'title': link['title']})
            
            self.json.dump(data, file, indent=4)
        
        self.save_old_data()