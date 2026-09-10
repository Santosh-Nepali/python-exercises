'''
import string
import time
import json
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://opennav.com/airportcodes/icao"

airports = {}

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; ICAO-Airport-Scraper/1.0)"
}

for letter in string.ascii_uppercase:
    url = f"{BASE_URL}?{letter}="

    print(f"Scraping {letter}: {url}")

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing ICAO / IATA / NAME.
    table = None

    for candidate in soup.find_all("table"):
        headers_found = [
            cell.get_text(" ", strip=True).upper()
            for cell in candidate.find_all(["th", "td"])
        ]

        if "ICAO" in headers_found and "IATA" in headers_found and "NAME" in headers_found:
            table = candidate
            break

    if table is None:
        print(f"  WARNING: no airport table found for {letter}")
        continue

    count = 0

    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])

        if len(cells) < 3:
            continue

        icao = cells[0].get_text(" ", strip=True).upper()
        iata = cells[1].get_text(" ", strip=True).upper()
        name = cells[2].get_text(" ", strip=True)

        # Skip header rows and malformed entries.
        if icao == "ICAO":
            continue

        if len(icao) != 4:
            continue

        airports[icao] = {
            "iata": iata or None,
            "name": name,
        }

        count += 1

    print(f"  Found {count} airports")

    # Be polite to the website.
    time.sleep(0.5)


print(f"\nTotal airports: {len(airports)}")

# Save as JSON
with open("icao_airports.json", "w", encoding="utf-8") as f:
    json.dump(
        airports,
        f,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    )

print("Saved to icao_airports.json")

# Optional: generate a Python dictionary file
with open("icao_airports.py", "w", encoding="utf-8") as f:
    f.write("# Generated from OpenNav ICAO airport directory\n\n")
    f.write("AIRPORTS = ")
    f.write(repr(dict(sorted(airports.items()))))
    f.write("\n")

print("Saved to icao_airports.py")

'''