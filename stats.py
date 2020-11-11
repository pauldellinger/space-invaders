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


def make_plot(title, xaxis, yaxis):
    """
    plt = stats.make_plot(asdf)
    plt.addlines(asdf)
    stats.save_plot(plt, path)
    """
    figure(1, figsize=(16, 9))
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    return plt



def add_lines(plt, compiled_results):
    """
    Compiled results is tuple with
    [([Xs], [Ys], label)]
    """
    for x, y, label in compiled_results:
        plt.plot(x, y,  alpha=0.9, label=label)

    plt.legend(loc=2, ncol=len(compiled_results))
    return plt

if __name__ == '__main__':

    
    avgScores = ([[1, 2, 3, 4], [100, 110, 340, 560], '0.2'],
                [[1, 2, 3, 4], [140, 400, 410, 450], '0.4'])
    plt = make_plot('Varying mutation rate', 'generations', 'avg score')
    add_lines(plt, avgScores)
    save_plot(plt, 'exampleavgscore')
