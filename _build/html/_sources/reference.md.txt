# Reference

## Markdown syntax

Tables can be written using the standard [Github Flavoured Markdown syntax](https://github.github.com/gfm/#tables-extension-):

:::{myst-example}
| foo | bar |
| --- | --- |
| baz | bim |
:::


The following options are recognized:

:::{admonition} ""
:class: seealso
:name: list-table-options



`align` : "left", "center", or "right"
: The horizontal alignment of the table.

`width` : [length] or [percentage]


`widths` : "auto", "grid", or a list of integers

:::

## List tables

The `list-table` directive is used to create a table from data in a uniform two-level bullet list.
"Uniform" means that each sublist (second-level list) must contain the same number of list items.

::::{myst-example}
:::{list-table} Frozen Delights!
:widths: 15 10 30
:header-rows: 1

*   - Treat
    - Quantity
    - Description
*   - Albatross
    - 2.99
    - On a stick!
*   - Crunchy Frog
    - 1.49
    - If we took the bones out, it wouldn't be
 crunchy, now would it?
*   - Gannet Ripple
    - 1.99
    - On a stick!
:::
::::

:::{note}
:class: dropdown
```{docutils-cli-help}
```
:::

:::{versionadded} 0.19.0
`myst-suppress-warnings` replicates 
:::

