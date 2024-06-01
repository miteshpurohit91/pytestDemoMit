import pytest


@pytest.mark.smoke
def test_creditcard2(setup):
    msg = "Hi"
    assert msg == "Hi", "Test is fail because condition is not matching"
    print("Hello")