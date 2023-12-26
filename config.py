import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 10215855))

    API_HASH = os.environ.get("API_HASH", "c6eac883d0f3124c86408a907bdde463)
