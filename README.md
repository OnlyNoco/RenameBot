<div align="center">

# 🎬 RenameBot

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)](https://telegram.org)

A powerful Telegram bot that renames files, videos, and documents with custom thumbnails and advanced media processing capabilities.

[Features](#-features) • [Installation](#-installation) • [Configuration](#-configuration) • [Usage](#-usage) • [Deployment](#-deployment)

</div>

---

## 📋 Overview

**RenameBot** is a feature-rich Telegram bot designed to help users rename their media files effortlessly. With support for videos, documents, custom thumbnails, and quality optimization, this bot provides a seamless file management experience directly in Telegram.

Whether you need to rename files, compress thumbnails, or batch process media, RenameBot has you covered with an intuitive interface and powerful backend.

---

## ✨ Features

### 🎯 Core Features
- 📝 **File Renaming** - Rename videos and documents with custom names
- 🖼️ **Custom Thumbnails** - Set and manage custom thumbnail images
- 📥 **Media Processing** - Download, process, and upload files seamlessly
- ⚡ **Progress Tracking** - Real-time progress bars for all operations
- 🔐 **Secure Operations** - Safe file handling with automatic cleanup

### 🚀 Advanced Features
- 📊 **Batch Processing** - Process multiple files efficiently
- 🎨 **Thumbnail Optimization** - Automatic image compression and resizing
- 💾 **Smart Storage** - Temporary file management with auto-cleanup
- 🛠️ **Customizable Settings** - Configurable download directory and quality settings
- 📱 **User-Friendly Interface** - Intuitive inline buttons and clear instructions

### 🛡️ Administrator Tools
- `/start` - Check bot status and get started
- `/help` - View available commands and features
- `/report` - Report issues to the bot administrator
- `/stats` - View system statistics and resource usage

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Telegram Bot Token ([BotFather](https://t.me/botfather))
- Telegram API credentials ([my.telegram.org](https://my.telegram.org))
- MongoDB database ([MongoDB Cloud](https://www.mongodb.com/cloud)) - Optional

### Local Installation

1. **Clone the Repository**
```bash
git clone https://github.com/OnlyNoco/RenameBot.git
cd RenameBot
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure the Bot**
```bash
cp sample_config.py config.py
# Edit config.py with your credentials
```

4. **Run the Bot**
```bash
python main.py
```

---

## ⚙️ Configuration

### Environment Variables

Create a `config.py` file based on `sample_config.py` with the following variables:

| Variable | Type | Description |
|----------|------|-------------|
| `BOT_TOKEN` | string | Your Telegram bot token from BotFather |
| `API_ID` | integer | Telegram API ID from my.telegram.org |
| `API_HASH` | string | Telegram API Hash from my.telegram.org |
| `OWNER_ID` | integer | Your Telegram user ID (admin) |
| `WORKER` | integer | Number of worker threads (default: 4) |
| `PORT` | integer | Port for web server (default: 8080) |
| `DB_URL` | string | MongoDB connection URL |
| `DB_NAME` | string | MongoDB database name |
| `DOWNLOAD_DIR` | string | Directory for temporary downloads (default: ./downloads) |
| `START_MSG` | string | Custom welcome message |
| `ABOUT_MSG` | string | About bot message |
| `CMD_MSG` | string | Commands help message |
| `START_PIC` | list | URLs for start command media |

### Example Configuration
```python
BOT_TOKEN = "your_bot_token_here"
API_ID = 26254064
API_HASH = "your_api_hash_here"
OWNER_ID = 5296584067
WORKER = 4
PORT = 8080
DB_URL = "mongodb+srv://username:password@cluster.mongodb.net"
DB_NAME = "RenameBot"
DOWNLOAD_DIR = "./downloads"
```

---

## 📖 Usage

### User Commands

1. **Start the Bot**
   - Use `/start` to initiate the bot and see the welcome message

2. **Send a File**
   - Send a video or document file to the bot
   - The bot will ask for a custom filename

3. **Set Thumbnail**
   - Send an image to the bot in private chat
   - The bot will save it as your custom thumbnail

4. **Rename Files**
   - Send media with the custom thumbnail already set
   - Reply with the desired filename (without extension)
   - Choose between `document` or `video` format
   - The bot will process and send the renamed file

5. **Get Help**
   - Use `/help` to view all available commands
   - Use `/report` to report issues to the admin

### Example Workflow

```
1. /start                          → Bot sends welcome message
2. Send photo                       → Bot saves as thumbnail
3. Send video file                 → Bot asks for filename
4. Reply with "MyVideo"            → Bot asks for format
5. Click "Video" button            → Bot processes and sends file
```

---

## 📁 Project Structure

```
RenameBot/
├── main.py                 # Entry point and bot initialization
├── bot.py                  # Bot class and core configuration
├── config.py              # Configuration (create from sample_config.py)
├── sample_config.py       # Configuration template
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── Procfile              # Deployment configuration
├── LICENSE               # MIT License
├── README.md             # This file
│
├── database/
│   └── database.py       # MongoDB operations and user management
│
├── plugins/
│   ├── __init__.py       # Web server initialization
│   ├── route.py          # Web routing
│   ├── start.py          # Start command handler
│   ├── report.py         # Issue reporting
│   │
│   └── core/
│       ├── main_decorator.py     # Main file processing logic
│       ├── thumb.py              # Thumbnail management
│       ├── cleanup.py            # Temporary file cleanup
│       └── progressbar.py        # Progress bar utilities
│
└── thumbnails/           # User thumbnail storage directory
```

---

## 🔧 Technology Stack

- **[Pyrofork](https://github.com/Mayuri-Chan/pyrofork)** - Advanced Telegram client library
- **[Python 3.11+](https://www.python.org/)** - Core language
- **[MongoDB](https://www.mongodb.com/)** - User database
- **[PIL/Pillow](https://pillow.readthedocs.io/)** - Image processing
- **[aiohttp](https://docs.aiohttp.org/)** - Async HTTP server
- **[TgCrypto](https://github.com/pyrogram/tgcrypto)** - Fast encryption

---

## 🌐 Deployment

### 🐳 Docker Deployment

```bash
docker build -t renamebot .
docker run -e BOT_TOKEN="your_token" -e API_ID="your_id" \
  -e API_HASH="your_hash" -e OWNER_ID="your_id" renamebot
```

### ☁️ Heroku Deployment

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Click the button above
2. Fill in the environment variables
3. Deploy and monitor logs

### 🎯 Render Deployment

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://dashboard.render.com/new)

**Steps:**
1. Connect your GitHub repository
2. Select Python as runtime
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python main.py`
5. Add environment variables:
   - `BOT_TOKEN`
   - `API_ID`
   - `API_HASH`
   - `OWNER_ID`
   - `DB_URL`
   - `DB_NAME`
6. Deploy

### 🚀 Koyeb Deployment

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/apps/create?type=git)

**Steps:**
1. Click deploy button above
2. Connect your GitHub account
3. Select this repository
4. Configure environment variables:
   - `BOT_TOKEN` - Your Telegram bot token
   - `API_ID` - Telegram API ID
   - `API_HASH` - Telegram API Hash
   - `OWNER_ID` - Your Telegram user ID
   - `DB_URL` - MongoDB connection string
   - `DB_NAME` - Database name
   - `PORT` - Web server port (8080)
5. Click "Deploy" and wait for completion

### 💻 VPS/Local Deployment

**Requirements:**
- Linux VPS or Local Machine
- Python 3.11+
- MongoDB access

**Installation:**
```bash
# Clone repository
git clone https://github.com/OnlyNoco/RenameBot.git
cd RenameBot

# Install dependencies
pip3 install -U -r requirements.txt

# Configure
cp sample_config.py config.py
nano config.py  # Edit with your credentials

# Run bot
python3 main.py
```

**Using Systemd (for persistent running):**
```bash
sudo nano /etc/systemd/system/renamebot.service
```

Add:
```ini
[Unit]
Description=RenameBot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/RenameBot
ExecStart=/usr/bin/python3 /path/to/RenameBot/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then run:
```bash
sudo systemctl daemon-reload
sudo systemctl enable renamebot
sudo systemctl start renamebot
```

---

## 🐛 Troubleshooting

### Bot Not Responding
- Verify `BOT_TOKEN` is correct
- Check internet connection
- Ensure bot is running: `python main.py`
- Check logs for error messages

### File Download Issues
- Verify bot has enough disk space
- Check `DOWNLOAD_DIR` permissions
- Ensure MongoDB is connected

### Thumbnail Not Saving
- Send image as file, not as photo
- Ensure image file is under 5MB
- Check directory permissions for `thumbnails/`

### Database Connection Issues
- Verify `DB_URL` is correct and accessible
- Check MongoDB cluster IP whitelist
- Ensure network connectivity
- Test connection string with MongoDB Compass

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs via `/report` command
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📚 Improve documentation

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use privately
- ✅ Modify and distribute
- ✅ Host yourself

We only ask that you provide proper credit by linking to the original repository.

---

## 👨‍💻 Author & Credits

<div align="center">

### 🌟 **OnlyNoco**

**Portfolio:** [onlynoco.vercel.app](https://onlynoco.vercel.app)  
**Telegram:** [@OnlyNoco](https://t.me/OnlyNoco)  
**GitHub:** [github.com/OnlyNoco](https://github.com/OnlyNoco)

---

### 📢 **My Channels**

Join our community for more amazing bots and content:

- **🎬 [Battle Through The Heavens](https://t.me/HeavenlySubs)** - Anime streaming and updates
- **🔞 [Hentai Crisp](https://t.me/+O7PeEMZOAoMzYzVl)** - Adult anime content

---

### 🙏 **Special Thanks**

- [Mayuri-Chan](https://github.com/Mayuri-Chan) - Pyrofork Library
- [Lonami](https://github.com/Lonami) - PyroMod Extension
- [MongoDB](https://www.mongodb.com/) - Database Service

</div>

---

## 📞 Support

For issues, questions, or suggestions:

- **Use `/report` command** in the bot to report problems
- **Contact [@OnlyNoco](https://t.me/OnlyNoco)** on Telegram
- **Open an issue** on [GitHub](https://github.com/OnlyNoco/RenameBot/issues)
- **Join support group** for community help

---

<div align="center">

**[⬆ Back to Top](#-renamebot)**

Made with ❤️ by [OnlyNoco](https://github.com/OnlyNoco)

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?style=flat-square&logo=telegram)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?style=flat-square&logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>
