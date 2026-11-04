import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "scripts/verify_data.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CSVTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "sample.csv"

    def put(self, content):
        self.path.write_text(content)
        return self.path

    def test_real_sample_deterministic(self):
        a = MODULE.inspect_csv()
        self.assertEqual(a, MODULE.inspect_csv())
        self.assertGreater(a["rows"], 0)
        self.assertFalse(a["provenance_verified"])
        self.assertFalse(a["scientific_claims_validated"])

    def test_known_statistics(self):
        r = MODULE.inspect_csv(self.put("date,C20,source\n2026-01-01,1,sample\n2026-02-01,3,sample\n"))
        self.assertEqual(r["C20"], {"min": 1, "max": 3, "mean": 2})
        self.assertEqual(len(r["data_sha256"]), 64)

    def test_headers_and_empty_data(self):
        for content in ("date,C20\n", "date,C20,source\n"):
            with self.assertRaises(ValueError):
                MODULE.inspect_csv(self.put(content))

    def test_nonfinite_and_bad_date(self):
        for content in ("date,C20,source\n2026-01-01,nan,test\n",
                        "date,C20,source\nbad,1,test\n"):
            with self.assertRaises(ValueError):
                MODULE.inspect_csv(self.put(content))

    def test_duplicate_dates(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            MODULE.inspect_csv(self.put("date,C20,source\n2026-01-01,1,x\n2026-01-01,2,x\n"))

    def test_symlink_rejected(self):
        self.path.symlink_to(MODULE.DEFAULT_DATA)
        with self.assertRaises(ValueError):
            MODULE.inspect_csv(self.path)

    def test_reproduction_does_not_write_dummy_figure(self):
        p = subprocess.run([sys.executable, str(ROOT / "scripts/repro.py")],
                           cwd=self.temp.name, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)["schema"], "pva.csv-summary/v1")
        self.assertFalse((Path(self.temp.name) / "fig_C20.png").exists())


if __name__ == "__main__":
    unittest.main()
