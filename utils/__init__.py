'''
    Tornillos y pernos
'''
import pandas as pd

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

def calculate_torque_subida(P, dp, µ, L):
    pass

def get_row_values(df:pd.DataFrame, j:float):
    '''
        Description
        -----------
        This function is used to get the values of a row in a data frame
        
        @param df is the table
        @param j is the value of the row
    '''
    
    row = df.loc[df['j'] == j]
    if len(row) > 0:
        return row.iloc[0][1:].to_numpy()
    
    upper_values = df.loc[df['j'] > j].iloc[0] [1:].to_numpy()
    lower_values = df.loc[df['j'] < j].iloc[-1] [1:].to_numpy()

    upper_j = df.loc[df['j'] > j].iloc[0] [:1].to_numpy()
    lower_j = df.loc[df['j'] < j].iloc[-1] [:1].to_numpy()

    return (j - lower_j) / (upper_j - lower_j) * (upper_values - lower_values) + lower_values
