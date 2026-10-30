# Belle's Recipe Book

A small static website for my girlfriend's recipe book.

## Running locally

This is a fully static site — no server, framework, or build step required.

Just open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Adding a recipe

All recipes live directly in `index.html`, inside the `.recipe-list` section.

Each recipe is a `<details>` card:

1. Copy an existing `<article class="recipe-card">` block.
2. Update the card's `id`.
3. Change the recipe name, description, and date.
4. Add ingredient lines using the quantity/unit spans, e.g.
   `<span class="ingredient-quantity">2</span> <span class="ingredient-unit">cups</span> sugar`.
5. Add direction lines using the step number span, e.g.
   `<span class="step-number">1</span> Preheat the oven to 350°F.`

## Deploying

Because it's static, it can be hosted anywhere that serves static files:
GitHub Pages, Netlify, Vercel, S3, or any plain web server.
