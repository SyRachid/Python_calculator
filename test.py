import function as f

def test_add():
    input_1 = 12
    input_2 = 13
    expected_outpout = 25
    assert f.addition(input_1,input_2) == expected_outpout
     
    input_1 = -5
    input_2 = 10
    expected_outpout = 5
   
    assert f.addition(input_1,input_2) == expected_outpout
   
    input_1 = -5
    input_2 = -5
    expected_outpout = -10
    assert f.addition(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 5.5
    expected_outpout = 0.5
    assert f.addition(input_1,input_2) == expected_outpout

#test de la fonction difference
def test_sous():
    input_1 = 12
    input_2 = 13
    expected_outpout = -1
    assert f.soustraction(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 10
    expected_outpout = -15
    assert f.soustraction(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = -5
    expected_outpout = 0
    assert f.soustraction(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 5.5
    expected_outpout = -10.5
    assert f.soustraction(input_1,input_2) == expected_outpout
   
"""
#test de la multiplication
def test_mul():
    input_1 = 12
    input_2 = 11
    expected_outpout = 132
    assert f.multiplication(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 10
    expected_outpout = -50
    try:
        assert f.multiplication(input_1,input_2) == expected_outpout
        print('multiplication test case 2 passed')
    except AssertionError:
        print("multiplication test case 2 failed")
    input_1 = -5
    input_2 = -5
    expected_outpout = 25
    try:
        assert f.multiplication(input_1,input_2) == expected_outpout
        print('multiplication test case 3 passed')
    except AssertionError:
        print("multiplication test case 3 failed")
    input_1 = -5
    input_2 = 5.5
    expected_outpout = -27.5
    try:
        assert f.multiplication(input_1,input_2) == expected_outpout
        print('multiplication test case 4 passed')
    except AssertionError:
        print("multiplication test case 4 failed")

#test division
def test_division():
    input_1 = 11
    input_2 = 11
    expected_outpout = 1
    try:
        assert f.division(input_1,input_2) == expected_outpout
        print('division test case 1 passed')
    except AssertionError:
        print("division test case 1 failed")
    input_1 = -5
    input_2 = 10
    expected_outpout = -0.5
    try:
        assert f.division(input_1,input_2) == expected_outpout
        print('division test case 2 passed')
    except AssertionError:
        print("division test case 2 failed")
    input_1 = -25
    input_2 = -5
    expected_outpout = 5
    try:
        assert f.division(input_1,input_2) == expected_outpout
        print('division test case 3 passed')
    except AssertionError:
        print("division test case 3 failed")
    input_1 = -27.5
    input_2 = 5.5
    expected_outpout = -5
    try:
        assert f.division(input_1,input_2) == expected_outpout
        print('division test case 4 passed')
    except AssertionError:
        print("division test case 4 failed")
    input_1 = 13
    input_2 = 0
    try:
        f.division(input_1,input_2) 
    except ValueError:
        print('division test case 5 passed ')
    else:
        print('division test case 5 failed')

test_division()
print("")
test_mul()
print("")
test_add()
print("")
test_sous()
"""