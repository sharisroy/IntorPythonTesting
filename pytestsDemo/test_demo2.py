# before run
#   1. Edit Configuration > plus(+) sign > Python Test > Pytest
#   2. If show error "No pytest runner found in selected interpreter" import pytest
import pytest


#   Run from terminal
#   1. go to project folder(/Python/PythonTesting/pytestsDemo)
#   2. run: py.test / py.test -v / py.test -v -s
#   3. run: py.test file name (ex: py.test test_demo1.py) for run single file
#   4. run: py.test -k method Name (ex : py.test -k Haris -v -s ) for run selected method
#   5. run : py.test -m group name -v -s (py.test -m smoke -v -s) for run group wise

# -k stands for method execution, -s logs in out put, -v stands for more information metadata

@pytest.mark.xfail # failed but not in the report
def test_secondMethods():
    message = 'second'
    assert message == "second Methods", "Test failed because condition do not match"
    # print("second Methods")

@pytest.mark.smoke
def test_Haris():
    print("print from demo 2")
