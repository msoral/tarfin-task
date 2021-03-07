import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from config import TRAIN_CONFIGS


def train():
    LOAD = TRAIN_CONFIGS["load"]
    SAVE = TRAIN_CONFIGS["save"]
    params = TRAIN_CONFIGS["model_params"]

    df = pd.read_csv(LOAD["preprocessed_data"], index_col=0)

    X = df.iloc[:, 1:]
    Y = df.iloc[:, 0]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
    print("Saving test set for future use...")
    x_test.to_csv(SAVE["input_test_data"])
    y_test.to_csv(SAVE["output_test_data"])
    print("Training model...")
    model = RandomForestClassifier(**params)
    model.fit(x_train.values, y_train.values)
    # Save Model
    print("Saving Model...")
    joblib.dump(model, open(SAVE["model"], "wb"))
    print("Completed!")


if __name__ == "__main__":
    train()
