"""Static contract tests. No claims about model inference quality."""
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate import CORE, WORKBUDDY, REFERENCE_NAMES, check, frontmatter
from build_packages import pack


class SkillContractTests(unittest.TestCase):
    def test_repo_contract(self):
        self.assertEqual(check(), [])

    def test_core_name(self):
        self.assertEqual(frontmatter((CORE / "SKILL.md").read_text("utf-8"))["name"], "analytical-reading")

    def test_workbuddy_required_fields(self):
        data = frontmatter((WORKBUDDY / "SKILL.md").read_text("utf-8"))
        self.assertEqual(data["version"], "2.1.0")
        for key in ("description", "description_zh", "description_en", "author"):
            self.assertTrue(data[key])

    def test_references_mirrored(self):
        for name in REFERENCE_NAMES:
            self.assertEqual((CORE / "references" / name).read_bytes(),
                             (WORKBUDDY / "references" / name).read_bytes())

    def test_checked_in_downloads_match_source(self):
        pairs = [
            ("analytical-reading-agent-skill-v2.1.0.zip", CORE),
            ("workbuddy-analytical-reading-v2.1.0.zip", WORKBUDDY),
        ]
        for zip_name, folder in pairs:
            with ZipFile(ROOT / "downloads" / zip_name) as zf:
                expected = {
                    "analytical-reading/" + str(f.relative_to(folder)).replace("\\", "/"): f.read_bytes()
                    for f in folder.rglob("*") if f.is_file() and not f.name.startswith(".")
                }
                self.assertEqual(set(zf.namelist()), set(expected))
                for member, content in expected.items():
                    self.assertEqual(zf.read(member), content, f"stale archive: {zip_name}: {member}")

    def test_both_zips_have_single_skill_root(self):
        with TemporaryDirectory() as temp:
            for folder in (CORE, WORKBUDDY):
                path = Path(temp) / (folder.parent.name + ".zip")
                pack(folder, path)
                with ZipFile(path) as zf:
                    names = zf.namelist()
                    self.assertEqual(len(names), len(set(names)))
                    self.assertIn("analytical-reading/SKILL.md", names)
                    self.assertTrue(all(n.startswith("analytical-reading/") for n in names))
                    for ref in REFERENCE_NAMES:
                        self.assertIn("analytical-reading/references/" + ref, names)


if __name__ == "__main__":
    unittest.main()
