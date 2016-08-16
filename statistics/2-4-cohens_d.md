[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
live = df1[df1.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def WeightDifference(live, firsts, others):
    
    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    print('Mean')
    print('First babies', mean1)
    print('Others', mean2)

    print('Variance')
    print('First babies', var1)
    print('Others', var2)

    print('Difference in lbs', mean1 - mean2)
    print('Difference in oz', (mean1 - mean2) * 16)

    print('Difference relative to mean (%age points)', 
          (mean1 - mean2) / mean0 * 100)

    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen d', d)

WeightDifference(live, firsts, others)


"""
WeightDifference(live, firsts, others)
Mean
First babies 7.1469226371951216
Others 7.317793050141148
Variance
First babies 1.969138240507451
Others 1.961434654631706
Difference in lbs -0.17087041294602656
Difference in oz -2.733926607136425
Difference relative to mean (%age points) -2.3608312806530996
Cohen d -0.12189377178120235

Other babies are slightly heavier than first babies however their variance is practically the same.
The live births seem to be slightly heavier in % age points. Cohens d suggests that other births are slightly heavier than first births 

"""

