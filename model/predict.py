import pandas as pd
import numpy as np
import joblib
from config import PRED_CONFIGS


def predict(data=None):
    LOAD = PRED_CONFIGS["load"]
    SAVE = PRED_CONFIGS["save"]

    # Import Model
    print("Importing Model...")
    model = joblib.load(open(LOAD["model"], "rb"))
    print("Done...\n")

    if data is None:
        x_test = pd.read_csv(LOAD["input_test_data"], index_col=0)
        y_test = pd.read_csv(LOAD["output_test_data"], index_col=0)

        # Generate Predictions
        print("Generating Predictions...")
        # This returns both probability for both True and False, we only take one.
        predict_prob = model.predict_proba(x_test.values)[:, 1]
        print("Done...\n")

        # Save Predictions
        print("Saving Predictions...")
        result = pd.DataFrame({"Id": x_test.index, "Probability": predict_prob})
        print(result.head(10))
        result["Id"] = result["Id"].astype(int)
        result["Probability"] = result["Probability"].astype(float)
        result.to_csv(SAVE["predictions"], index=False)
        print("Completed!")
    else:
        print("returning prediction for a single value")
        return model.predict_proba(data)[:, 1]


if __name__ == "__main__":
    predict()

