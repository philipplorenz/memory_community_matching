#!/usr/bin/env python3


from matching import matching



timeseries = [

        { 'orange': { 1, 2, 3 },
          'violet': { 4, 5, 6 },
          'green':  { 7, 8, 9 } },

        { 'violet': { 2, 3, 4, 5, 6 },
          'green':  { 7, 8 },
          'yellow': { 9 } },

        { 'orange': { 1, 2, 3 },
          'violet': { 4, 5, 6, 7 },
          'green':  { 8, 9 } }

    ]

correct_temporal_communities = [{(0, 'violet'), (1, 'violet'), (2, 'violet')}, {(0, 'orange'), (2, 'orange')}, {(2, 'green'), (1, 'green'), (0, 'green')}]

# see figure 6 in paper



temporal_communities = matching(timeseries, 2)

print(temporal_communities)


# test if results are identical
found = set()
for temp_comm in temporal_communities:

    for i, correct_temp_comm in enumerate(correct_temporal_communities):

        if temp_comm == correct_temp_comm:
            found.add(i)
            break
    else:
        raise Exception('wrong communtity found')

if len(found) < len(correct_temp_comm):
    raise Exception('some communities not found')
