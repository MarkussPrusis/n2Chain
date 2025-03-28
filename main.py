import pandas as pd
import flask
from flask import request, send_file, Flask, Response
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

pd.options.display.float_format = "{:.6f}".format
app = flask.Flask(__name__)
df = pd.read_csv("data.csv")
df.set_index("Datums", inplace=True)
show = pd.DataFrame()


rows = []


@app.route("/")
def open():
    return flask.render_template("open.html")

@app.route("/login")
def login():
    return flask.render_template("login.html")

@app.route("/main")
def main():
    return flask.render_template("main.html")

@app.route("/nchain")
def nchain():
    return flask.render_template("nchain.html")

@app.route("/fisch")
def fisch():
    return flask.render_template("fisch.html")

@app.route("/creators")
def creators():
    return flask.render_template("creators.html")

@app.route("/creatorsnologin")
def creatorsnologin():
    return flask.render_template("creatorsnologin.html")

@app.route("/download_csv")
def download_csv():
    global show
    csv_data = io.StringIO()
    show.to_csv(csv_data, index=True)
    csv_data.seek(0)

    return Response(
        csv_data.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=data.csv"}
    )
    #return send_file("data.csv", as_attachment=True, mimetype="text/csv")


@app.route("/data", methods=["GET", "POST"])
def data():
    global df
    global show
    show = pd.DataFrame()
    plt.figure(figsize=(6, 4))
    if request.method == "POST":
        rows.clear()
        use = False
        for i in df.index.to_list():
            if int(i) == int(request.form.get("from")):
                use = True
            if use == True:
                rows.append(i)
            if int(i) == int(request.form.get("to")):
                use = False
        show = df.loc[rows]
        if "1" in request.form.getlist("check") and "2" in request.form.getlist("check"):
            show = show
            if "lin" in request.form.getlist("grafiks"):
                plt.plot(show["$N2 Vērtība (Paredzamā)"], marker='o', linestyle='-', label = "$N2")
                plt.plot(show["Fisch spēlētāju skaits (Paredzamais)"], marker='o', linestyle='-', label = "Fisch")
            elif "his" in request.form.getlist("grafiks"):
                plt.bar(show.index, show["$N2 Vērtība (Paredzamā)"], alpha=0.7, label = "$N2")
                plt.bar(show.index, show["Fisch spēlētāju skaits (Paredzamais)"], alpha=0.7, label = "Fisch")
            plt.legend()
            plt.title("$N2 Vērtība vs Fisch spēlētāju skaits")
        elif "1" in request.form.getlist("check"):
            show = show[["$N2 Vērtība (Paredzamā)"]]
            if "lin" in request.form.getlist("grafiks"):
                plt.plot(show["$N2 Vērtība (Paredzamā)"], marker='o', linestyle='-', label = "$N2")
            elif "his" in request.form.getlist("grafiks"):
                plt.bar(show.index, show["$N2 Vērtība (Paredzamā)"], alpha=0.7, label = "$N2")
            plt.legend()
            plt.title("$N2 Vērtība")
        elif "2" in request.form.getlist("check"):
            show = show[["Fisch spēlētāju skaits (Paredzamais)"]]
            if "lin" in request.form.getlist("grafiks"):
                plt.plot(show["Fisch spēlētāju skaits (Paredzamais)"], marker='o', linestyle='-', label = "Fisch")
            elif "his" in request.form.getlist("grafiks"):
                plt.bar(show.index, show["Fisch spēlētāju skaits (Paredzamais)"], alpha=0.7, label = "Fisch")
            plt.legend()
            plt.title("Fisch spēlētāju skaits")
        else:
            show = pd.DataFrame()

    plt.xlabel("Gads")
    plt.ylabel("")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return flask.render_template("data.html", tables=[show.to_html()], titles=[''], plot_data=image_base64)



app.run(debug=True)