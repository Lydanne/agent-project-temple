import unittest,tempfile,shutil,subprocess,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Contract(unittest.TestCase):
 def test_clean_template(self):
  self.assertEqual(subprocess.run(['python3',str(ROOT/'scripts/check.py'),str(ROOT)],capture_output=True).returncode,0)
 def test_reject_invalid_metadata_or_policy(self):
  with tempfile.TemporaryDirectory() as td:
   r=Path(td)/'repo';shutil.copytree(ROOT,r,ignore=shutil.ignore_patterns('.git','__pycache__'))
   if (r/'bundle.json').exists():
    s=(r/'README.md').read_text();(r/'README.md').write_text(s.replace('"draft"','"stable"',1))
   else:
    p=r/'project.json';d=json.loads(p.read_text());d['git']['auto_merge']=True;p.write_text(json.dumps(d))
   self.assertNotEqual(subprocess.run(['python3',str(ROOT/'scripts/check.py'),str(r)],capture_output=True).returncode,0)

 def test_escaping_repository_and_invalid_wiki_are_rejected(self):
  for mode in ['path','wiki']:
   with tempfile.TemporaryDirectory() as td:
    r=Path(td)/'repo';shutil.copytree(ROOT,r,ignore=shutil.ignore_patterns('.git','__pycache__'))
    if mode=='path':
     j=json.loads((r/'project.json').read_text());j['repositories']=[{'path':'repositories/../../outside'}];(r/'project.json').write_text(json.dumps(j))
    else:(r/'wiki/README.md').write_text('# Missing metadata')
    self.assertNotEqual(subprocess.run(['python3',str(ROOT/'scripts/check.py'),str(r)],capture_output=True).returncode,0)
