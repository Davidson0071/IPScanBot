import requests

import json

import telebot

bot = telebot.TeleBot('YOUR_API_TOKEN_HERE')

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):

    bot.reply_to(message, "Welcome to Proxy Checker Bot! Please send me a proxy in the format 'IP:PORT'.")

@bot.message_handler(func=lambda message: True)

def check_proxy(message):

    proxy = message.text.strip()

    # Call ipinfo.io API to get IP address details

    url = f"https://ipinfo.io/{proxy}/json"

    response = requests.get(url)

    # Check if the API call was successful

    if response.status_code == 200:

        data = json.loads(response.text)

        # Check if the IP address is valid

        if "ip" in data:

            # Extract the IP address details

            ip = data["ip"]

            city = data["city"] if "city" in data else ""

            region = data["region"] if "region" in data else ""

            country = data["country"] if "country" in data else ""

            postal = data["postal"] if "postal" in data else ""

            timezone = data["timezone"] if "timezone" in data else ""

            org = data["org"] if "org" in data else ""

            host = data["hostname"] if "hostname" in data else ""

            # Format the details with emojis and send the result back to the user

            result = f"✅ Valid proxy:\n\n🌐 IP address: {ip}\n🏙️ City: {city}\n🌍 Region: {region}\n🌎 Country: {country}\n📭 Postal code: {postal}\n🕰️ Timezone: {timezone}\n🏢 Organization: {org}\n🌐 Hostname: {host}"

            bot.reply_to(message, result)

        else:

            bot.reply_to(message, "❌ Invalid proxy. Please send me a valid proxy in the format 'IP:PORT'.")

    else:

        bot.reply_to(message, f"❌ Error checking proxy: {response.text}")

bot.polling()

