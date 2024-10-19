from flask import Flask, request, jsonify
from multiagent import multi_agent_workflow

app = Flask(__name__)


@app.route("/conversation", methods=["POST"])
def handle_conversation():
    data = request.json
    input_text = data.get("input_text")
    response = multi_agent_workflow(input_text, video=False)

    return response


@app.route("/youtube_analysis", methods=["POST"])
def handle_youtube_analysis():
    data = request.json
    search_query = data.get("search_query")
    response = multi_agent_workflow(search_query, video=True)
    return response


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
