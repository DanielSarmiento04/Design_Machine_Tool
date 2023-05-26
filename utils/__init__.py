def C_dureza(c_h, c_l, c_t, a, t):
    return c_h + (t + a * c_t) * (c_l - c_h)

def get_razon_espesor(T_l, T_h):
    """
    Description
    -----------

    This function is used to calculate the thickness ratio


    @param T_l is the lower 
    @param T_h  is the higher

    """
    return T_l / (T_l + T_h)

def calculate_c_t(t, q0, q1, q2, q3, *arg):
    if True:
        return q3 * pow(t, 3) + q2 * pow(t, 2) + q1 * t + q0

def calculate_c_r(r, p0, p1, p2, p3, *args):
    return p3 * pow(r, 3) + p2 * pow(r, 2) + p1 * r + p0

def calculate_k_b_prima(j, a_t, a_b, l_t, l_s, E=30e6):

    return pow(1 + j, -1) * (a_t * a_b) / (a_t * l_s + a_b * l_t) * E


def calculate_k_f(d, units='usa')-> float:
    '''
        Description
        -----------
        This function is used to calculate the k_f factor, single bolt fatigue stress concentrator
    '''
    if units == 'usa':
        return 5.7 + 0.6812 * d
    
    return 5.7 + 0.02682 * d

import numpy as np

def calculate_indice_resorte(D:float, d:float):
    '''
        Description
        -----------
        This function is used to calculate the indice resorte
    '''
    return D / d


def calcula_k_s(c):
    '''
        Description
        -----------
        This function is used to calculate the k_s
    '''
    return (2 * c + 1) / (2 * c)

def calculate_cortante(k_s, F, D, d):
    '''
        Description
        -----------
        This function is used to calculate the cortante stress
    '''
    return k_s * ( 8 * F * D ) / ( np.pi * pow(d, 3) )


def calculate_SUT(A, d, m):
    '''
        Description
        -----------
        This function is used to calculate the SUT        
    '''
    return A / pow(d, m)

