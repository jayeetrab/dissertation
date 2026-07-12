from spatial import extract_spatial_metadata

text = "A proposed 80-unit residential development on a brownfield site in Clifton, Bristol city centre."
res = extract_spatial_metadata(text)
print(f"Location: {res.location_name}, Lat: {res.lat}, Lon: {res.lon}")
