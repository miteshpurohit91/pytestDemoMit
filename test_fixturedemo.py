import pytest

@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_fixturedemo(self):
        print("This is fixture demo class")

    def test_fixturedemo2(self):
        print("This is fixture demo method2")
