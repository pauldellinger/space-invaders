from matplotlib import pyplot as plt
from pylab import figure, axes, pie, title, show
import numpy as np

def save_plot(chart, path):
    chart.savefig('plots/' + path + '.png', bbox_inches='tight')
    chart.savefig('plots/' + path + '.pdf', bbox_inches='tight')

def save_array(arr, path):
    np.savetxt("results/" + path + '.csv', arr, delimiter=",")

def generation_stats(strategies):
    """
    Type [(score, strategy)]
    Return average, 
    max, 
    standard deviation, 
    varaiance of populations

    """
    pass

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
