# SportyBet Web Scraper with Python: Automate Betting Data Extraction

This Python script automates the extraction of soccer betting data from **SportyBet**. It scrapes match times, team names, and betting odds (home, draw, away) from the SportyBet website, providing a quick and efficient way to gather betting data for further analysis.

## 📌 Features

- **Automated Betting Data Scraping**: Extracts match times, teams, and odds from SportyBet’s soccer section.
- **CSV Output**: Saves the data into a CSV file for easy access and analysis.
- **Headless Browser**: Runs in a headless mode (no GUI), making the scraping process more efficient.
- **Handles Pagination**: Automatically navigates through pages to capture all available matches.
- **Duplicate Removal**: Detects and removes duplicate records to maintain clean datasets.

## 🚀 How It Works

The scraper visits the SportyBet football betting page, extracts soccer match details, and saves the data in a structured CSV format. The script scrolls through the available matches and clicks the "Next" button to ensure all available matches are scraped.

### Key Steps:

1. **Headless Browser Setup**: The script uses a headless Selenium browser to navigate the SportyBet website.
2. **Scroll and Click**: It scrolls to load more matches and clicks the "Next" button to navigate through pages.
3. **Data Scraping**: Using `BeautifulSoup` and `lxml`, the script extracts match times, home/away teams, and betting odds.
4. **Data Storage**: The scraped data is saved as a CSV file for easy access and analysis.
5. **Duplicate Handling**: Ensures no duplicate records in the final output file.

## 🛠️ Requirements

Before running the script, ensure the following packages are installed:

- **Python 3.x**
- **Selenium**
- **BeautifulSoup4**
- **lxml**
- **pandas**
- **ChromeDriver** (or the appropriate driver for your browser)

Install the required packages using pip:
```bash
pip install selenium beautifulsoup4 lxml pandas
```

## 🏃 How to Run the Script

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ezee-Kits/SportyBet-Web-Scraper.git
   ```

2. **Set up ChromeDriver**:  
   Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for your browser. Ensure the ChromeDriver is in your system path.

3. **Run the Python Script**:
   ```bash
   python sportybet_scraper.py
   ```

4. **View Results**:  
   The scraped data will be saved as `SPORTYBET.csv` in the specified directory.

## 📁 Output

The output CSV file (`SPORTYBET.csv`) contains the following fields:
- **TIME**: The match time.
- **HOME TEAM**: The home team in the match.
- **AWAY TEAM**: The away team in the match.
- **HOME ODD**: Odds for the home team to win.
- **DRAW ODD**: Odds for a draw.
- **AWAY ODD**: Odds for the away team to win.
- **BOOKMAKER**: The bookmaker name (SportyBet).

## 🔧 Future Improvements

- **Expand to Other Sports**: Scrape data from other sports like basketball or tennis.
- **Error Handling**: Add more robust error handling for page load issues or website changes.
- **Enhance Efficiency**: Improve the script’s speed by optimizing scrolling and data extraction techniques.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing

Feel free to contribute by opening issues, suggesting improvements, or submitting pull requests. All feedback is welcome!
