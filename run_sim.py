#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 5 2023

@author: jeffreydoering
umdoerij@myumanitoba.ca

This script is part of a project contributing to a PhD research stream at the 
University of Manitoba in the department of Electrical and Computer Engineering
"""

# Import required packages
import sim_setup.sim_iter

# Set values for key simulation variables
n_prods = 5
n_revs = 10
rev_bias = 1
count_bias = 1
prod_qual = 1

# Execute test of simulations
test_sim = sim_setup.sim_iter.review_sim(n_prods = n_prods, 
                                         n_revs = n_revs,
                                         rev_bias = rev_bias, 
                                         count_bias = count_bias, 
                                         prod_qual = prod_qual)
test_sim.step()
print(test_sim.reviews_data)