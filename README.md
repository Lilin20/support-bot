# Support-Bot

This bot manages support tickets and role management. It is made for the TBS1-Community Discord. 

## Table of Contents
- [Support-Bot](#support-bot)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contact](#contact)

## Installation

Follow these steps if you want to deploy the bot on your server:

1. Install Python-Packages
    ```shell
    pip install py-cord
    pip install configparser
    ```
2. Download the bot files
   ```shell
   git clone https://github.com/Lilin20/support-bot.git
   ```
3. Edit the 'config.ini' file
   ```ini
   [Bot]
   token=<BOT_TOKEN> # Insert your bot token.
   ```
4. Start the bot
   ```shell
   python3 main.py
   ```

## Usage

- /create_support_embed
  - Creates the embed and the view for the support system.
    - This will send an embed with 2 buttons (the view with the buttons is persistent).
      - After clicking a button, a modal (form) will open.
    - Admin permission is needed.

- /create_role_selection
  - Creates the embed for the role selection information.
  - Admin permission is needed.  

- /select_role
  - Creates the embed and the view for the role selection.
    - This will send an embed with 2 selectors (the view with the selectors is persistent).
      - After choosing a role, all selectors will be disabled.

## Contact

Any questions? Feel free to DM me on discord.

Discord: illnesslilin
