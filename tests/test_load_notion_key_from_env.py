import os

from dotenv import load_dotenv
from notion_client import Client
from notion_client.helpers import collect_paginated_api

load_dotenv()


def test_load_notion_key_from_env():
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    assert notion is not None
