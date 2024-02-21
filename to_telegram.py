import os
import requests
from dotenv import load_dotenv


load_dotenv()

# Get bot token and channel ID from environment variables
bot_token = os.getenv('TELEGRAM_API_TOKEN')
chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

# Specify the file path to the log file
file_path = "requirements.txt"# iam sending requirements.txt for demo

# Prepare the message parameters
url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
files = {'document': open(file_path, 'rb')}
params = {'chat_id': chat_id}

# Send the document
response = requests.post(url, params=params, files=files)

if response.status_code == 200:
    print("Document sent successfully!")
else:
    print(f"Failed to send document: {response.text}")

