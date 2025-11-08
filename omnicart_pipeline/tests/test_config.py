import tempfile
import os
import pytest
from configparser import ConfigParser
from omnicart_pipeline.config import ConfigManager  # replace 'your_module' with the actual filename (without .py)

@pytest.fixture
def config():
    return ConfigManager('pipeline.cfg')

def test_get_load_base_url(config):
    assert config.get_load_base_url() == 'https://fakestoreapi.com/'

def test_get_load_limit(config):
    assert config.get_load_limit() == 5


