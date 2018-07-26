from django.test import TestCase, Client

# Create your tests here.

from .models import User

class UserModelTest(TestCase):

    def test_calc(self):
        user = User()
        # 编写测试用例首先要明确要测试的方法 or 函数要返回的结果，然后编写测试断言期望结果是否与返回结果相同
        # 保证测试的方法 or 函数永远是符合预期的
        self.assertIs(user.calc(3, 6), True)    # 期望返回 True，结果返回 True，测试 ok
        # self.assertIs(user.calc(3, 4), False)    # 期望返回 False，结果返回 False，测试 ok