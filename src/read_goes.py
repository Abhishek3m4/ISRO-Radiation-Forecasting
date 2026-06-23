import cdflib

cdf = cdflib.CDF(
    r"data/raw/goes/goes15_epead-science-electrons-e13ew_1min_20150101_v01.cdf"
)

info = cdf.cdf_info()

print("\nVariables:\n")

for var in info.zVariables:
    print(var)