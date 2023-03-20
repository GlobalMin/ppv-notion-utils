selector_to_html = {"a[href=\"#code-of-conduct\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Code of Conduct<a class=\"headerlink\" href=\"#code-of-conduct\" title=\"Permalink to this heading\">#</a></h1><h2>Placeholder<a class=\"headerlink\" href=\"#placeholder\" title=\"Permalink to this heading\">#</a></h2><h3>Getting Python (Windows)<a class=\"headerlink\" href=\"#getting-python-windows\" title=\"Permalink to this heading\">#</a></h3><p>If you\u2019re on Windows,\ndownload the recommended installer for the latest stable release of Python\nfrom the official [Python website].\nBefore clicking <strong>Install now</strong>,\nenable the option to add Python to your <code class=\"docutils literal notranslate\"><span class=\"pre\">PATH</span></code> environment variable.</p><p>Verify your installation by checking the output of the following commands in a new terminal window:</p>", "a[href=\"#getting-python-windows\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Getting Python (Windows)<a class=\"headerlink\" href=\"#getting-python-windows\" title=\"Permalink to this heading\">#</a></h3><p>If you\u2019re on Windows,\ndownload the recommended installer for the latest stable release of Python\nfrom the official [Python website].\nBefore clicking <strong>Install now</strong>,\nenable the option to add Python to your <code class=\"docutils literal notranslate\"><span class=\"pre\">PATH</span></code> environment variable.</p><p>Verify your installation by checking the output of the following commands in a new terminal window:</p>", "a[href=\"#placeholder\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Placeholder<a class=\"headerlink\" href=\"#placeholder\" title=\"Permalink to this heading\">#</a></h2><h3>Getting Python (Windows)<a class=\"headerlink\" href=\"#getting-python-windows\" title=\"Permalink to this heading\">#</a></h3><p>If you\u2019re on Windows,\ndownload the recommended installer for the latest stable release of Python\nfrom the official [Python website].\nBefore clicking <strong>Install now</strong>,\nenable the option to add Python to your <code class=\"docutils literal notranslate\"><span class=\"pre\">PATH</span></code> environment variable.</p><p>Verify your installation by checking the output of the following commands in a new terminal window:</p>"}
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
