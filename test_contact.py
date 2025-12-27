#!/usr/bin/env python3
"""Test script for contact form submission."""

import json
import urllib.request

from build import SITE

FORM_ENDPOINT = SITE["form_endpoint"]

test_data = {
    "name": "Test User",
    "email": "test@example.com",
    "phone": "555-123-4567",
    "message": "This is a test submission from the test script.",
}


def main():
    if "YOUR_GOOGLE_APPS_SCRIPT_URL" in FORM_ENDPOINT:
        print("Error: Update FORM_ENDPOINT with your deployed Apps Script URL")
        return

    data = json.dumps(test_data).encode("utf-8")
    req = urllib.request.Request(
        FORM_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    print(f"Sending test submission to: {FORM_ENDPOINT}")
    print(f"Data: {json.dumps(test_data, indent=2)}")

    try:
        with urllib.request.urlopen(req) as response:
            result = response.read().decode("utf-8")
            print(f"\nResponse ({response.status}):")
            print(result)
    except urllib.error.HTTPError as e:
        print(f"\nHTTP Error {e.code}: {e.reason}")
        print(e.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"\nURL Error: {e.reason}")


if __name__ == "__main__":
    main()
