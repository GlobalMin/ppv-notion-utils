# PPV Notion Utils

> Yet another workaround solution to make Notion have basic recurring tasks functionality. Many paid options are well known as well as decent
> free ones. Most are GUI based flows that are too bulky and tedious for this one very specific use case. So this repo tries to be a free option
> to have a recurring task system that can be pulled out whenever needed and the setup will stay the same, so it'll remain fast and focused on
> this one task.

Some basic automations for common tasks within the Pillars, Pipelines, and Vauls (PPV) system that runs on Notion. **Note that PPV is a paid product and this won't apply to you if you're not using it.**

Check out course info here if you want to know what this is about:
https://www.yearzero.io/notion-life-design

---

## Recurring tasks

The thing that must not be mentioned to a Notion fan.

### Within native Notion

Notion infamously doesn't have a native way to create recurring tasks. They released functionality to repeat templates and this seems potentially close enough at first
but there isn't a way to filter on a future date which makes it basically useless.

### Solution this repo provides

:::{card} Before

```{image} _static/recurring_task_before.png

```

:::

:::{card} After

```{image} _static/recurring_task_after.png

```

:::

## Quickstart

```{admonition} Copied from README.md
:class: note
:name: list-table-options

1. Create a Notion API token to let Python interact with your Notion workspace. You can do this by going to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) and creating a new integration. You'll need to give it a name and select the "Read and write" permission. Once you've created the integration, you'll be given a token that you can use to authenticate with Notion.
2. Rename `.env.example` to `.env` and paste your token into the `NOTION_TOKEN` field.
3. Fill in `WEEKS_DB` with the ID of the database that corresponds to the weekly review pages. This will allow you to bulk create new weeks in that db.
4. Fill in `ACTION_ITEMS_DB` with the ID of the database that corresponds to the action items pages. This will allow you to bulk copy/paste recurring tasks at an
interval of your choosing.
5. (Optoinal) Create a new virtual environment and install the dependencies with command `make install`. It's not a great idea to install dependencies globally on your machine but if you want you can simply run `pip install -r requirements.txt`.
5. Open quick_start.ipynb for recurring tasks walkthrough.

```

:::{card} Now...
Now open up [quick-start.ipynb](https://github.com/GlobalMin/ppv-notion-utils/blob/e4e4f082957834a124b049f70c651fdabff176d2/quick_start.ipynb) and follow the instructions there.
:::
