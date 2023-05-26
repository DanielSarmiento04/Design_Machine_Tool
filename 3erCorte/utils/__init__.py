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

