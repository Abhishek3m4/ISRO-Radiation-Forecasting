from pathlib import Path
from datetime import date, timedelta

ROOT = Path("data/raw/swe")

for year in range(2010, 2021):

    folder = ROOT / str(year)

    downloaded = set()

    if folder.exists():
        for f in folder.glob("*.cdf"):
            try:
                downloaded.add(f.name[10:18])   # YYYYMMDD
            except:
                pass

    start = date(year, 1, 1)
    end = date(year + 1, 1, 1)

    d = start

    missing = []

    while d < end:

        s = d.strftime("%Y%m%d")

        if s not in downloaded:
            missing.append(s)

        d += timedelta(days=1)

    print(f"\n===== {year} =====")
    print(f"Downloaded : {len(downloaded)}")
    print(f"Missing    : {len(missing)}")

    if missing:
        print(*missing[:20], sep="\n")

        if len(missing) > 20:
            print("...")