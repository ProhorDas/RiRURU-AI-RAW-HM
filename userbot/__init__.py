# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """

import os
import platform
import re
import time
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from .storage import Storage
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
from git import Repo
from platform import python_version, uname
from telethon import __version__, version

load_dotenv("config.env")

STORAGE = (lambda n: Storage(Path("data") / n))

StartTime = time.time()

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get(
    "CONSOLE_LOGGER_VERBOSE") or "False")

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info(
        "You MUST have a python version of at least 3.8."
        "Multiple features depend on this. Bot quitting."
    )
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = (os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________") or None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY") or None
API_HASH = os.environ.get("API_HASH") or None


# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION") or None

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN") or None

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID") or 0)

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG") or "True")
if BOTLOG:
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER") or "True")
else:
    LOGSPAMMER = True

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN") or "False")

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ") or "False")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME") or None
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY") or None

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME") or None
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN") or None

# Custom (forked) repo URL and BRANCH for updater.
UPSTREAM_REPO_URL = (os.environ.get("UPSTREAM_REPO_URL")
                     or "https://github.com/PrajjuS/ProjectFizilion.git")
UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH") or "Demon"

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get(
    "CONSOLE_LOGGER_VERBOSE") or "False")

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL") or None

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY") or None

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY") or None

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or None
GOOGLE_CHROME_BIN = "/usr/bin/chromium"

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID") or None
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY") or None
WEATHER_DEFLANG = os.environ.get("WEATHER_DEFLANG") or None

# Genius lyrics API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN") or None

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID") or None

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT") or "False")
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT") or "False")

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME") or None

# Default .alive logo
ALIVE_LOGO = str(os.environ.get("ALIVE_LOGO") or "https://github.com/ElytrA8/ProjectFizilion/raw/dragon/resources/glitch.gif")
# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY") or "")
TZ_NUMBER = int(os.environ.get("TZ_NUMBER") or 1)

# Version of One4uBot
USERBOT_VERSION = os.environ.get("USERBOT_VERSION") or "1.1"

# User Terminal alias
USER_TERM_ALIAS = os.environ.get("USER_TERM_ALIAS") or "drag0n"

# Updater alias
UPDATER_ALIAS = os.environ.get("UPDATER_ALIAS") or "Fizilion"

# Zipfile module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY") or "./zips"

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME") or "True")

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX") or None
DEFAULT_BIO = os.environ.get("DEFAULT_BIO") or None

LASTFM_API = os.environ.get("LASTFM_API") or None
LASTFM_SECRET = os.environ.get("LASTFM_SECRET") or None
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME") or None
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD") or None
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API is not None:
    lastfm = LastFMNetwork(
        api_key=LASTFM_API,
        api_secret=LASTFM_SECRET,
        username=LASTFM_USERNAME,
        password_hash=LASTFM_PASS,
    )
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA") or None
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID") or None
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET") or None
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA") or None
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID") or None
TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TMP_DOWNLOAD_DIRECTORY") or "./downloads/"

# Uptobox
USR_TOKEN = os.environ.get("USR_TOKEN_UPTOBOX", None)

#SourceForge
SFUSER = os.environ.get("SFUSER") or "null"
SFPASS = os.environ.get("SFPASS") or "null"
SFDIR = os.environ.get("SFDIR") or "null"

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


async def check_botlog_chatid():
    if not BOTLOG:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file."
        )
        quit(1)


async def send_alive_status():
    if BOTLOG_CHATID and LOGSPAMMER:
        DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
        repo = Repo()
        modules = CMD_HELP
        uptime = await get_readable_time((time.time() - StartTime))
        output = (
            "` =============================== `\n"
            f"`Fizilion is Up [Premium Edition] `\n"
            f"`=============================== `\n"
            f"•`Telethon       : v{version.__version__} `\n"
            f"•`Python         : v{python_version()} `\n"   
            f"•`User           : {DEFAULTUSER} `\n"
            f"•`Running on     : {repo.active_branch.name} `\n"
            f"•`Loaded modules : {len(modules)} `\n"
            f"•`Fizilion       : {USERBOT_VERSION} `\n"
            f"•`Bot Uptime     : {uptime} `\n"
        )
        await bot.send_message(BOTLOG_CHATID, output)
        return True


with bot:
    try:
        bot.loop.run_until_complete(send_alive_status())
    except:
        pass


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ZALG_LIST = {}
ISAFK = False
AFKREASON = None
DELMSG = False
