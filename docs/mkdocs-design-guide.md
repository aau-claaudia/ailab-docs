# How to design a MkDocs page 

This is a basic overview of which features you can use to design a MkDocs page. You can find more features: https://squidfunk.github.io/mkdocs-material/reference/

## Headings and font

You write normal paragraph text just by typing like this. You can create headings by placing a # before the text like so:

# Heading 1
## Heading 2
### Heading 3
#### Heading 4

## Insert code in text and in codeblocks:

You use backticks to `write code in text`.

You can also create a console codeblock like so:

```console
pwd
```

You can also make it a python codeblock:
```py
import tensorflow as tf
```

## Call-outs
You can make call-outs/admonitions like so:

??? info "This is a closed info box by default"
    This is the content

???+ info "This is a open info box by default"
    This is the content

Look at https://squidfunk.github.io/mkdocs-material/reference/admonitions/ for more types of call-outs, like warning, example etc.

## Data tables
You can also create data tables like this:

| Method      | Description     |
| ----------- | --------------- |
| `GET`       | Fetch resource  |
| `PUT`       | Update resource |
| `DELETE`    | Delete resource |


## Custom HTML/CSS
<div>
    <p>
        You can paste your own custom HTML/CSS as you would normal in a .html file
    </p>
</div>