import hashlib
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(".."))

from sphinx.application import Sphinx


project = "PPV Notion utils"
author = "Jameson Stillwell"
root = "index"

language = "en"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_tippy",
    "sphinx_togglebutton",
]

# -- MyST settings ---------------------------------------------------
myst_enable_extensions = [
    # "dollarmath",
    # "amsmath",
    # "deflist",
    # "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "strikethrough",
    "substitution",
    # "tasklist",
    # "attrs_block",
    # "attrs_inline",
]

# myst_number_code_blocks = ["typescript"]
myst_heading_anchors = 3
myst_footnote_transition = True
myst_dmath_double_inline = True
myst_enable_checkboxes = True
myst_substitutions = {
    "role": "[role](#syntax/roles)",
    "directive": "[directive](#syntax/directives)",
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

suppress_warnings = ["myst.strikethrough"]

# -- HTML output -------------------------------------------------
html_title = "PPV Notion Utils"


html_show_sphinx = False
html_show_sourcelink = False
html_show_copyright = False
html_last_updated_fmt = None

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["local.css"]
html_logo = "_static/Untitled.png"

html_sidebars = {
    "index": [],  # Remove sidebars on landing page to save space
}

html_theme_options = {
    "external_links": [
        {"name": "PPV Course", "url": "https://www.yearzero.io/notion-life-design"},
    ],
    "show_toc_level": 3,
    "navbar_align": "left",
}


# -- Autodoc settings ---------------------------------------------------


# def setup(app: Sphinx):
#     """Add functions to the Sphinx setup."""
#     from myst_parser._docs import (
#         DirectiveDoc,
#         DocutilsCliHelpDirective,
#         MystAdmonitionDirective,
#         MystConfigDirective,
#         MystExampleDirective,
#         MystLexer,
#         MystToHTMLDirective,
#         MystWarningsDirective,
#         NumberSections,
#         StripUnsupportedLatex,
#     )

#     app.add_directive("myst-config", MystConfigDirective)
#     app.add_directive("docutils-cli-help", DocutilsCliHelpDirective)
#     app.add_directive("doc-directive", DirectiveDoc)
#     app.add_directive("myst-warnings", MystWarningsDirective)
#     app.add_directive("myst-example", MystExampleDirective)
#     app.add_directive("myst-admonitions", MystAdmonitionDirective)
#     app.add_directive("myst-to-html", MystToHTMLDirective)
#     # app.add_post_transform(StripUnsupportedLatex)
#     # app.add_post_transform(NumberSections)
#     app.connect("html-page-context", add_version_to_css)
#     app.add_lexer("myst", MystLexer)


# def add_version_to_css(app, pagename, templatename, context, doctree):
#     """Add the version number to the local.css file, to bust the cache for changes."""
#     if app.builder.name != "html":
#         return
#     if "_static/local.css" in context.get("css_files", {}):
#         css = Path(app.srcdir, "_static/local.css").read_text("utf8")
#         hashed = hashlib.sha256(css.encode("utf-8")).hexdigest()
#         index = context["css_files"].index("_static/local.css")
# context["css_files"][index] = f"_static/local.css?hash={hashed}"
