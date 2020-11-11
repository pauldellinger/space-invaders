from matplotlib import pyplot as plt
from pylab import figure, axes, pie, title, show
import numpy as np
import statistics

def save_plot(chart, path):
    chart.savefig('plots/' + path + '.png', bbox_inches='tight')
    chart.savefig('plots/' + path + '.pdf', bbox_inches='tight')

def save_array(arr, path):
    np.savetxt("results/" + path + '.csv', arr, delimiter=",")


# Gen Stats.
def fetch_generation_stats(strategies):
    # Extract.
    scores = [t[0] for t in strategies]
    
    # Compute.
    maxx = max(scores)
    minn = min(scores)
    avg = sum(scores) / float(len(scores))
    std = statistics.stdev(scores)

    # Construct.
    d = {
        "max" : maxx,
        "min" : minn,
        "avg" : avg,
        "std" : std
    }

    # Ret.
    return d



# Sim Stats.
def fetch_simulation_stats(generations):
    # Init.
    allStats = []
    
    # Each Gen.
    for generation in generations:
        # This Stats.
        thisStats = fetch_generation_stats(generation)

        # Append.
        allStats.append(thisStats)
    
    # Ret.
    return allStats






        
if __name__ == '__main__':
    # figure(1, figsize=(6, 6))
    # ax = axes([0.1, 0.1, 0.8, 0.8])

    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # fracs = [15, 30, 45, 10]

    # explode = (0, 0.05, 0, 0)
    # pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    # title('Raining Hogs and Dogs', bbox={'facecolor': '0.8', 'pad': 5})
    # save_plot(plt, 'example')
    arr = np.array([[1,2],[3,4]])
    save_array(arr, 'example')