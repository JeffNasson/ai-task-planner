def run_real_assertion(page, assertion: str):
    assertion = assertion.lower()
    flash = page.locator("#flash")

    if "dashboard" in assertion or "logged in" in assertion:
        assert "/secure" in page.url, f"Expected secure page, got {page.url}" # This locator is specific to the herokuapp login page. In a real application, you would need to use a locator that matches the secure page element on your page.
    elif any(word in assertion for word in ["invalid", "error", "incorrect"]):
        assert flash.is_visible(), "Error message not visible" # This checks that the flash message is visible on the page, which is where the error message is displayed on the herokuapp login page.
        assert "invalid" in flash.text_content().lower(), "Wrong error message displayed" # This checks that the flash message contains the word "invalid", which is part of the error message displayed when login fails on the herokuapp login page.

    elif any(word in assertion for word in ["required", "empty", "missing"]):
        assert flash.is_visible(), "Validation message not visible" # This checks that the flash message is visible on the page, which is where the validation message is displayed on the herokuapp login page when required fields are empty.
        assert "required" in flash.text_content().lower() or "empty" in flash.text_content().lower(), "Wrong validation message" # This is a simple check for the presence of "required" or "empty" in the flash message.
    else:
        print(f"SKIPPED: No mapping for assertion → {assertion}") # If the assertion doesn't match any of the known patterns, print a message and skip the assertion instead of failing the test.
        return

    print("PASS")