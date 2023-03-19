import datetime
import os
import re

from dotenv import load_dotenv
from notion_client import Client
from notion_client.helpers import collect_paginated_api

load_dotenv()
notion = Client(auth=os.environ["NOTION_TOKEN"])


def _extract_properties_from_page(notion_page):
    """
    Return properties dict from a page dict, but first
    clean fields that need to be nullified for a new page.
    """

    properties = notion_page["properties"]

    # delete fields that need to be nullified for a new page
    if notion_page.get("properties").get("Created time"):
        del properties["Created time"]

    return properties


def add_ndays_to_datestring(datestring, days=7):
    """
    Add n days to a datestring in the format "2021-01-01".
    """
    date = datetime.datetime.strptime(datestring, "%Y-%m-%d")
    date_plus_n_days = date + datetime.timedelta(days=days)
    return date_plus_n_days.strftime("%Y-%m-%d")


def add_new_weekly_page(database_id, num_new_weeks=1):
    """
    Add a new weekly page to the database.
    """
    weekly_pages = collect_paginated_api(
        notion.databases.query, database_id=database_id
    )

    for i in range(1, num_new_weeks + 1):
        properties_dict = _extract_properties_from_page(weekly_pages[0])

        props_to_copy = {
            "Date": properties_dict["Date"],
            "Week Title": properties_dict["Week Title"],
        }

        new_start_date = add_ndays_to_datestring(
            properties_dict["Date"]["date"]["start"], days=7
        )
        new_start_date_formatted = datetime.datetime.strptime(
            new_start_date, "%Y-%m-%d"
        ).strftime("%b %d")

        new_end_date = add_ndays_to_datestring(
            properties_dict["Date"]["date"]["end"], days=7
        )
        new_end_date_formatted = datetime.datetime.strptime(
            new_end_date, "%Y-%m-%d"
        ).strftime("%b %d")

        props_to_copy["Date"]["date"]["start"] = new_start_date
        props_to_copy["Date"]["date"]["end"] = new_end_date

        new_week_title = f"<< {new_start_date_formatted} - {new_end_date_formatted}"

        props_to_copy["Week Title"]["title"][0]["plain_text"] = new_week_title
        props_to_copy["Week Title"]["title"][0]["text"]["content"] = new_week_title

        notion.pages.create(
            parent={"database_id": database_id},
            properties=props_to_copy,
        )

