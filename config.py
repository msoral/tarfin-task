from dataclasses import dataclass
from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, "data")
OUTPUT_PATH = Path.joinpath(ROOT_PATH, "model_output")

PREPROCESS_CONFIGS = {
    "load": {
        "raw_data": Path.joinpath(DATA_PATH, "cs-training.csv")
    },
    "save": {
        "preprocessed_data": Path.joinpath(DATA_PATH, "preprocessed.csv"),
        "imputation": Path.joinpath(DATA_PATH, "impute.p")
    },
    "impute": True
}

TRAIN_CONFIGS = {
    "load": {
        "preprocessed_data": PREPROCESS_CONFIGS["save"]["preprocessed_data"],
    },
    "save": {
        "model": Path.joinpath(OUTPUT_PATH, "model.p"),
        "input_test_data": Path.joinpath(DATA_PATH, "x_test.csv"),
        "output_test_data": Path.joinpath(DATA_PATH, "y_test.csv")
    },
    "model_params": {
        "max_depth": 6,
        "random_state": 42,
        "n_estimators": 100
        }
}

PRED_CONFIGS = {
    "load": {
        "input_test_data": Path.joinpath(DATA_PATH, "x_test.csv"),
        "output_test_data": Path.joinpath(DATA_PATH, "y_test.csv"),
        "model": TRAIN_CONFIGS["save"]["model"],
    },
    "save": {
        "predictions": Path.joinpath(OUTPUT_PATH, "predictions.csv")
    },
}


@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 3306
    user: str = "tarfindb"
    password: str = "123123"
    dialect: str = "mysql"
    driver: str = "mysqlconnector"
    db: str = "mysqldb"
