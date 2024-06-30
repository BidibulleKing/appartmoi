from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from DataManager import DataManager
from services.BienIci import BienIci
from services.Pap import Pap

import requests
import json

def init():
    data_structure = '''{
                "bienici": {
                    "listing": []
                },
                "pap": {
                    "listing": []
                }
            }'''

    # if data.json does not exist, create it
    try:
        with open('data.json', 'r') as file:
            pass
    except FileNotFoundError:
        with open('data.json', 'w') as file:
            file.write(data_structure)

    # if old_links.json does not exist, create it
    try:
        with open('old_links.json', 'r') as file:
            pass
    except FileNotFoundError:
        with open('old_links.json', 'w') as file:
            file.write(data_structure)

def push_to_trello(links: list):
    settings = json.load(open('settings.json'))
    headers = {
        'Content-Type': 'application/json'
    }

    for link in links:
        query = {
            'key': settings['trello']['key'],
            'token': settings['trello']['token'],
            'idList': settings['trello']['idList'],
            'name': link.get('title'),
            'desc': link.get('url')
        }

        response = requests.request("POST", url=settings['trello']['url'], params=query, headers=headers)

        if response.status_code == 200:
            print("Link added to Trello")
        else:
            print("An error occurred: ", response.text)

def prompt_user():
    print("Apartment Scraper")
    print("Choose an advertiser to scrape")
    print("1. BienIci")
    print("2. PAP")

    choice = input("Enter the number of the advertiser: ")

    if choice == '1':
        print("Scraping BienIci")
        with open('settings.json', 'r') as file:
            url = json.load(file).get('bienici').get('url')
            advertiser = BienIci(url=url)
    elif choice == '2':
        print("Scraping PAP")
        with open('settings.json', 'r') as file:
            url = json.load(file).get('pap').get('url')
            advertiser = Pap(url=url)
    else:
        print("Invalid choice")
        prompt_user()

    return advertiser

def main():
    init()

    advertiser = prompt_user()
    advertiser_name = advertiser.get_name()

    webdriver_url = 'http://localhost:4444'
    driver = webdriver.Remote(command_executor=webdriver_url, options=webdriver.ChromeOptions(), keep_alive=False)
    advertiser.set_selenium_dependencies(driver, By, NoSuchElementException)

    links = advertiser.get_links()

    driver.quit()

    if links:
        data_manager = DataManager(links=links, advertiser_name=advertiser_name, json=json)
        data_manager.save_data()
    
    with open('data.json', 'r') as file:
        data = json.load(file)

        if data[advertiser_name]['listing']:
            push_to_trello(data[advertiser_name]['listing'])
        else:
            print("No new links to push to Trello")

    exit()

main()