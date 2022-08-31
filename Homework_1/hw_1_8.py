def Hanoi(rings, pole_1, pole_2, pole_3):
    if rings==1:
        print('Move disc 1 from pole',pole_1,'to pole',pole_2)
        return
    Hanoi(rings-1, pole_1, pole_3, pole_2)
    print('Move disc',rings,'from pole',pole_1,'to pole',pole_2)
    Hanoi(rings-1, pole_3, pole_2, pole_1)

rings = 5
Hanoi(rings, '1', '3', '2')
