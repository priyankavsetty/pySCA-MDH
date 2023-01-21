#!/usr/bin/env python
# Author: Priyanka V.Setty
# Date: 2023-01-20
# Usage: functions for SCA analysis
# imports
from __future__ import division

import argparse
import matplotlib.pyplot as plt
import pickle
import json
from json import JSONEncoder
from argparse import ArgumentParser

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def plot_first_order_statistics(Dsca,plot_title):
    
    fig, axs = plt.subplots(1,1, figsize=(9,4))
    xvals = [i+1 for i in range(len(Dsca['Di']))]
    plt.bar(xvals,Dsca['Di'], color='k')
    plt.tick_params(labelsize=11); plt.grid()
    plt.xlabel('Amino Acid Positions', fontsize=12)
    plt.ylabel('Di', fontsize=12)
    plt.title(plot_title)

    return fig
    