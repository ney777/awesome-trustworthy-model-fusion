"""Ensure local drafts, downloaded full text and credentials are not tracked."""
import subprocess
import sys
from pathlib import Path

paths=subprocess.check_output(['git','ls-files','-z'],text=True).split('\0')
bad=[]
for path in filter(None,paths):
    parts=Path(path).parts
    if parts[0] in ['survey','sources','work'] or Path(path).name.startswith('.env') or Path(path).suffix.lower() in ['.pem','.key']:
        bad.append(path)
if bad:
    print('Private or sensitive paths tracked:\n'+'\n'.join(bad))
    sys.exit(1)
print('Release path check passed: local manuscript and source-download directories are untracked.')
