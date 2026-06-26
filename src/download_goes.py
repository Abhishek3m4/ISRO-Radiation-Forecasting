# src/download_goes.py

import requests
from pathlib import Path

BASE_URL = (
    "https://cdaweb.gsfc.nasa.gov/pub/data/goes/"
    "goes15/epead-electrons/e13ew_1min"
)

ROOT = Path("data/raw/goes")

for year in range(2010, 2021):

    year_dir = ROOT / str(year)
    year_dir.mkdir(parents=True, exist_ok=True)

    for month in range(1, 13):

        date = f"{year}{month:02d}01"

        filename = (
            f"goes15_epead-science-electrons-"
            f"e13ew_1min_{date}_v01.cdf"
        )

        url = f"{BASE_URL}/{year}/{filename}"

        save_path = year_dir / filename

        if save_path.exists():
            print("SKIP:", filename)
            continue

        try:
            r = requests.get(url, timeout=60)

            if r.status_code == 200:

                save_path.write_bytes(r.content)

                print("DOWNLOADED:", filename)

            else:
                print("NOT FOUND:", filename)

        except Exception as e:
            print("ERROR:", filename, e)