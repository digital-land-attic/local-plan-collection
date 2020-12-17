import csv
import re

bad_chars = re.compile(r"[^A-Za-z0-9]")


def generate_slug(prefix, key_field, row):
    """
    Helper method to provide slug without a Slugger instance
    """
    for field in ["planning_authority", key_field]:
        if field not in row or not row[field]:
            return None

    key = bad_chars.sub("-", row[key_field])

    return f"{prefix}/{row['planning_authority'].replace(':','/')}/{key}"


f = "dataset/local-plan-data.csv"
out_file = "dataset/local-plan-data-slug.csv"

reader = csv.DictReader(open(f))

out_fields = reader.fieldnames + ["slug"]

writer = csv.DictWriter(open(out_file, "w"), out_fields)
writer.writeheader()

for row in reader:
    row["slug"] = generate_slug("local-plan", "plan_id", row)
    writer.writerow(row)
