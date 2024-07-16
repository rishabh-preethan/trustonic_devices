from playwright.sync_api import sync_playwright
import pandas as pd

data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for page_num in range(1, 11):
        url = f"https://miportal.entel.cl/personas/catalogo/celulares/page/{page_num}"
        page.goto(url, wait_until='networkidle')
        page.set_extra_http_headers({"Cache-Control": "no-cache"})
        page.reload()
        cards = page.query_selector_all(".card-body.card-body-cascade")

        for card in cards:
            name_elem = card.query_selector(".info-equipo.mb-2.mb-xl-0")
            price_elem = card.query_selector(".info-precio.mt-1")

            name = name_elem.inner_text() if name_elem else ""
            price = price_elem.inner_text() if price_elem else ""

            data.append({"Name": name, "Price": price})

    browser.close()

df = pd.DataFrame(data)
df.to_excel("Entel_chile//entel_cellphones1.xlsx", index=False)
