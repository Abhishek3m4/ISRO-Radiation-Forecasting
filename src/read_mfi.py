import cdflib

cdf = cdflib.CDF(
    r"data/raw/wind_mfi/wind_mfi_jan2015/wi_h0_mfi_20150101_v05.cdf"
)

info = cdf.cdf_info()

print(info)