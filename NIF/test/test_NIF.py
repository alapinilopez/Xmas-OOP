from src.NIF import NIF
import pytest

@pytest.mark.NIF
def test_NIF():
    assert "Z" == NIF.get_char(45371354)
    assert "S" == NIF.get_char(43051598)