import requests
from bs4 import BeautifulSoup

BASE = "https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_h1/2014/"

r = requests.get(BASE, timeout=300)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

with open("downloads/swe_2014.txt", "w", encoding="utf-8") as f:
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if href.endswith(".cdf"):
            f.write(BASE + href + "\n")
            f.write(f" out=2014/{href}\n")

print("Done")