#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import rainflow

def DEL_algorithm(timeseries, neq, m, display_cyclecount = False):
#     Inputs:
#         timeseries: array of datapoints
#         neq: number of equivalent cycles
#         m: Wohler exponent of material
#         display_cyclecount: set as False as default, set True if you want to see the actual rainflow cycle counting

#     Outputs:
#         Seq: Damage equivalent load (DEL) as a float

    dec = 4 # how many decimals should the ranges have
    cycle_count = rainflow.count_cycles(timeseries, ndigits = dec) # cycle counting

    if display_cyclecount == False:
        None
    if display_cyclecount == True:
        print('Range (S), #cycles (n)')
        display(cycle_count)

    # make lists where my ranges and number of cycles will be stored
    list_range = []
    list_cycle = []
    i = 0
    while (i < len(cycle_count)):
        list_range.append(cycle_count[i][0])  # turns the first columm of cycle_count into a seperate list, S_i
        list_cycle.append(cycle_count[i][1])  # turn the second column of cycle_count into a seperate list, n_i
        i += 1

    list_sn = []
    ii = 0
    while (ii < len(cycle_count)):
        list_sn.append((list_range[ii]**m)*list_cycle[ii]) # S_i^m * n_i for i = 1, 2, 3, ..., n
        ii += 1

    sum_sn = sum(list_sn) # sum (S_i^m * n_i)
    S_eq = (sum_sn/neq)**(1/m)
    S_eq = float('{:.4f}'.format(Seq))
    return S_eq
