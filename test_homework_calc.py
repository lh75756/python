import pytest
import yaml

from pythoncode.calculator import Calculator


def get_adddatas():
    with open('./datas/homework_calc.yml',encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['ids']
        return [adddatas,myids]
def get_divdatas():
    with open('./datas/homework_calc.yml',encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        divdatas = mydatas['div']['datas']
        myids = mydatas['div']['ids']
        return [divdatas,myids]

class TestCalculator:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")
        self.calc = Calculator()

    @pytest.mark.parametrize('a,b,expect',get_adddatas()[0],ids=get_adddatas()[1])
    def test_add_case(self,a,b,expect):
        print("这是加法的测试用例")
        result = self.calc.add(a,b)
        assert expect == result
        print("运算成功")
    @pytest.mark.parametrize('a,b,expect',get_divdatas()[0],ids=get_divdatas()[1])
    def test_div_case(self,a,b,expect):
        print("这是除法的测试用例")
        result = self.calc.div(a,b)
        assert expect == result
        print("运算成功")