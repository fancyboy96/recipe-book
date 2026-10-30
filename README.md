# Recipes

A static recipe book website.

## Running locally

This is a fully static site — no server, framework, or build step required.

Just open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Adding a recipe

Recipes live in their own pages under `recipes/<recipe-name>/index.html`.

1. Create a new folder like `recipes/my-new-recipe/`.
2. Copy an existing recipe page as a template.
3. Update the title, recipe name, date, ingredients, and steps.

The homepage (`index.html`) has a table of recipes — add a row with the recipe name linking to its page and its date.

## Deploying

Because it's static, it can be hosted anywhere that serves static files:
GitHub Pages, Netlify, Vercel, S3, or any plain web server.
