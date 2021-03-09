import numpy as np
import pandas as pd
import joblib
from config import PREPROCESS_CONFIGS


def preprocess():

    LOAD = PREPROCESS_CONFIGS["load"]
    SAVE = PREPROCESS_CONFIGS["save"]

    print("Importing raw data..")
    df = pd.read_csv(LOAD["raw_data"], index_col=0)

    print("Preprocessing data..")
    # Using the insights gained at data analysis step, outlier data are removed.
    df = df.loc[df["DebtRatio"] <= df["DebtRatio"].quantile(0.975)]
    df = df.loc[(df["RevolvingUtilizationOfUnsecuredLines"] < 13)]
    df = df.loc[df["NumberOfTimes90DaysLate"] <= 17]

    impute_dic = None

    # Using results of the data analysis, null values are filled.
    if PREPROCESS_CONFIGS["impute"]:
        print("IMPUTE!")
        dependents_mode = df["NumberOfDependents"].mode()[0] # impute with mode
        df["NumberOfDependents"] = df["NumberOfDependents"].fillna(dependents_mode)

        income_median = df["MonthlyIncome"].median()
        df["MonthlyIncome"] = df["MonthlyIncome"].fillna(income_median)
        impute_dic = {
            "MonthlyIncome": {
                "median": income_median
            },
            "NumberOfDependents": {
                "mode": dependents_mode
            }
        }
    else:
        print("Dropping null values!")
        df.dropna(inplace=True)

    df["EstimatedCreditLine"] = df["DebtRatio"] * df["MonthlyIncome"]
    df["AverageIncomeUntilApp"] = df["MonthlyIncome"].expanding().mean()
    print("Done...\n")

    # Save Essential Items
    print("Saving Essential Items...\n")
    if impute_dic:
        joblib.dump(impute_dic, open(SAVE["imputation"], "wb"))
    df.to_csv(SAVE["preprocessed_data"])
    print("Completed!")


if __name__ == "__main__":
    preprocess()
