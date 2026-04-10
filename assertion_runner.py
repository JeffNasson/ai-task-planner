def run_real_assertion(page, assertion: str):
    assertion = assertion.lower()

    if "dashboard" in assertion or "logged in" in assertion:
        assert "/secure" in page.url, f"Expected secure page, got {page.url}"
    elif "error" in assertion or "invalid" in assertion:
        assert page.locator("#flash").is_visible(), "Error message not visible"

    else:
        print(f"SKIPPED: No mapping for assertion → {assertion}")
        return

    print("PASS")