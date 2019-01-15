#!/usr/bin/env python3
import os
from setuptools import setup

from pathlib import Path

thisDir = Path(__file__).parent

formatsPath = thisDir / "kaitai_struct_formats"
kaitaiSetuptoolsCfg = {
	"formats": {
		"cpython_frozen_table.py": {"path": "database/cpython_frozen_table.ksy"}
	},
	"formatsRepo": {
		"git": "https://github.com/KOLANICH/kaitai_struct_formats.git",
		"refspec": "cpython_frozen_table",
		"localPath": formatsPath,
		"update": True,
	},
	"outputDir": thisDir / "FrozenTable",
	"inputDir": formatsPath,
	'flags':{
		"readStoresPos": True,
	}
}

setup(use_scm_version=True, kaitai=kaitaiSetuptoolsCfg)
