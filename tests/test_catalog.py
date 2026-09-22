import copy
import importlib.util
import json
import unittest
from pathlib import Path
from jsonschema import ValidationError

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("catalog", ROOT / "tools/catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((ROOT / "schema/capability.schema.json").read_text())
        self.record = json.loads((ROOT / "capabilities/identity.service-credentials.json").read_text())
    def validate(self, records=None):
        return catalog.validate_records(records or [self.record], self.schema)
    def test_candidate_valid(self):
        self.validate()
    def test_unknown_fields_rejected(self):
        self.record["private_notes"] = "not allowed"
        with self.assertRaises(ValidationError): self.validate()
    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError): self.validate([self.record, copy.deepcopy(self.record)])
    def test_domain_mismatch_rejected(self):
        self.record["domain"] = "billing"
        with self.assertRaises(ValueError): self.validate()
    def test_restricted_url_rejected(self):
        self.record["evidence"][0]["url"] = "https://example.com/restricted"
        with self.assertRaises(ValueError): self.validate()
    def test_private_public_claim_rejected(self):
        self.record["evidence"][0]["verification"] = "PUBLICLY_REPRODUCIBLE"
        with self.assertRaises(ValueError): self.validate()
    def test_public_evidence_requires_url(self):
        self.record["evidence"][0]["visibility"] = "PUBLIC"
        with self.assertRaises(ValueError): self.validate()
    def test_unverified_promotion_rejected(self):
        self.record["status"] = "EXPERIMENTAL"
        with self.assertRaises(ValueError): self.validate()
    def test_stable_unavailable(self):
        self.record["status"] = "STABLE"
        with self.assertRaises(ValueError): self.validate()
    def test_deterministic_order(self):
        second = copy.deepcopy(self.record)
        second["id"] = "identity.another"
        a = catalog.render(self.validate([self.record, second]))
        b = catalog.render(self.validate([second, self.record]))
        self.assertEqual(a,b)
    def test_valid_experimental_evidence(self):
        self.record["status"] = "EXPERIMENTAL"
        self.record["implementations"] = [{"url":"https://example.com/code","revision":"test-fixture"}]
        self.record["verification"] = [{"kind":k,"result":"PASS","evidence_url":"https://example.com/test-fixture"} for k in ["CONTRACT_TEST","SECURITY_TEST","REAL_CONSUMER","HUMAN_REVIEW"]]
        self.validate()
    def test_failed_consumer_is_not_verification(self):
        self.record["status"] = "EXPERIMENTAL"
        self.record["implementations"] = [{"url":"https://example.com/code","revision":"test-fixture"}]
        self.record["verification"] = [{"kind":"REAL_CONSUMER","result":"FAIL","evidence_url":"https://example.com/test-fixture"}]
        with self.assertRaises(ValueError): self.validate()

if __name__ == "__main__": unittest.main()
