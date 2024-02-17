# before run
#   1. Edit Configuration > plus(+) sign > Python Test > Pytest
#   2. If show error "No pytest runner found in selected interpreter" import pytest

#   Run from terminal
#   1. go to project folder(/Python/PythonTesting/pytestsDemo)
#   2. run: py.test / py.test -v / py.test -v -s
#   3. run: py.test file name (ex: py.test test_demo1.py) for run single file
#   4. run: py.test -k method Name (ex : py.test -k Haris -v -s ) for run selected method
#   5. run : py.test -m group name -v -s (py.test -m smoke -v -s) for run group wise

# -k stands for method execution, -s logs in out put, -v stands for more information metadata

# HTML report
#   1. pip install pytest-html install package
#   2. run: py.test --html=reportName.html -s -v

import pytest


def test_firstProgram(setup):
    print("hello")


@pytest.mark.smoke
def test_firstMethods():
    print("first Methods")

@pytest.mark.skip
def test_Haris():
    print("print from demo 1")



