import cdflib

cdf = cdflib.CDF(
    r"data/raw/swe/2011/wi_h1_swe_20110704_v01.cdf"
)

print(cdf.cdf_info().zVariables)