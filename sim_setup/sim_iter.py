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
import numpy
import pandas as pd
import random
from scipy.special import softmax
import statistics

# Configuring a class to contain our iterative simulation code
class review_sim:
    
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
    def __init__(self, n_prods, n_revs, rev_bias, count_bias, prod_qual):
        
        # Set number of products in market
        self.n_prods = n_prods

        # Set number of iteration in the simulation
        self.n_revs = n_revs
                
        # Set review bias
        self.rev_bias = rev_bias
        
        # Set review count bias
        self.count_bias = count_bias
        
        # Set product quality anchor
        self.prod_qual = prod_qual

        # Dynamically set quality values for all products
        qual_vals = []
        rand_vals = softmax([round(random.random(), 2)\
                             for x in range(0, self.n_prods)])
        for i in range(0, self.n_prods):
            qual_vals.append(tuple(["product_%s" % str(i + 1), rand_vals[i]]))
        self.qual_vals = qual_vals
    
        # Dynamically set dataframe columns, based on number of products
        col_names = ['step']      # Adding to this in a moment
        for i in range(1, self.n_prods + 1):
            col_names.append("product_%s" % i)
        self.reviews_data = pd.DataFrame(columns = col_names)
        
        # Dynamically set storage object for purchase probabilities
        prob_col_names = ['step']
        for i in range(1, self.n_prods + 1):
            prob_col_names.append("product_%s" % i)
        self.prob_data = pd.DataFrame(columns = prob_col_names)
    
    # Instantiate step-wise simulation
    def step(self):

        # Set step count
        step_counter = 0

        # Iterate through model steps
        for i in range(0, self.n_revs):

            if step_counter == 0:     # Accounting for first sim step
                
                # Choose product based on product quality scores
                prod_choice = numpy.random.choice(numpy.arange(0, self.n_prods), 
                                   p=[x[1] for x in self.qual_vals])
                prod_choice_name = self.qual_vals[prod_choice][0]

                # Save new review to reviews dataframe
                new_row = {"step": step_counter + 1,
                           "%s" % prod_choice_name: random.randrange(1, 5)}
                self.reviews_data = self.reviews_data.append(new_row, 
                                                             ignore_index=True)

                # Save new review probabilities to reviews dataframe
                new_row_prob = [step_counter + 1]
                new_row_prob.extend([x[1] for x in self.qual_vals])
                self.prob_data = self.prob_data.append(pd.DataFrame([new_row_prob],
                                             columns = self.prob_data.columns))

            else:     # Accounting for all sim steps >1

                # Collect info on current review counts
                rev_counts = []
                for product in range(1, self.n_prods + 1):
                    rev_counts.append(len(self.reviews_data) - \
                                      self.reviews_data['product_%s' % \
                                      product].isna().sum())
                rev_counts = softmax(rev_counts)

                # Collect info on current review valences
                avg_scores = []
                for product in range(1, self.n_prods + 1):
                    avg_scores.append(numpy.mean(self.reviews_data\
                                                 ['product_%s' % product]))
                avg_scores = numpy.nan_to_num(avg_scores).tolist()
                avg_scores = softmax(avg_scores)

                # Grab most recent purchase probabilites weights
                last_prob_vals = self.prob_data.iloc[-1][1:].tolist()

                # Combine indexes to get new purchase probabilities
                new_prob_scores = []
                for counts, scores, last_prob in zip(rev_counts, avg_scores, 
                                                     last_prob_vals):
                    vals = [counts, scores, last_prob]
                    new_prob_scores.append(statistics.mean(vals))

                # Choose new product to purchase, and save data
                prob_tuples = []
                for i in range(0, self.n_prods):
                    prob_tuples.append(tuple(["product_%s" % str(i + 1), 
                                              new_prob_scores[i]]))
                prod_choice = numpy.random.choice(numpy.arange\
                           (0, self.n_prods), p=[x[1] for x in prob_tuples])
                prod_choice_name = prob_tuples[prod_choice][0]
                new_row = {"step": step_counter + 1,
                           "%s" % prod_choice_name: random.randrange(1, 5)}
                self.reviews_data = self.reviews_data.append(new_row, 
                                                             ignore_index=True)
                
                # Save new review probabilities to reviews dataframe
                new_row_prob = [step_counter + 1]
                new_row_prob.extend([x[1] for x in prob_tuples])
                self.prob_data = self.prob_data.append(pd.DataFrame([new_row_prob],
                                             columns = self.prob_data.columns))
                
            # Progress counter and finalize
            step_counter += 1
            
        return self.reviews_data
        return self.prob_data