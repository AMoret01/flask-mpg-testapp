import os
from flask import Flask,jsonify,request
import pickle


app=Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return """
    <h1> App para calcular MPG</h1>
    App para testear flask y Railway
    """

@app.route("/api/v1/predictions", methods=["GET"])
def predictions():
    cylinders=request.args["cylinders"]
    displacement=request.args["displacement"]
    horsepower=request.args["horsepower"]
    acceleration=request.args["acceleration"]
    weight=request.args["weight"]
    model_year=request.args["model_year"]

    map_origin={'usa': 1, 'japan': 2, 'europe': 3}
    origin=request.args["origin"]
    origin=map_origin[origin]

    filename="model.save"
    loaded_model= pickle.load(open(filename,"rb"))
    
    # El orden de los datos tiene que ser el mismo que en el modelo
    new_data=[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]
    resultado={"mpg":loaded_model.predict([new_data])[0]}
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
