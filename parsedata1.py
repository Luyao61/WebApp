import numpy as np
from numpy import genfromtxt
from polls.models import EyewitnessStimuli
data = genfromtxt('polls/files/O3.txt', dtype=str, names=None, delimiter='\t')
for line1 in data:
    q1 = EyewitnessStimuli(score=line1[0].astype(np.int), lineup_race=line1[2], lineup_number=line1[3],
                           category=line1[4], statement=line1[5], chosen_face=line1[6].astype(np.int),
                           lineup_order=line1[7])
    q1.save()
