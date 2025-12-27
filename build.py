#!/usr/bin/env python3
"""
Static site generator for A State of Mind Counseling website.
Uses Jinja2 templates to generate HTML pages.

Usage:
    python build.py
"""

from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Paths
ROOT_DIR = Path(__file__).parent
TEMPLATES_DIR = ROOT_DIR / "templates"
OUTPUT_DIR = ROOT_DIR / "docs"

# Site-wide configuration
SITE = {
    "name": "A State of Mind Counseling",
    "phone": "3034166116",
    "phone_display": "(303) 416-6116",
    "email": "astateofmindcounsel@gmail.com",
    "address_line1": "1135 Pearl St #207",
    "address_line2": "Boulder, CO 80302",
    "calendly_url": "https://calendly.com/astateofmind",
    "form_endpoint": "https://script.google.com/macros/s/AKfycbyd7Q18YaKXBQMiHKZYS8Rs6l1aOchtw0nYrPVGVrhB3FnHicxCRvR7csoB78kKmDE7/exec",
}

# Testimonials data
TESTIMONIALS = [
    {
        "quote": "I want you to know that our son, C__, who you worked with 2 years ago, has not smoked pot since then which means he hasn't had any more episodes of CHS (Cannabinoid hyperemesis syndrome)! We are so thankful that you helped our son",
        "author": "H.S., Client's Parent",
        "date": "May 2020",
    },
    {
        "quote": "Julian held a really great space during our session. I felt a lot of trust with the gentleness of his speaking and how he reflecting back to me my own process as I worked through it. I am leaving my session with him in a deep feeling of gratitude for everything.",
        "author": "Steven J., Client",
        "date": "February 2022",
    },
    {
        "quote": "Julian has been such a joy to work with. In just a few sessions, his insight and guidance have helped me to gain incredible clarity. Julian has created a safe environment to go deep and explore beneath the surface. I am incredibly grateful for Julian and the support he has provided.",
        "author": "Mary K., Client",
        "date": "October 2019",
    },
    {
        "quote": "It is like the sun has come out for Alex (not their real name). We are so grateful to see the profound changes in our child and to see them thriving and no longer at risk",
        "author": "R.J., Client's Parent",
        "date": "October 2020",
    },
    {
        "quote": "The quality of soulfulness and depth with which Julian operates is profound. He's got the Midas Touch especially when working with clients. I highly recommend his work",
        "author": "Kevin McKeag, Client",
        "date": "August 2023",
    },
    {
        "quote": "Humans thrive when Someone validates their unique sparkle. Julian is a gifted healer. We wholeheartedly recommend him",
        "author": "Alex M., Client",
        "date": "July 2023",
    },
]

# Quotes for about page
QUOTES = [
    {
        "text": "Every morning think as you wake up: I am alive, I have a precious human life, I am not going to waste it.",
        "author": "The Dalai Lama",
    },
    {
        "text": "People are somewhat gorgeous collections of chemical fires, aren't they? We are towers of kinds of fires, down to the tiniest constituencies of ourselves, whatever those are.",
        "author": "Harold Brodkey",
    },
    {
        "text": "The right way to wholeness is made up of fateful detours and wrong turnings.",
        "author": "C.G. Jung",
    },
    {
        "text": "Until you make the unconscious, conscious, it will rule your life - and you will call it fate.",
        "author": "C.G. Jung",
    },
]

# Pages to build
PAGES = [
    {"template": "pages/index.html", "output": "index.html"},
    {"template": "pages/about.html", "output": "about.html"},
    {"template": "pages/credentials.html", "output": "credentials.html"},
    {"template": "pages/trauma.html", "output": "trauma.html"},
    {"template": "pages/relationships.html", "output": "relationships.html"},
    {"template": "pages/psychedelic-therapy.html", "output": "psychedelic-therapy.html"},
    {"template": "pages/life-transitions.html", "output": "life-transitions.html"},
    {"template": "pages/contact.html", "output": "contact.html"},
    {"template": "pages/faqs.html", "output": "faqs.html"},
]


def build():
    """Build all pages."""
    import shutil

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Copy static assets
    for asset_dir in ["css", "images", "js"]:
        src = ROOT_DIR / asset_dir
        dst = OUTPUT_DIR / asset_dir
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"Copied: {asset_dir}/")

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    # Global context available to all templates
    context = {
        "site": SITE,
        "year": datetime.now().year,
        "testimonials": TESTIMONIALS,
        "quotes": QUOTES,
    }

    for page in PAGES:
        template = env.get_template(page["template"])
        html = template.render(**context)

        output_path = OUTPUT_DIR / page["output"]
        output_path.write_text(html)
        print(f"Built: {page['output']}")

    print(f"\nGenerated {len(PAGES)} pages in docs/")


if __name__ == "__main__":
    build()
