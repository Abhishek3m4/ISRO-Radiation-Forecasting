from pathlib import Path
from datetime import date, timedelta
import requests

BASE_URL = "https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_h1"

START_YEAR = 2010
END_YEAR = 2020

base_dir = Path("data/raw/wind")

for year in range(START_YEAR, END_YEAR + 1):

    year_dir = base_dir / str(year)
    year_dir.mkdir(parents=True, exist_ok=True)

    current = date(year, 1, 1)
    last_day = date(year, 12, 31)

    while current <= last_day:

        datestr = current.strftime("%Y%m%d")

        filename = f"wi_h1_swe_{datestr}_v01.cdf"

        url = f"{BASE_URL}/{year}/{filename}"

        save_path = year_dir / filename

        if save_path.exists():
            current += timedelta(days=1)
            continue

        try:

            r = requests.get(url, timeout=10)

            if r.status_code == 200:

                save_path.write_bytes(r.content)

                print("DOWNLOADED:", filename)

            else:

                print("NOT FOUND:", filename)

        except Exception as e:

            print("ERROR:", filename, e)

        current += timedelta(days=1)