from flask import Flask, render_template
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/income")
def income():
    engine = create_engine(f"sqlite:///resources/sqlite/income.sqlite")
    data = engine.execute("SELECT * FROM income")
    key = []
    value = []
    for row in data:
        key.append(row['county'])
        value.append(row['median_income'])
    data = engine.execute("SELECT * FROM income")
    column2 = 'Median Income'
    return render_template("income.html", data=data, column2=column2, key=key, value=value)


@app.route("/employment")
def employment():
    engine = create_engine(f"sqlite:///resources/sqlite/unemployment.sqlite")
    data = engine.execute("SELECT * FROM unemployment")
    key = []
    employment = []
    unemployment = []
    rate = []
    for row in data:
        key.append(row['county'])
        employment.append(row['employment'])
        unemployment.append(row['unemployment'])
        rate.append(row['rate'])
    data = engine.execute("SELECT * FROM unemployment")
    return render_template("employment.html", data=data, key=key, employment=employment,
                           unemployment=unemployment, rate=rate)


@app.route("/population")
def population():
    engine = create_engine(f"sqlite:///resources/sqlite/population.sqlite")
    data = engine.execute("SELECT * FROM population")
    key = []
    value = []
    for row in data:
        key.append(row['county'])
        value.append(row['total_population'])
    data = engine.execute("SELECT * FROM population")
    column2 = 'Total Population'
    return render_template("income.html", data=data, column2=column2, key=key, value=value)


@app.route("/analysis")
def analysis():
    engine = create_engine(f"sqlite:///resources/sqlite/income.sqlite")
    data = engine.execute("SELECT * FROM income")
    county = []
    income = []
    for row in data:
        county.append(row['county'])
        income.append(row['median_income'])
    engine = create_engine(f"sqlite:///resources/sqlite/unemployment.sqlite")
    rate = []
    data = engine.execute("SELECT rate FROM unemployment")
    for row in data:
        rate.append(row[0])
    engine = create_engine(f"sqlite:///resources/sqlite/population.sqlite")
    population = []
    data = engine.execute("SELECT total_population FROM population")
    for row in data:
        population.append(row[0])

    return render_template("analysis.html", county=county, income=income, rate=rate, population=population)


if __name__ == "__main__":
    app.run(debug=True)
