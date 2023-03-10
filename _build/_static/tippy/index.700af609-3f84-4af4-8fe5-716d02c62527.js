selector_to_html = {"a[href=\"#admonition-types\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">2.\u00a0\u00a0Admonition types<a class=\"headerlink\" href=\"#admonition-types\" title=\"Permalink to this heading\">#</a></h2><p>The following core admonition types are available:</p>", "a[href=\"#ppv-notion-utils\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">PPV Notion Utils<a class=\"headerlink\" href=\"#ppv-notion-utils\" title=\"Permalink to this heading\">#</a></h1><p>A set of helper scripts that automate or speed up componente of he Pillars, Pipelines, and Vaults (PPV) life design system that runs in Notion.</p>", "a[href=\"#id1\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">1.\u00a0\u00a0<a class=\"headerlink\" href=\"#id1\" title=\"Permalink to this heading\">#</a></h2>", "a[href=\"#id2\"]": "<table class=\"docutils align-default\" id=\"id2\">\n<caption><span class=\"caption-text\">Project variables</span><a class=\"headerlink\" href=\"#id2\" title=\"Permalink to this table\">#</a></caption>\n<thead>\n<tr class=\"row-odd\"><th class=\"head\"><p>Variable</p></th>\n<th class=\"head\"><p>Description</p></th>\n<th class=\"head\"><p>Example</p></th>\n</tr>\n</thead>\n<tbody>\n<tr class=\"row-even\"><td><p><code class=\"docutils literal notranslate\"><span class=\"pre\">project_name</span></code></p></td>\n<td><p>Project name on PyPI and GitHub</p></td>\n<td><p><code class=\"docutils literal notranslate\"><span class=\"pre\">hypermodern-python</span></code></p></td>\n</tr>\n<tr class=\"row-odd\"><td><p><code class=\"docutils literal notranslate\"><span class=\"pre\">package_name</span></code></p></td>\n<td><p>Python package name</p></td>\n<td><p><code class=\"docutils literal notranslate\"><span class=\"pre\">hypermodern_python</span></code></p></td>\n</tr>\n</tbody>\n</table>"}
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
