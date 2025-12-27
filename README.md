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

## Contact Form Setup

The contact form uses Google Apps Script to send emails. The script is in `contact-form.gs`.

### Initial Setup

1. Go to [script.google.com](https://script.google.com)
2. Click **New project**
3. Delete any placeholder code and paste the contents of `contact-form.gs`
4. Click **Deploy** > **New deployment**
5. Click the gear icon next to "Select type" and choose **Web app**
6. Configure:
   - Description: "Contact form handler"
   - Execute as: **Me**
   - Who has access: **Anyone**
7. Click **Deploy**
8. Authorize the app when prompted (allows it to send email as you)
9. Copy the **Web app URL**
10. Paste the URL into `build.py` under `SITE["form_endpoint"]`
11. Rebuild: `uv run python build.py`

### Updating the Script

If you modify `contact-form.gs`:

1. Go to your project at [script.google.com](https://script.google.com)
2. Update the code
3. Click **Deploy** > **New deployment** (not "Manage deployments")
4. Configure as Web app with the same settings
5. Copy the new URL and update `build.py` if it changed
6. Rebuild the site

### Testing

```bash
uv run python test_contact.py
```

This sends a test submission. Check the target email inbox for the message.
