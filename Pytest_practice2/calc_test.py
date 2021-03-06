import pytest
import yaml

from HW_python.Pytest_practice2.calc import Calculator

# 从.yaml 中读取测试用例
with open('calc.yaml', 'r') as f:
    datas = yaml.safe_load(f)
add_data = datas['add']['add_data']
sub_data = datas['sub']['sub_data']
sub_ids = datas['sub']['sub_ids']
div_data = datas['div']['div_data']
mul_data = datas['mul']['mul_data']


@pytest.fixture(params=add_data)
def get_add_data(request):
    data = request.param
    print(data)
    return data


@pytest.fixture(params=div_data)
def get_div_data(request):
    data = request.param
    print(data)
    return data


@pytest.fixture(params=mul_data)
def get_mul_data(request):
    data = request.param
    print(data)
    return data


@pytest.fixture(params=sub_data)
def get_sub_data(request):
    data = request.param
    print(data)
    return data


class TestCalc(object):
    # 每个类里的方法都会去实例化一个Calculator类
    # def setup(self):
    #     print('start_testing')
    #     # 实例化Calculator类
    #     self.calc = Calculator()
    # def teardown(self):
    #     print('end_starting')

    # TestCalc这个测试类只实例化一次Calculator，且每个类里的方法共用这个Calculator的实例
    def setup_class(self):
        print('start_testing')
        # 实例化Calculator类
        self.calc = Calculator()

    def teardown_class(self):
        print('end_testing')

    # 可以在pytest.ini文件中自定义mark标签，并通过@pytest.mark.[自定义标签]作用到测试用例中
    # 通过终端命令 ptest -vs calc_test.py -k add  中的-k add 来执行某一标签
    @pytest.mark.run(order=1)
    def test_add(self, calculation, get_add_data):

        result = self.calc.add(get_add_data[0], get_add_data[1])
        # 由于python底层的计算处理逻辑  0.30000000000000004 != 0.3， 需要将是浮点数的result 利用round函数保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
        pytest.assume(result == get_add_data[2])

    @pytest.mark.run(order=4)
    def test_div(self, calculation, get_div_data):
        result = self.calc.div(get_div_data[0], get_div_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_div_data[2]

    @pytest.mark.run(order=2)
    def test_sub(self, calculation, get_sub_data):
        assert self.calc.sub(get_sub_data[0], get_sub_data[1]) == get_sub_data[2]

    @pytest.mark.run(order=3)
    def test_mul(self, calculation, get_mul_data):
        result = self.calc.mul(get_mul_data[0], get_mul_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_data[2]
