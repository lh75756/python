import pytest
@pytest.fixture(scope="module")
def Fixture():
    print("开始计算")
    yield
    print("结束运算")