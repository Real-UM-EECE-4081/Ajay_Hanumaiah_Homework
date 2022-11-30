

AbZeroC = float(-273.15)
AbZeroF = float(-459.67 )

def convert_to_F(C):
    if C <= AbZeroC :
        raise ValueError("ERROR: Temperature below absolute 0!")
    else:
        F = float((C*1.8)+32)
        return F

def convert_to_C(F):
    if F <= AbZeroF:
        raise ValueError("ERROR: Temperature below absolute 0!")
    else:
        C = float((F-32) * 1/8)
        return C
        

