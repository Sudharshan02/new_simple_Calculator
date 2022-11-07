import unittest

def sum(x, y):
    return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by Zero!')
    return x/y



class calculator_Test(unittest.TestCase):

    def setUp(self):
        print('Setup Called.....')
        #Arrange
        self.x = 10
        self.y = 20



    def test_cal_test_func1(self):
        print('Test1 Called...')

        #Arrange
        #x = 10
        #y = 20
        #act
        result = sum(self.x, self.y)
        result1 = subtract(self.x, self.y)
        result2 = multiply(self.x, self.y)
        result3 = divide(self.x, self.y)


        #Assert

        self.assertEqual(result, self.x + self.y)
        self.assertEqual(result1, self.x - self.y)
        self.assertEqual(result2, self.x * self.y)
        self.assertEqual(result3, self.x / self.y)



    def test_cal_test_func2(self):
        print('Test 2 called.....')
        # Arrange
        #x = 10
        #y = 20
        # act
        result = sum(self.y, self.x)
        result1 = subtract(self.y, self.x)
        result2 = multiply(self.y, self.x)
        result3 = divide(self.y, self.x)

        # Assert

        self.assertEqual(result, self.y + self.x)
        self.assertEqual(result1, self.y - self.x)
        self.assertEqual(result2, self.y * self.x)
        self.assertEqual(result3, self.y / self.x)


if __name__ == "__main__":
    unittest.main()








