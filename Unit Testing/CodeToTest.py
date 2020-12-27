from datetime import *
def validateCard(expDate):
    if expDate>datetime.now().date():
        return 'Valid'
    # else:
    #     return 'Expired'
    else:
        raise RuntimeError('Card has expired')
    
    
# print(validateCard(date(2022,2,2))) -- no need of this statement cause we checking this in the unit test

# THIS CODE NEED TO BE CHECKED IF IT'S CORRECT OR NOT
# done in UnitTest.py
