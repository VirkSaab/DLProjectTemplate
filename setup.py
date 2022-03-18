from setuptools import setup, find_packages
from dlp import CNF_PATH
from dlp.utils import load_yaml
CNF = load_yaml(CNF_PATH)

PROJ_NAME = CNF.project_name.lower()

VERSION = '0.0.1'

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()
    
setup(
    name=f"{PROJ_NAME}",
    version=VERSION,
    description='My End-to-End Deep Learning Project',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['ez_setup', 'tests', '.github']),
    include_package_data=True,
    entry_points=f"""
        [console_scripts]
        {PROJ_NAME}={PROJ_NAME}.main:cli
    """,
)
