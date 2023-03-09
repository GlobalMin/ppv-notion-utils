selector_to_html = {"a[href=\"#list-tables\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">List tables<a class=\"headerlink\" href=\"#list-tables\" title=\"Permalink to this heading\">#</a></h2><p>The <code class=\"docutils literal notranslate\"><span class=\"pre\">list-table</span></code> directive is used to create a table from data in a uniform two-level bullet list.\n\u201cUniform\u201d means that each sublist (second-level list) must contain the same number of list items.</p>", "a[href=\"#reference\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Reference<a class=\"headerlink\" href=\"#reference\" title=\"Permalink to this heading\">#</a></h1><h2>Markdown syntax<a class=\"headerlink\" href=\"#markdown-syntax\" title=\"Permalink to this heading\">#</a></h2><p>Tables can be written using the standard <a class=\"reference external\" href=\"https://github.github.com/gfm/#tables-extension-\">Github Flavoured Markdown syntax</a>:</p>", "a[href=\"#id1\"]": "<table class=\"docutils align-default\" id=\"id1\">\n<caption><span class=\"caption-text\">Frozen Delights!</span><a class=\"headerlink\" href=\"#id1\" title=\"Permalink to this table\">#</a></caption>\n<colgroup>\n<col style=\"width: 27.3%\"/>\n<col style=\"width: 18.2%\"/>\n<col style=\"width: 54.5%\"/>\n</colgroup>\n<thead>\n<tr class=\"row-odd\"><th class=\"head\"><p>Treat</p></th>\n<th class=\"head\"><p>Quantity</p></th>\n<th class=\"head\"><p>Description</p></th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"row-even\"><td><p>Albatross</p></td>\n<td><p>2.99</p></td>\n<td><p>On a stick!</p></td>\n</tr>\n<tr class=\"row-odd\"><td><p>Crunchy Frog</p></td>\n<td><p>1.49</p></td>\n<td><p>If we took the bones out, it wouldn\u2019t be\ncrunchy, now would it?</p></td>\n</tr>\n<tr class=\"row-even\"><td><p>Gannet Ripple</p></td>\n<td><p>1.99</p></td>\n<td><p>On a stick!</p></td>\n</tr>\n</tbody>\n</table>", "a[href=\"#markdown-syntax\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Markdown syntax<a class=\"headerlink\" href=\"#markdown-syntax\" title=\"Permalink to this heading\">#</a></h2><p>Tables can be written using the standard <a class=\"reference external\" href=\"https://github.github.com/gfm/#tables-extension-\">Github Flavoured Markdown syntax</a>:</p>"}
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
