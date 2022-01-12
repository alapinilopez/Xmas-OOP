from src.DNI import DNI
import pytest

@pytest.mark.DNI_healthy
def test_DNI_healthy():
    assert False == DNI("ABC456789").DNI_healthy
    assert True == DNI("45371634Z").DNI_healthy