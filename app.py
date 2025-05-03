from flask import Flask, render_template, request, jsonify
from agno_agent.agent import run_agent



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")




@app.route("/send_message", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    try:
        response = run_agent(user_input)
    except Exception as e:
        response = f"Error processing your query: {str(e)}"
    return jsonify({"response": response})






if __name__ == "__main__":
    app.run(debug=True,port=8001)
