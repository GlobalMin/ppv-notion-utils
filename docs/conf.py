"""Sphinx configuration."""
import hashlib
from pathlib import Path

project = "PPV Notion utils"
author = "Jameson Stillwell"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx_tippy",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
    "strikethrough",
    "tasklist",
    "attrs_inline",
    "attrs_block",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
]
autodoc_typehints = "description"
html_theme = "furo"


# -- HTML output -------------------------------------------------


html_title = ""

html_last_updated_fmt = ""


# -- Local Sphinx extensions -------------------------------------------------


def setup(app):
    """Add functions to the Sphinx setup."""
    from myst_parser._docs import (
        DirectiveDoc,
        DocutilsCliHelpDirective,
        MystAdmonitionDirective,
        MystConfigDirective,
        MystExampleDirective,
        MystLexer,
        MystToHTMLDirective,
        MystWarningsDirective,
        NumberSections,
        StripUnsupportedLatex,
    )

    app.add_directive("myst-config", MystConfigDirective)
    app.add_directive("docutils-cli-help", DocutilsCliHelpDirective)
    app.add_directive("doc-directive", DirectiveDoc)
    app.add_directive("myst-warnings", MystWarningsDirective)
    app.add_directive("myst-example", MystExampleDirective)
    app.add_directive("myst-admonitions", MystAdmonitionDirective)
    app.add_directive("myst-to-html", MystToHTMLDirective)
    app.add_post_transform(StripUnsupportedLatex)
    app.add_post_transform(NumberSections)
    app.connect("html-page-context", add_version_to_css)
    app.add_lexer("myst", MystLexer)


def add_version_to_css(app, pagename, templatename, context, doctree):
    """Add the version number to the local.css file, to bust the cache for changes."""
    if app.builder.name != "html":
        return
    if "_static/local.css" in context.get("css_files", {}):
        css = Path(app.srcdir, "_static/local.css").read_text("utf8")
        hashed = hashlib.sha256(css.encode("utf-8")).hexdigest()
        index = context["css_files"].index("_static/local.css")
        context["css_files"][index] = f"_static/local.css?hash={hashed}"


##
