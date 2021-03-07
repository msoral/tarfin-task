import model
from app import db, init_app, models
import pandas as pd

if __name__ == "__main__":
    model.preprocess()
    model.train()
    model.predict()

    app = init_app()
    with app.app_context():
        db.create_all()
        df = pd.read_csv("data/preprocessed.csv", index_col=0)
        data = df.to_dict('records')
        for item in data:
            models.AppTableService.insert_data(item)
