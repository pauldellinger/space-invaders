import os
import pickle
import json
from stats import *
from datetime import datetime


paths = (

    'strategies/20201117-173256/[0.1, 0.25, 2, 50]/[0.1, 0.25, 2, 50]-sim-results',
    'strategies/roy_strategies/[0.01, 0.25, 2, 50]/[0.01, 0.25, 2, 50]-sim-results',
    'strategies/roy_strategies/[0.02, 0.25, 2, 50]/[0.02, 0.25, 2, 50]-sim-results',
    'strategies/roy_strategies/[0.03, 0.25, 2, 50]/[0.03, 0.25, 2, 50]-sim-results',
    'strategies/roy_strategies/[0.04, 0.25, 2, 50]/[0.04, 0.25, 2, 50]-sim-results',
    'strategies/roy_strategies/[0.05, 0.25, 2, 50]/[0.05, 0.25, 2, 50]-sim-results',
    'strategies/roy_strategies/[0.06, 0.25, 2, 50]/[0.06, 0.25, 2, 50]-sim-results',
    'strategies/20201117-135235/[0.07, 0.25, 2, 50]/[0.07, 0.25, 2, 50]-sim-results',
    'strategies/20201117-173256/[0.08, 0.25, 2, 50]/[0.08, 0.25, 2, 50]-sim-results',
    'strategies/20201117-173256/[0.09, 0.25, 2, 50]/[0.09, 0.25, 2, 50]-sim-results',
)
variable ='Mutation Rate'

all_results = []
for sim_folder in paths:
    sim_results = []
    generation_folders = sorted([entry.path for entry in os.scandir(sim_folder) 
        if '.p' not in entry.path and 'DS' not in entry.path], key=lambda x: int(x.split("/")[-1]))
    for entry in generation_folders[:100]:
        print(entry)
        if '.p' not in entry and 'DS' not in entry:
            generation_results = []
            for strat in os.scandir(entry):
                score = strat.path.split(".p")[0].split("/")[-1]
                strategy = pickle.load(open(strat, 'rb'))
                generation_results.append((int(score), strategy))
            print(len(generation_results))
            sim_results.append(generation_results)
    print(len(sim_results))
    all_results.append(sim_results)
print(len(all_results))

allSimStats = []
varLst = []
for folder, sim in zip(paths, all_results):
    specs = folder.split("/")[2]
    specs = json.loads(specs)
    varLst.append(specs[0])

    stats = fetch_simulation_stats(sim)
    allSimStats.append(stats)

legendLabels = list(map(lambda x: variable + "=" + str(x), varLst))
for stat in ('Average', 'Max'):
    Ys = []
    Xs = []
    for i in range(len(allSimStats)):
        Ys.append([])
        for j in range(len(allSimStats[i])):
            Ys[i].append(allSimStats[i][j][stat])
        Xs.append(range(len(allSimStats[i])))
    d = {
        
        "Xs": Xs,
        "Ys":Ys,
        "title" : variable + "'s effect on " + stat + " Score",
        "xLabel" : "Generation",
        "yLabel" : stat + " Score",
        "n" : len(allSimStats),
        "legendLabels" : legendLabels
    }
    fig, ax1 = make_plot(d['title'], d['xLabel'], d['yLabel'])
    compiled_results = list(zip(d['Xs'], d['Ys'], d['legendLabels']))
    add_lines(fig, ax1, compiled_results)
    save_plot(fig, stat + variable + datetime.now().strftime("%Y%m%d-%H%M%S"))
