"""Validate public capability records and generate a deterministic catalog."""
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def validate_records(records, schema):
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    seen = set()
    for record in records:
        validator.validate(record)
        ident = record["id"]
        if ident in seen:
            raise ValueError(f"duplicate capability: {ident}")
        seen.add(ident)
        if ident.split(".")[0] != record["domain"]:
            raise ValueError(f"domain mismatch: {ident}")
        for evidence in record["evidence"]:
            if evidence["visibility"] == "RESTRICTED":
                if "url" in evidence or evidence["verification"] != "MAINTAINER_REPORTED":
                    raise ValueError("restricted evidence cannot expose URLs or claim public verification")
            elif "url" not in evidence:
                raise ValueError("public evidence requires a URL")
        if record["status"] in {"EXPERIMENTAL", "STABLE"}:
            passed = {v["kind"] for v in record["verification"] if v["result"] == "PASS"}
            required = {"CONTRACT_TEST", "SECURITY_TEST", "REAL_CONSUMER", "HUMAN_REVIEW"}
            if not record["implementations"] or not required <= passed:
                raise ValueError(f"promotion lacks implementation/verification: {ident}")
        if record["status"] == "STABLE":
            raise ValueError("STABLE promotion is unavailable during bootstrap")
    return sorted(records, key=lambda record: record["id"])

def render(records):
    return json.dumps({"schema_version": 1, "capabilities": records}, indent=2, sort_keys=True) + "\n"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    schema = json.loads((ROOT / "schema/capability.schema.json").read_text())
    files = sorted((ROOT / "capabilities").glob("*.json"))
    if not files:
        raise ValueError("no capability records")
    records = [json.loads(path.read_text()) for path in files]
    for path, record in zip(files, records):
        if path.stem != record["id"]:
            raise ValueError(f"filename does not match ID: {path.name}")
    output = render(validate_records(records, schema))
    target = ROOT / "catalog.json"
    if args.check:
        if not target.exists() or target.read_text() != output:
            raise SystemExit("catalog.json is stale; run python tools/catalog.py")
    else:
        target.write_text(output)
    print(f"Validated {len(records)} capabilities; catalog {'checked' if args.check else 'generated'}.")

if __name__ == "__main__":
    main()
