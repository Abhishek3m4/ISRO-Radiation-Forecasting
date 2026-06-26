from pathlib import Path
import argparse
import requests
from bs4 import BeautifulSoup

DATASETS = {
    "goes": {
        "base_url": "https://cdaweb.gsfc.nasa.gov/pub/data/goes/goes15/cdf/epead_e13ew_1min",
        "raw_dir": Path("data/raw/goes"),
        "years": range(2010, 2021),
    },
    "swe": {
        "base_url": "https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_h1",
        "raw_dir": Path("data/raw/wind"),
        "years": range(2010, 2021),
    },
    "mfi": {
        "base_url": "https://cdaweb.gsfc.nasa.gov/pub/data/wind/mfi/mfi_h0",
        "raw_dir": Path("data/raw/wind_mfi"),
        "years": range(2010, 2021),
    },
}

parser = argparse.ArgumentParser()
parser.add_argument("dataset", choices=DATASETS.keys())
args = parser.parse_args()

cfg = DATASETS[args.dataset]

downloads_dir = Path("downloads")
downloads_dir.mkdir(exist_ok=True)

outfile = downloads_dir / f"{args.dataset}.txt"

with outfile.open("w", encoding="utf-8") as fout:

    for year in cfg["years"]:

        print(f"Scanning {year}...")

        year_url = f"{cfg['base_url']}/{year}/"

        try:
            r = requests.get(year_url, timeout=60)
            r.raise_for_status()
        except Exception as e:
            print("Cannot open:", year_url)
            print(e)
            continue

        soup = BeautifulSoup(r.text, "html.parser")

        # create local folder only
        year_dir = cfg["raw_dir"] / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        for link in soup.find_all("a"):

            href = link.get("href", "")

            # ignore non-data files
            if not href.endswith(".cdf"):
                continue

            # NEVER SKIP EXISTING FILES
            url = f"{year_url}{href}"

            fout.write(url + "\n")
            fout.write(f" out={year}/{href}\n")

print("\nDone.")
print("Output:", outfile)