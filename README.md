# ppv-notion-utils
Some basic automations for common tasks within the Pillars, Pipelines, and Vauls (PPV) system that runs on Notion. Note that PPV is a paid product and this won't apply to you if you're not using it.

## Quickstart
1. Create a Notion API token to let Python interact with your Notion workspace. You can do this by going to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) and creating a new integration. You'll need to give it a name and select the "Read and write" permission. Once you've created the integration, you'll be given a token that you can use to authenticate with Notion.
2. Rename `.env.example` to `.env` and paste your token into the `NOTION_TOKEN` field.
3. Fill in `WEEKS_DB` with the ID of the database that corresponds to the weekly review pages. This will allow you to bulk create new weeks in that db.
4. Fill in `ACTION_ITEMS_DB` with the ID of the database that corresponds to the action items pages. This will allow you to bulk copy/paste recurring tasks at an 
interval of your choosing.


