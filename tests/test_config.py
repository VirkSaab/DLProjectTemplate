import pytest
from pathlib import Path
from dlp import CNF_PATH
from dlp.utils import load_yaml

# * this function loads the config file for the tests.
@pytest.fixture
def CNF():
    return load_yaml(CNF_PATH)

def test_config(CNF):
    """Check if the config file is loaded correctly."""
    # Check project name
    assert CNF.project_name == "DLP"