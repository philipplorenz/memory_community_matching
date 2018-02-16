#!/usr/bin/env python3

import os
import sys
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt


# allow importing module from within
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from memory_community_matching import matching



# dataset
folder = '../Daily_Groups'
filename = 'community_tags{}_2015_list.txt'


tags = set()


for i in range(1, 363):
    
    #data = np.loadtxt(os.path.join(folder, filename.format(i)), dtype=int, delimiter=',', usecols=(0,1))
    
    with open(os.path.join(folder, filename.format(i))) as f:
        
        for line in f:
            
            _, community, tag = map(str.strip, line.split(','))
            
            tags.add(tag)
            
    
tags_dict = {}
tags_reverse_dict = {}
for i, tag in enumerate(tags):
    tags_dict[i] = tag
    tags_reverse_dict[tag] = i
    

timeseries = []

for i in range(1, 363):
    
    with open(os.path.join(folder, filename.format(i))) as f:
        
        communities = defaultdict(set)
        
        for line in f:
            
            _, community, tag = map(str.strip, line.split(','))
            
            communities[int(community)].add(tags_reverse_dict[tag])
            
        timeseries.append(communities)
            
            
temporal_communities = matching(timeseries, memory=2)

print('Found {} temporal communities'.format(len(temporal_communities)))
print('Longest temporal community lasts {} timesteps'.format(max(map(len, temporal_communities))))

plt.hist(list(map(len, temporal_communities)), 20)
plt.savefig('temporal_community_length_hist.png')


