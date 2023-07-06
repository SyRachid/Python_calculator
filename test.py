import function as f

def test_add():
    input_1 = 12
    input_2 = 13
    expected_outpout = 25
    try:
        assert f.addition(input_1,input_2) == expected_outpout
        print('addition test case 1 passed')
    except AssertionError:
        print("addition test case 1 failed")
    input_1 = -5
    input_2 = 10
    expected_outpout = 5
    try:
        assert f.addition(input_1,input_2) == expected_outpout
        print('addition test case 2 passed')
    except AssertionError:
        print("addition test case 2 failed")
    input_1 = -5
    input_2 = -5
    expected_outpout = -10
    try:
        assert f.addition(input_1,input_2) == expected_outpout
        print('addition test case 2 passed')
    except AssertionError:
        print("addition test case 2 failed")
    input_1 = -5
    input_2 = 5.5
    expected_outpout = 0.5
    try:
        assert f.addition(input_1,input_2) == expected_outpout
        print('addition test case 4 passed')
    except AssertionError:
        print("addition test case 4 failed")
#test de la fonction difference
def test_sous():
    input_1 = 12
    input_2 = 13
    expected_outpout = -1
    try:
        assert f.soustraction(input_1,input_2) == expected_outpout
        print('soustraction test case 1 passed')
    except AssertionError:
        print("soustraction test case 1 failed")
    input_1 = -5
    input_2 = 10
    expected_outpout = -15
    try:
        assert f.soustraction(input_1,input_2) == expected_outpout
        print('soustraction test case 2 passed')
    except AssertionError:
        print("soustraction test case 2 failed")
    input_1 = -5
    input_2 = -5
    expected_outpout = 0
    try:
        assert f.soustraction(input_1,input_2) == expected_outpout
        print('soustraction test case 2 passed')
    except AssertionError:
        print("soustraction test case 2 failed")
    input_1 = -5
    input_2 = 5.5
    expected_outpout = -10.5
    try:
        assert f.soustraction(input_1,input_2) == expected_outpout
        print('soustraction test case 4 passed')
    except AssertionError:
        print("soustraction test case 4 failed")


