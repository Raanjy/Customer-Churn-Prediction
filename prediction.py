from flask import Flask, render_template, request
import pickle
# Creating the Flask app
app = Flask(__name__,template_folder='Templates')
model = pickle.load(open("Finalised_model.pickle", "rb"))


@app.route("/", methods=["GET"])
def home():
    return render_template("Customer Churn Prediction.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        CreditScore = float(request.form["CreditScore"])
        Gender = float(request.form["Gender"])
        Age = float(request.form["Age"])
        Geography = float(request.form["Geography"])
        Balance = float(request.form["Balance"])
        NumOfProducts = float(request.form["NumOfProducts"])
        IsActiveMember = float(request.form["IsActiveMember"])
        Tenure = float(request.form["Tenure"])
        HasCrCard = float(request.form["HasCrCard"])
        EstimatedSalary = float(request.form["EstimatedSalary"])

        prediction = model.predict([[CreditScore, Gender, Age, Geography, Balance, IsActiveMember, Tenure, HasCrCard, NumOfProducts, EstimatedSalary]])
        if prediction == 1:
            return render_template("Result.html", predicted_texts="Customer Exited")
        else:
            return render_template("Result.html", predicted_texts="Customer Not Exited")
    else:
        return render_template("Customer Churn Prediction.html")

if __name__ == "__main__":
    app.run(debug=True)
