import pytest
import yaml
from HW_python.Pytest_practice1.calc import Calculator

# 从.yaml 中读取测试用例
with open('calc.yaml', 'r') as f:
    datas = yaml.safe_load(f)
add_data = datas['add']['add_data']
sub_data = datas['sub']['sub_data']
sub_ids = datas['sub']['sub_ids']
div_data = datas['div']['div_data']


class TestCalc(object):
    def setup(self):
        self.calc = Calculator()
        print('开始计算')

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize(
        "a, b, expect",
        add_data,
                             )
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        # 由于python底层的计算处理逻辑  0.30000000000000004 != 0.3， 需要将是浮点数的result 利用round函数保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 将从.yaml文件中读取的sub测试用例传入参数化的装饰器中
    @pytest.mark.parametrize(
        'a, b, expect',
        sub_data,
        ids=sub_ids
                            )
    def test_sub(self, a, b, expect):
        assert self.calc.sub(a, b) == expect

    def test_mul(self):
        assert self.calc.mul(3, 2) == 6

    @pytest.mark.parametrize(
        'a, b, expect',
        div_data,
                             )
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect

