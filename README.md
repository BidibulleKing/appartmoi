# BienIci & PAP - Apartment Scraper

This project is a Python-based web scraper designed to collect apartment listings from various real estate websites. Currently, it supports scraping from BienIci and PAP. The scraper uses Selenium for navigating and extracting data from these websites. Collected data can be saved locally and pushed to a Trello board for easy tracking and management.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Docker
- [Selenium Standalone Server](https://hub.docker.com/r/selenium/standalone-chrome) for Docker
- A Trello account for integration

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages.
3. Copy `settings.example.json` to `settings.json` and fill in your details:

- Trello API key, token and list ID for integration.
- URLs for BienIci and PAP with your search criteria.

### Usage

Run the scraper with the following command:

```sh
python app.py
```

Follow the on-screen prompts to choose the advertiser you wish to scrape. The scraper will collect the listings and save them to `data.json`. If configured, new listings will be pushed to the specified Trello board.

## Features

- Supports scraping from BienIci and PAP.
- Saves scraped data locally in JSON format.
- Integrates with Trello to push new listings for easy tracking.
- Utilizes Selenium WebDriver for robust web navigation and data extraction.

## Configuration

Edit `settings.json` to configure the scraper:

- **Trello**: Fill in your API key, token and list ID to enable Trello integration.
- **BienIci and PAP**: Set the URLs with you search criteria for each advertiser.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems.

## License

Distributed under the MIT License. See `LICENSE` for more information.
