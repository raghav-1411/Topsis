import pandas as pd
import numpy as np

def run_topsis(df, weights, impacts):
    if df.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:]
    criteria_count = data.shape[1]

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != criteria_count:
        raise Exception("Number of weights must match number of criteria")

    if len(impacts) != criteria_count:
        raise Exception("Number of impacts must match number of criteria")

    for i in impacts:
        if i not in ['+', '-']:
            raise Exception("Impacts must be + or -")

    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(criteria_count):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = score.rank(ascending=False).astype(int)

    return df
