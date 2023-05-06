# IPScanBot

IPScanBot is a Telegram bot that allows users to scan and check IP addresses for information such as location, ISP, and more. The bot is built using Python and the Telebot library.

## Features

- Check information for a single IP address

- Check information for multiple IP addresses in a text file

- Display information such as location, ISP, and more for each IP address

- Send results with emojis for easy interpretation

## Usage

To use IPScanBot, follow these steps:

1. Start a chat with the bot by searching for `@I_P_Scan_Bot` in Telegram or clicking on this link: http://t.me/I_P_Scan_Bot

2. Send an IP address to the bot in the format `xxx.xxx.xxx.xxx`, where each `x` is a number between 0 and 255. The bot will respond with information about the IP address.

3. To scan multiple IP addresses, upload a text file with one IP address per line. The bot will scan each IP address and send the results back in a formatted message.

4. For more information, send the `/help` command to the bot.

## Installation

To install and run IPScanBot locally, follow these steps:

1. Clone the GitHub repository: `git clone https://github.com/your-username/IPScanBot.git`

2. Navigate to the project directory: `cd IPScanBot`

3. Install the required packages: `pip install -r requirements.txt`

4. Create a new bot in Telegram and get the API token.

5. Create a `.env` file and add the following line: `API_TOKEN=<your_bot_api_token>`

6. Run the bot: `python main.py`

## Contributing

Contributions to IPScanBot are welcome! To contribute:

1. Fork the repository

2. Create a new branch: `git checkout -b my-new-feature`

3. Make changes and commit them: `git commit -am 'Add some feature'`

4. Push to the branch: `git push origin my-new-feature`

5. Submit a pull request

## Credits

IPScanBot was created by [David](https://github.com/Davidson0071) and is licensed under the [MIT License](https://opensource.org). 

The bot uses the [ipinfo.io API](https://ipinfo.io/) to retrieve information about IP addresses. 

## Disclaimer

This bot is provided for educational purposes only. The creator is not responsible for any misuse of the bot or any consequences that arise from using the bot.

