import datetime
import os
from copy import deepcopy

import pandas as pd
from dotenv import load_dotenv
from notion_client import Client
from notion_client.helpers import collect_paginated_api

load_dotenv()
notion = Client(auth=os.environ["NOTION_TOKEN"])


def _find_title_key_in_properties_dict(notiondb_pages_as_list):
    """
    Loop over Notion db pages and find the property that has the type "title".
    """

    for single_n_page in notiondb_pages_as_list:
        if isinstance(single_n_page, dict) and single_n_page.get("properties"):
            for key, value in single_n_page["properties"].items():
                if isinstance(value, dict) and value.get("type") == "title":
                    return key

    return None


def _find_page_where_title_value_matches_string(notiondb_pages_as_list, title):
    """
    This will grab the page we want to copy based on searching for the title.
    The titles are super nested and deep into the page dict so this is a bit
    of a pain to get to.

    """
    title_prop_name_for_db = _find_title_key_in_properties_dict(notiondb_pages_as_list)
    for p in notiondb_pages_as_list:
        if p["properties"][title_prop_name_for_db]["title"][0]["plain_text"] == title:
            return p
            # type: ignore

    raise ValueError(f"Could not find page with title '{title}' in database.")


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


def _create_properties_copies_and_add_increment(num, properties_dict, days=7):
    """
    Make n copies of a properties dict and return a list of dicts.
    """
    # initialize to be the exact same as the original
    list_of_dates_to_return = [deepcopy(properties_dict) for _ in range(num)]

    original_date = properties_dict["Do Date"]["date"]["start"]

    # Wrote less efficiently to show steps. Just incrementing start date by days and storing
    # in a list.
    new_dates = []
    for i in range(num):
        days_to_add = (i + 1) * days
        updated_date = pd.to_datetime(original_date) + datetime.timedelta(
            days=days_to_add
        )
        new_dates.append(updated_date.strftime("%Y-%m-%d"))

    # Main update step to the properties dict
    for propcopy, replacementdate in zip(list_of_dates_to_return, new_dates):
        propcopy.update({"Do Date": {"date": {"start": replacementdate}}})

    return list_of_dates_to_return


def run_copy_and_increment_end_to_end(database_id, title, num:int, days_between=7):
    """
    Run the whole process of copying a page and incrementing the dates.
    """
    all_results = collect_paginated_api(notion.databases.query, database_id=database_id)
    page_copy = _find_page_where_title_value_matches_string(all_results, title)
    properties_with_updated_dates = _create_properties_copies_and_add_increment(
        num, _extract_properties_from_page(page_copy), days=days_between
    )

    for prop in properties_with_updated_dates:
        notion.pages.create(
            parent={"database_id": database_id},
            properties=prop,
        )
