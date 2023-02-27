import os

import pytest
from utils.base_session import BaseSession
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture(scope="session")
def examp_api():
    return BaseSession(os.getenv("REG_API"))

