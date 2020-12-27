# create and run unit tests in Python,
# instead of invoking this function manually within this script and then running
# it and manually checking the console will be writing unit tests. We use the unit test module from Python,
# which is inbuilt into Python. 

import unittest
from CodeToTest import *

class CreditClassValidationTest(unittest.TestCase):
    # to setup some data and clean up the data after the test we use setup block and teardown block
    # setup and teardown is invoked before and after every test, helps in cleanup and no intermix 
    def setUp(self): # by default it has nothing we override the function
        print("Setup")

    def test_validateCard_valid(self):
        result=validateCard(date(2022,2,2))
        self.assertEqual('Valid',result)

    # when the code to test return an output instead on raising an error use this
    # def test_validateCard_expired(self):
    #     result=validateCard(date(2020,2,2))
    #     self.assertEqual('Expired',result)

    # when raising an error in else block
    def test_validateCard_expired(self):
        with self.assertRaises(RuntimeError): # expecting run time error when passing invalidate date
            validateCard(date(2020,2,2))
            # this passes when 2020 but when 2022 the runtime error is never raised thus it fails

    def tearDown(self): # by default it has nothing we override the function
        print("Tear Down")



# # If you are using a text editor etc use this if block else pycharm does the same as shown below
if __name__=="__main__":
    unittest.main()

# # whenerver we run a python script it convert it to main script and run, thus when this line is checked with the name == main method
# # it execute the unittest.main first

# but pycharm doesn't require this block


# the output would be number of dots depending on the nnumber of test we are running in the unit test
