import requests
from twilio.rest import Client

STOCK_NAME = "BTC"
COMPANY_NAME = "Bitcoin"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "M2FZ96LEIIF0W4SO"  # TODO Create a Environment Variable
NEWS_API_KEY = "d927f41bf1344eca916ebca46d1c54c0" # TODO Create a Environment Variable
TWILIO_SID = "ACf6cb7d1a8260df02875af7cb23c4676a"
TWILIO_AUTH_TOKEN = "db9d18e9df047ee6bd6e80ff72ae9f22"
TWILIO_PHONE_NUMBER = "+18593748175"
MY_PHONE_NUMBER = "+5515998025147"

# Get yesterday's closing stock price.
stock_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": STOCK_NAME,
    "market": "USD",
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Digital Currency Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4b. close (USD)"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
before_yesterday_closing_price = day_before_yesterday_data["4b. close (USD)"]
print(yesterday_closing_price)
print(before_yesterday_closing_price)

# Find the positive difference between 1 and 2.
difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)
print(diff_percent)

# Use the News API to get articles related to the COMPANY_NAME.
news_params = {
    "q": "bitcoin",
    "apiKey": "d927f41bf1344eca916ebca46d1c54c0",
}
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]
# Use Python slice operator to create a list that contains the first 3 articles.
three_articles = articles[:3]

# Create a new list of the first 3 articles headline and description using list comprehension.
formatted_articles = [f"\n\n{STOCK_NAME}: {up_down}{diff_percent}%\nTítulo: {article['title']}. \n\nDescrição: {article['description']}" for article in three_articles]

# Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(body=article, from_="+18593748175", to="+5515998025147")

