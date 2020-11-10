from matplotlib import pyplot as plt
from pylab import figure, axes, pie, title, show
import numpy as np

def save_plot(chart, path):
    chart.savefig('plots/' + path + '.png', bbox_inches='tight')
    chart.savefig('plots/' + path + '.pdf', bbox_inches='tight')

def save_array(arr, path):
    np.savetxt("results/" + path + '.csv', arr, delimiter=",")

def generation_stats(strategy):
        
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