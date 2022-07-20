'''

##### Trigonometric Calculator by Taylor Series #####

-*- coding: utf-8 -*-

Trigonometry.py
  
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

For more information about the math used here, see:

https://en.wikipedia.org/wiki/Taylor_series
https://pt.wikipedia.org/wiki/S%C3%A9rie_de_Taylor
https://mathworld.wolfram.com/TaylorSeries.html
https://pt.wikipedia.org/wiki/N%C3%BAmeros_de_Bernoulli
https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_zeta_de_Riemann
https://proofwiki.org/wiki/Power_Series_Expansion_for_Real_Arcsecant_Function
https://proofwiki.org/wiki/Power_Series_Expansion_for_Cotangent_Function

'''

pi: int = 3.14159265358979

def factorial(number: int) -> int:       #Most of this functions will use the factorial.
    partial: int = 1
    for fact in range(1, number+1):
        partial = partial*fact
    return partial
    
def Riemann_zeta(s: int, order: int = 250) -> float:      #Needed for the Bernoulli numbers function.
    z: int = 0
    for k in range(1, order):
        z += k**(-s)
    return z
    
def bernoulli_numbers(nb: int) -> float:     #Needed to find the tangent.
    if nb == 0:
        ber: float = 1
    elif nb == 1:
        ber: float = -1/2
    elif nb%2 == 0:
        berP1: float = (-1)**((nb/2)+1) * (2*factorial(nb))
        berP2: float = (2*pi)**(nb)
        berP3: float = Riemann_zeta(nb)
        ber: float = (berP1 / berP2) * berP3
    else:
        ber: float = 0
    return ber

def sine(ang_degrees: float, order: int = 250) -> float:
    ang_radians: float = ang_degrees*pi/180
    sine_ang: float = 0
    for n in range(0, order):
        part1: float = (-1)**n
        part2: float = factorial(2*n+1)
        part3: float = ang_radians**(2*n+1)
        sine_ang += (part1 / part2) * part3
    return sine_ang

def cosine(ang_degrees: float, order: int = 250) -> float:
    ang_radians: float = ang_degrees*pi/180
    cos_ang: float = 0
    for n in range(0, order):
        part1: float = (-1)**n
        part2: float = factorial(2*n)
        part3: float = ang_radians**(2*n)
        cos_ang += (part1 / part2) * part3
    return cos_ang
            
def tangent(ang_degrees: float, order: int = 50):
    if ang_degrees == 0:
        return 0
    ang_radians: float = ang_degrees*pi/180
    if abs(ang_radians) >= (pi/2):
        return None
    else:
        tan_ang: float = 0
        for n in range(0, order):
            part1: float = bernoulli_numbers(2*n) * ((-4)**n) * (1-(4**n))
            part2: float = factorial(2*n)
            part3: float = ang_radians**(2*n-1)
            tan_ang += (part1 / part2) * part3
        return tan_ang

def cotangent(ang_degrees: float, order: int = 50):
    ang_radians: float = ang_degrees*pi/180
    if abs(ang_radians) >= pi or ang_radians == 0:
        return 'Undefined'
    else:
        cotan_ang: float = 0
        for n in range(0, order):
            part1: float = (-1)**n * (2**(2*n)) *  bernoulli_numbers(2*n)
            part2: float = factorial(2*n)
            part3: float = ang_radians**(2*n-1)
            cotan_ang += (part1 / part2) * part3
        return cotan_ang

def secant(ang_degrees: float, order: int = 250) -> float:
    sec_ang: float = 1 / cosine(ang_degrees, order)
    return sec_ang

def cosecant(ang_degrees: float, order: int = 250) -> float:
    if ang_degrees == 0:
        return 'Inf'
    cossec_ang: float = 1 / sine(ang_degrees, order)
    return cossec_ang

def arcsine(arc_value: float, order: int = 250) -> float:
    if abs(arc_value) > 1:
        return None
    arcs_rad: float = 0
    for n in range(0, order):
        part1: float = factorial(2*n)
        part2: float = (4**n) * (factorial(n)**2) * (2*n+1) 
        part3: float = arc_value**(2*n+1)
        arcs_rad += (part1 / part2) * part3
    arcs_graus: float = arcs_rad*180/pi
    return arcs_graus
  
def arccosine(arc_value: float, order: int = 250) -> float:
    if abs(arc_value) > 1:
        return None
    arcc_graus: float = (90) - arcsine(arc_value, order)
    return arcc_graus

def arctangent(arc_value: float, order: int = 50) -> float:
    arct_rad: float = 0
    for n in range(0, order):
        part1: float = (-1)**n
        part2: float = (2*n+1) 
        part3: float = arc_value**(2*n+1)
        arct_rad += (part1 / part2) * part3
    arct_graus: float = arct_rad*180/pi
    return arct_graus

def arccotangent(arc_value: float, order: int = 50) -> float:
    arcctg_graus: float = (90) - arctangent(arc_value, order)
    return arcctg_graus

def arcsecant(arc_value: float, order: int = 250) -> float:
    if abs(arc_value) <= 1:
        return None
    arcsc_rad: float = 0
    for n in range(0, order):
        part1: float = factorial(2*n)
        part2: float = (2**(2*n)) * (factorial(n))**2 * (((2*n)) + 1)
        part3: float = arc_value**((2*n)+1)
        arcsc_rad += part1 / (part2 * part3)
    arcsc_rad = (pi/2) - arcsc_rad
    arcsc_graus: float = arcsc_rad*180/pi
    return arcsc_graus
    
def arccosecant(arc_value: float, order: int = 250) -> float:
    if abs(arc_value) <= 1:
        return None
    arccsc_rad: float = 0
    for n in range(0, order):
        part1: float = factorial(2*n)
        part2: float = (2**(2*n)) * (factorial(n))**2 * (((2*n)) + 1)
        part3: float = arc_value**((2*n)+1)
        arccsc_rad += part1 / (part2 * part3)
    arccsc_graus = arccsc_rad*180/pi
    return arccsc_graus

if __name__ == '__main__':
    print('##### Trigonometric Calculator by Taylor Series #####')
    while True:
        try:
            function: int = int(input('\nEnter the number of the operation:\n1 - Sine\n2 - Cosine\n3 - Tangent\n4 - Cotangent\n5 - Secant\n6 - Cosecant\n7 - Arcsine\n8 - Arccosine\n9 - Arctangent\n10 - Arccotangent\n11 - Arcsecant\n12 - Arccosecant\n0 - Exit\n-> '))
            if function == 0:
                break
            if function == 1:
                in_degrees: float = float(input('What is the angle in degrees for the calculation? '))
                print(f'The sine of {in_degrees} degrees is {sine(in_degrees)}')
            elif function == 2:
                in_degrees: float = float(input('What is the angle in degrees for the calculation? '))
                print(f'The cosine of {in_degrees} degrees is {cosine(in_degrees)}')
            elif function == 3:
                in_degrees: float = float(input('What is the angle in degrees for the calculation (-90 < value < 90)? '))
                print(f'The tangent of {in_degrees} degrees is {tangent(in_degrees)}')
            elif function == 4:
                in_degrees: float = float(input('What is the angle in degrees for the calculation (-180 < value < 180)? '))
                print(f'The cotangent of {in_degrees} degrees is {cotangent(in_degrees)}')
            elif function == 5:
                in_degrees: float = float(input('What is the angle in degrees for the calculation (-90 < value < 90)? '))
                print(f'The secant of {in_degrees} degrees is {secant(in_degrees)}')
            elif function == 6:
                in_degrees: float = float(input('What is the angle in degrees for the calculation (-180 < value < 180)? '))
                print(f'The cosecant of {in_degrees} degrees is {cosecant(in_degrees)}')
            elif function == 7:
                arc: float = float(input('What is the arc value (-1 < value < 1) for the calculation? '))
                print(f'The arcsine of {arc} is {arcsine(arc)} degrees')
            elif function == 8:
                arc: float = float(input('What is the arc value (-1 < value < 1) for the calculation? '))
                print(f'The arccosine of {arc} is {arccosine(arc)} degrees')
            elif function == 9:
                arc: float = float(input('What is the arc value for the calculation? '))
                print(f'The arctangent of {arc} is {arctangent(arc)} degrees')
            elif function == 10:
                arc: float = float(input('What is the arc value for the calculation? '))
                print(f'The arccotangent of {arc} is {arccotangent(arc)} degrees')
            elif function == 11:
                arc: float = float(input('What is the arc value (value < -1 or value > 1) for the calculation? '))
                print(f'The arcsecant of {arc} is {arcsecant(arc)} degrees')
            elif function == 12:
                arc: float = float(input('What is the arc value (value < -1 or value > 1) for the calculation? '))
                print(f'The arccosecant of {arc} is {arccosecant(arc)} degrees')
            else:
                print('Invalid option or angle value.')
        except ValueError:
            print('An error occurred.\nUse only numbers\n')
        
