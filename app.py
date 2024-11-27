from flask import Flask, request, jsonify,render_template
from model import calculate_financial_score

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/score', methods=['POST'])
def score():
    """
    API endpoint to calculate financial score.
    Input: JSON data with income, savings, and expenditures.
    Output: Financial score and insights.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. Please provide JSON data."}), 400
        
        financial_score, insights = calculate_financial_score(data)
        response = {
            "financial_score": financial_score,
            "insights": insights
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

