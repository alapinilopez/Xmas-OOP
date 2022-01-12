from src.DNI import DNI
import pytest

@pytest.mark.DNI_check
def test_DNI_check():
    assert True == DNI("45371634Z").DNI_check()
    assert True == DNI("43051598S").DNI_check()
    assert False == DNI("43734").DNI_check()
    