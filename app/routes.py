from flask import Blueprint
import os
import markdown
# from .models import AppTableService
import pandas as pd
from model import predict
from config import TRAIN_CONFIGS
bp = Blueprint('bp', __name__)


@bp.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(bp.root_path) + '/README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()

    # Convert to HTML
    return markdown.markdown(content)


@bp.route('/prediction/<my_id>', methods=['GET'])
def get_prediction(my_id):
    print(f"Called get method of Predict.")
    # data = AppTableService.query_by_id(id)
    df = pd.read_csv(TRAIN_CONFIGS["load"]["preprocessed_data"], index_col=0)
    print(df.shape)
    data = df.loc[my_id].values
    print(data)
    prediction = predict(data=data)
    return {"id": my_id, "prediction": prediction}, 200
    # else:
    #     return {"msg": f"no entry with {my_id} could be found."}, 400
