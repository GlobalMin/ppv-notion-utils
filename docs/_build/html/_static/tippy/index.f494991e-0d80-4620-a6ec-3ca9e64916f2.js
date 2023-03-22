selector_to_html = {"a[href=\"#quickstart\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Quickstart<a class=\"headerlink\" href=\"#quickstart\" title=\"Permalink to this heading\">#</a></h2>", "a[href=\"#recurring-tasks\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Recurring tasks<a class=\"headerlink\" href=\"#recurring-tasks\" title=\"Permalink to this heading\">#</a></h2><p>The thing that must not be mentioned to a Notion fan.</p>", "a[href=\"#within-native-notion\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Within native Notion<a class=\"headerlink\" href=\"#within-native-notion\" title=\"Permalink to this heading\">#</a></h3><p>Notion infamously doesn\u2019t have a native way to create recurring tasks. They released functionality to repeat templates and this seems potentially close enough at first\nbut there isn\u2019t a way to filter on a future date which makes it basically useless.</p>", "a[href=\"#solution-this-repo-provides\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Solution this repo provides<a class=\"headerlink\" href=\"#solution-this-repo-provides\" title=\"Permalink to this heading\">#</a></h3>", "a[href=\"#ppv-notion-utils\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">PPV Notion Utils<a class=\"headerlink\" href=\"#ppv-notion-utils\" title=\"Permalink to this heading\">#</a></h1><p>Some basic automations for common tasks within the Pillars, Pipelines, and Vauls (PPV) system that runs on Notion. <strong>Note that PPV is a paid product and this won\u2019t apply to you if you\u2019re not using it.</strong></p><p>Check out course info here if you want to know what this is about:\n<a class=\"reference external\" href=\"https://www.yearzero.io/notion-life-design\">https://www.yearzero.io/notion-life-design</a></p>"}
skip_classes = ["headerlink", "sd-stretched-link"]

window.onload = function () {
    for (const [select, tip_html] of Object.entries(selector_to_html)) {
        const links = document.querySelectorAll(` ${select}`);
        for (const link of links) {
            if (skip_classes.some(c => link.classList.contains(c))) {
                continue;
            }

            tippy(link, {
                content: tip_html,
                allowHTML: true,
                arrow: true,
                placement: 'auto-start', maxWidth: 500, interactive: false,

            });
        };
    };
    console.log("tippy tips loaded!");
};
