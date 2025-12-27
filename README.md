# A State of Mind Counseling Website

Static website for A State of Mind Counseling, built with Jinja2 templates.

## Structure

```
templates/          # Jinja2 source templates
├── base.html       # Base layout
├── partials/       # Shared components (header, footer, cta)
└── pages/          # Page content
docs/               # Generated site (deploy target)
build.py            # Build script
```

## Building

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/).

```bash
uv run python build.py
```

This generates the site in `docs/`.

## Deployment

GitHub Pages serves from `docs/` on the main branch.

To deploy changes:

1. Edit templates in `templates/`
2. Run `uv run python build.py`
3. Commit and push (including `docs/`)

## Editing

- **Site-wide data** (contact info, testimonials, quotes): Edit `build.py`
- **Shared layout**: Edit `templates/base.html` or `templates/partials/`
- **Page content**: Edit `templates/pages/*.html`
