def convert_far_to_cel(F):
    print(f'Enter a temperature in degrees F:{F}')
    C=(F-32)*5/9
    print(f'{F} degrees C={C} degrees C')





def convert_cel_to_far(C):
    print(f'Enter a temperature in degree C:{C}')
    F=C*9/5+32
    print(f'{C} degrees F={F} degree F')