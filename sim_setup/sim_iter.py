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
from collections import namedtuple
import csv
import pandas as pd
import random

# Configuring a class to contain our iterative simulation code
class review_sim(*, n_revs, n_prods, prod_qual,rev_bias, count_bias):
    
    """
    Class to manage iterative product purchase and review simulations
    
    General info:
        1. Assume some number of like products exist in a market (e.g., TVs)
        2. Assume consumers are reading reviews online prior to purchasing
        3. Assume past review valence (positivity) and number of previous
            reviews left both info the purchase decision
        4. Simulation n number of purchase cycles
        5. ID network level effects of review bias on total market state (i.e.,
            which TV sold most)
        
    Arguments (all args are kwargs):
    n_revs = number of reviews (steps) we are simulation
    n_prods = number of comparable products in the market
    prod_qual = coefficient to ancher product quality
    rev_bias = coefficient to skew purchase decision based on past review
        valence
    count_bias = coeffient to skew purchase decision based on number
        of purchases of the product to date (# review left/visible)
    """
    
    # Instantiate key model features and data storage
    def __init__(self):
        
        # Set number of products in market
        n_prods = n_prods
        
        # Set dataframe to store iterative data for easy analysis later
        col_names = ['step']
        for i in range(0, n_prods):
            col_names.append("product_%s" % i)
        
        sim_data = pd.DataFrame(columns)
        
    # Instantiate step-wise
    def step(self):

        # Set number of products in market
        n_prods = n_prods

        # Set number of iteration in the simulation
        n_revs = n_revs
                
        # Set review bias
        rev_bias = rev_bias
        
        # Set review count bias
        count_bias = count_bias
        
        # Set product quality anchor
        prod_qual = prod_qual
        
        # Iterate through model steps
        step_counter = 0
        
        for review in range(0, n_revs):
            
            # Account for first, unbiased step
            if step_counter == 0:
                
                
            
            else:
                
                
                
        return sim_data