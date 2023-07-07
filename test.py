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
   

#test de la multiplication
def test_mul():
    input_1 = 12
    input_2 = 11
    expected_outpout = 132
    assert f.multiplication(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 10
    expected_outpout = -50
    assert f.multiplication(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = -5
    expected_outpout = 25
    assert f.multiplication(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 5.5
    expected_outpout = -27.5
    assert f.multiplication(input_1,input_2) == expected_outpout
#test division
def test_division():
    input_1 = 11
    input_2 = 11
    expected_outpout = 1
    assert f.division(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 10
    expected_outpout = -0.5
    assert f.division(input_1,input_2) == expected_outpout
    input_1 = -25
    input_2 = -5
    expected_outpout = 5
    assert f.division(input_1,input_2) == expected_outpout
    input_1 = -27.5
    input_2 = 5.5
    expected_outpout = -5
#test pour la fonction puissance
def test_pow():
    input_1 = 5
    input_2 = 2
    expected_outpout = 25 
    assert f.puissance(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 3
    expected_outpout = -125
    assert f.puissance(input_1,input_2) == expected_outpout
    input_1 = -5
    input_2 = 2
    expected_outpout = 25
    assert f.puissance(input_1,input_2) == expected_outpout
    input_1 = 1
    input_2 = 2
    expected_outpout = 1
    assert f.puissance(input_1,input_2) == expected_outpout
    