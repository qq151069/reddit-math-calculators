# Copyright (c) 2018, qq151069
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


"""Reddit premise
You wake up tomorrow in the year 1518.
You can't die from old age or disease, but physical injury can still kill you.
Every time you die you travel 50 years into the past. 
Another 50 years is added for each time you die so if you've died 3 times
and die a 4th time you get sent back 200 years. 
Will you ever make it back?"""

import numpy as np
import datetime
import random

numPeons = 1e3
startYear = 1518
baseDeathRate = 600 # in units of micromort
                    # https://en.wikipedia.org/wiki/Micromort

# penalty = multiplierPenalty * numDeaths + additivePenalty
multiplierPenalty = 50
additivePenalty = 0

    
def life(startYear,finalYear,cutoffYear=0):

    currentYear = startYear
    elapsedYears = 0
    counter = 1

    while(currentYear < finalYear):
        # If your number is up, "die" and teleport back home
        if(random.random() <= annualDeathRate):
            currentYear -= (counter * multiplierPenalty + additivePenalty)
            counter += 1
        currentYear += 1
        elapsedYears += 1
  
        # To speed up the calculation, return early if peon jumps back
        # before time period
        if(currentYear <= cutoffYear):
            return((counter-1,currentYear,elapsedYears))
    
    return((counter-1,currentYear,elapsedYears))

def test():
    now = datetime.datetime.now()
    finalYear = now.year
    a,b = [],[]
    numSuccess = 0
    for i in range(int(numPeons)):
        aa,bb,cc = life(startYear,finalYear)
        if(bb == 2018):
            a.append(aa)
            b.append(cc)
            numSuccess += 1
    survivalRate = (numSuccess) * 100.0/numPeons
    return("Survival rate: {:1.2f}%; ".format(survivalRate) + \
           "Avg num deaths: {:1.1f}; ".format(np.average(a)) + \
           "Avg years elapsed: {:1.0f}".format(np.average(b)))

if __name__ == "__main__":
    for i in range(1,21,1):
        annualDeathRate = i * baseDeathRate * 1.0/1e6
        print("Death rate multiplier: {:d}\t\t{:s}".format(i,test()))
