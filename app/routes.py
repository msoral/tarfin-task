from flask import Blueprint, jsonify, request
import pandas as pd
import os
import markdown
from .models import AppTableService
from model import predict
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


@bp.route('/prediction/', methods=['GET'])
def get_prediction():
    print(f"Called get method of Predict.")
    data = request.get_json(force=True)
    my_id = data["id"]
    query_result = AppTableService.query_by_id(my_id)
    result = query_result.__dict__
    result.pop("id")
    result.pop("_sa_instance_state")
    result.pop("sd2y")
    print(result)
    df = pd.DataFrame(result, index=[0])
    df["EstimatedCreditLine"] = df["debt_ratio"] * df["m_income"]
    df["AverageIncomeUntilApp"] = df["m_income"].expanding().mean()
    print(df.head())

    prediction = predict(data=df.values)
    output = {"id": my_id, "prediction": float(prediction)}
    return jsonify(output), 200

