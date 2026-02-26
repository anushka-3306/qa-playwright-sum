from playwright.sync_api import sync_playwright
import re

BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed="

def main():
    grand_total = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for seed in range(57, 67):  # 57 to 66
            url = f"{BASE_URL}{seed}"
            page.goto(url)
            page.wait_for_load_state("networkidle")

            text = page.inner_text("body")
            numbers = re.findall(r"\d+", text)

            seed_sum = sum(int(num) for num in numbers)
            print(f"Seed {seed} sum: {seed_sum}")

            grand_total += seed_sum

        browser.close()

    print("\nTOTAL SUM:", grand_total)


if __name__ == "__main__":
    main()
