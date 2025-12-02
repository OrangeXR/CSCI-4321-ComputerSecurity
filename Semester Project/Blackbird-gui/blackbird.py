import os
import argparse
import logging
import sys
import random
from datetime import datetime
from rich.console import Console

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import config
from modules.whatsmyname.list_operations import checkUpdates
from modules.core.username import verifyUsername
from modules.core.email import verifyEmail
from modules.utils.userAgent import getRandomUserAgent
from modules.export.file_operations import createSaveDirectory
from modules.export.csv import saveToCsv
from modules.export.pdf import saveToPdf
from modules.export.json import saveToJson
from modules.utils.file_operations import isFile, getLinesFromFile
from modules.utils.permute import Permute
from dotenv import load_dotenv

load_dotenv()


def initiate():
    """Initialize logging, config, and environment variables."""
    if not os.path.exists("logs/"):
        os.makedirs("logs/")
    logging.basicConfig(
        filename=config.LOG_PATH,
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    config.console = Console()
    config.dateRaw = datetime.now().strftime("%m_%d_%Y")
    config.datePretty = datetime.now().strftime("%B %d, %Y")
    config.userAgent = getRandomUserAgent(config)

    # Initialize defaults for attributes normally set by argparse
    config.username = None
    config.username_file = None
    config.permute = False
    config.permuteall = False
    config.csv = False
    config.pdf = False
    config.json = False
    config.filter = None
    config.no_nsfw = False
    config.dump = False
    config.proxy = None
    config.verbose = False          # <-- added default
    config.ai = False
    config.setup_ai = False
    config.timeout = 30
    config.max_concurrent_requests = 30
    config.email = None
    config.email_file = None
    config.no_update = False
    config.about = False

    config.usernameFoundAccounts = None
    config.emailFoundAccounts = None
    config.currentUser = None
    config.currentEmail = None

    lines = getLinesFromFile("assets/text/splash.txt")
    config.splash_line = random.choice(lines) if lines else ""


def run_blackbird_search(username=None, email=None):
    """
    Run Blackbird search for a username or email.
    Returns a list of found accounts (dicts with 'name', 'url', 'status').
    """
    initiate()
    results = []

    if username:
        config.username = [username]
        config.currentUser = username
        verifyUsername(config.currentUser, config)
        if config.usernameFoundAccounts:
            results = config.usernameFoundAccounts

    if email:
        config.email = [email]
        config.currentEmail = email
        verifyEmail(config.currentEmail, config)
        if config.emailFoundAccounts:
            results = config.emailFoundAccounts

    return results


def cli_main():
    """Original CLI entry point, preserved for command-line use."""
    parser = argparse.ArgumentParser(
        prog="blackbird",
        description="An OSINT tool to search for accounts by username in social networks.",
    )
    parser.add_argument("-u", "--username", nargs="*", type=str)
    parser.add_argument("-e", "--email", nargs="*", type=str)
    args = parser.parse_args()

    initiate()

    if args.username:
        for user in args.username:
            config.currentUser = user
            verifyUsername(config.currentUser, config)
            if config.usernameFoundAccounts:
                config.console.print(config.usernameFoundAccounts)

    if args.email:
        for mail in args.email:
            config.currentEmail = mail
            verifyEmail(config.currentEmail, config)
            if config.emailFoundAccounts:
                config.console.print(config.emailFoundAccounts)


if __name__ == "__main__":
    cli_main()
