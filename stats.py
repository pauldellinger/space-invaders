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
        "Max" : maxx,
        "Min" : minn,
        "Average" : avg,
        "Standard Deviation" : std
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
    fig, ax1 = plt.subplots()
    fig.set_size_inches(16,9)
    ax1.set_title(title)
    ax1.set_xlabel(xaxis)
    ax1.set_ylabel(yaxis)
    return fig, ax1



def add_lines(fig, ax1, compiled_results):
    """
    Compiled results is tuple with
    [([Xs], [Ys], label)]
    """
    for x, y, label in compiled_results:
        ax1.plot(x, y, alpha=0.9, label=label)

    fig.legend(loc='upper right', ncol=1)
    return ax1

if __name__ == '__main__':

    
    avgScores = ([[1, 2, 3, 4], [100, 110, 340, 560], '0.2'],
                [[1, 2, 3, 4], [140, 400, 410, 450], '0.4'])
    fig, ax = make_plot('Varying mutation rate', 'generations', 'avg score')
    add_lines(fig, ax, avgScores)
    save_plot(fig, 'exampleavgscore')
