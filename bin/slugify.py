import csv

from digital_land.slug import Slugger


f = "dataset/local-plan-data.csv"
out_file = "dataset/local-plan-data-slug.csv"

reader = csv.DictReader(open(f))

out_fields = reader.fieldnames + ["organisation", "slug"]

writer = csv.DictWriter(open(out_file, "w"), out_fields)
writer.writeheader()

for row in reader:
    row["organisation"] = row["planning_authority"]
    row["slug"] = Slugger.generate_slug("local-plan", "plan_id", row)
    writer.writerow(row)
