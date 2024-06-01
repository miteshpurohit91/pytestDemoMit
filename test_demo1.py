import pytest

#Anycode should wrap in one method
#-s keyword will execute logs, -k is for method name filter
#assert is part of pytest
#In pytest We can't have same method name. If we kept it will overwrite previous
#We can mark (tag) tests and then run with -m
#Py test has some predefind mark like, skip: It will skip perticular test,
# xfail mark : It is used when test is executed but that case is not consider into report
@pytest.mark.smoke
def test_greeting():
    msg = "Hi"
    assert msg == "Hi", "Test is fail because condition is not matching"
    print("Hello")


def test_creditcard():
    a=2
    b=4
    assert a+2 == 6, "Addition not match"

#fixture is used like pre request or post request stuff,After yield Post execution methods are run

def test_fixturedemo(setup):
    print("I am original execution Method")