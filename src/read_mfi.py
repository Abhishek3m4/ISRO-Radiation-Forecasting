import cdflib

cdf = cdflib.CDF(
    r"data/raw/wind_mfi/wi_h0_mfi_20260601_v03.cdf"
)

info = cdf.cdf_info()

print(info)