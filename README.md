# ResumeSenderBot

ResumeSenderBot is an automated tool designed to streamline the job application process by sending resumes directly to hiring managers' email addresses. Additionally, the bot can search for email IDs within Telegram chats, making it easier to target relevant contacts.

## Features

- Automated Resume Sending: Send your resume directly to the hiring manager's email.
- Email Extraction from Telegram: Automatically extract email addresses from Telegram chat logs.
- Customizable Templates: Customize the email content and subject line.
- Error Handling: Robust error handling to manage failed attempts and retries.
- Logging: Logs activities for tracking purposes and future references.

## Tech Stack

- Python: Core programming language for the bot.
- Telegram API: For accessing and extracting emails from Telegram chats.
- SMTP (Simple Mail Transfer Protocol): For sending emails.
- Regex: Employed to identify and extract email addresses from Telegram chats.
- ConfigParser: For managing configurations like email credentials and Telegram API keys.

## Setup Instructions

### Prerequisites

- Python 3.7+
- A valid Gmail account (or another SMTP-compatible email account)
- Telegram API credentials
- Required Python packages (listed in requirements.txt)

### Installation

1. Clone the repository:
   git clone https://github.com/shank250/resumeSenderBot.git
   cd resumeSenderBot

2. Install the required packages:
   pip install -r requirements.txt

3. Set up environment variables or update the config.ini file with your credentials:

   .env:

   [EMAIL]  
   EMAIL_ID = your_email@gmail.com  
   PASSWORD = your_password  

   [TELEGRAM]  
   API_ID = your_api_id  
   API_HASH = your_api_hash  

4. Run the bot:
   python main.py

## Usage

1. Ensure that your Telegram account has access to the necessary chats from which you want to extract emails.
2. Customize your email content by modifying the email_template.txt file.
3. Run the bot and watch it automatically send resumes to the extracted email addresses.

## Project Structure

resumeSenderBot/  
├── main.py               # Entry point for the bot  
├── email_sender.py       # Handles email sending logic  
├── telegram_scraper.py   # Handles Telegram chat scraping  
├── .env            # Configuration file for credentials  
├── email_template.txt    # Template for the email content  
├── requirements.txt      # Python dependencies  
└── README.md             # Project documentation (this file)  

## Contributing

We welcome contributions! Please check the issues for open bugs or feature requests. Feel free to fork this project and make your changes.

1. Fork the project
2. Create your feature branch: git checkout -b feature/YourFeature
3. Commit your changes: git commit -m 'Add some feature'
4. Push to the branch: git push origin feature/YourFeature
5. Open a pull request

## License

This project is licensed under the GNU License - see the LICENSE file for details.

## Contact

For any inquiries or issues, feel free to reach out to the project maintainers.

---

Happy Coding!
