import unittest
import calc

class testCalc(unittest.TestCase):
    
    def testSimpleAdd(self):
        result, msg = calc.calc(1, '+', 1)
        self.assertEqual(result, 2.0)
    
    def testLargeProduct(self):
        result, msg = calc.calc(123456789.0, '*', 987654321.0)
        self.assertEqual(result, 1.2193263111263526e+17)
        
    def testDivByZero(self):
        result, msg = calc.calc(6, '/', 0.0)
        self.assertEqual(msg, 'ZeroDivisionError')

# 创建 test suite
TestSuite = unittest.TestSuite()
# 添加 test 到 suite 中
TestSuite.addTest(testCalc("testSimpleAdd"))
TestSuite.addTest(testCalc("testLargeProduct"))
TestSuite.addTest(testCalc("testDivByZero"))
# 创建 Test runner
runner = unittest.TextTestRunner()
# 执行测试
runner.run(TestSuite)