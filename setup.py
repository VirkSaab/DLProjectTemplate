from setuptools import setup, find_packages

VERSION = '0.0.1'

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()
    
setup(
    name=f"dlp",
    version=VERSION,
    description='My End-to-End Deep Learning Project',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['ez_setup', 'tests', '.github']),
    include_package_data=True,
    entry_points=f"""
        [console_scripts]
        mvqag=dlp.main:cli
    """,
)
