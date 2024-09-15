# Random Facts Bot

## Overview

The **Random Facts Bot** is a Telegram bot that provides users with interesting random facts. Users can interact with the bot by sending commands to receive a fact and can opt to receive more facts or stop at any time. The bot is built using the `pyTelegramBotAPI` library (also known as `telebot`) and is fully capable of handling commands, user responses, and certain content types like documents and audio.

## Features

- Sends a random fact from a predefined list.
- Users can request additional facts or choose to stop receiving them.
- Responds to basic commands like `/start` and `/help`.
- Handles invalid inputs gracefully.
- Provides warnings when audio or document files are sent.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- `pyTelegramBotAPI` library installed. You can install it via pip:

  ```bash
  pip install pyTelegramBotAPI
