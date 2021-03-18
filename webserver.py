# Import Packages
from flask import Flask, render_template, request
import pandas as pd
from snowflakeConnection import sfconnect

# Flask Web Application
app = Flask("my website")


@app.route('/')
def homepage():
    cur.execute("SELECT COLOR_NAME,COUNT(COLOR_NAME) AS COLOR_COUNT FROM COLORS "
                "GROUP BY COLOR_NAME "
                "ORDER BY COLOR_COUNT DESC;")
    rows = pd.DataFrame(cur.fetchall(), columns=['Color Name', 'Votes'])
    dfhtml = rows.to_html(index=False)
    return render_template('index.html', dfhtml=dfhtml)


@app.route('/coolcharts')
def coolcharts():
    cur.execute("SELECT COLOR_NAME, COUNT(COLOR_NAME) AS COLOR_COUNT FROM COLORS "
                "GROUP BY COLOR_NAME "
                "ORDER BY COLOR_COUNT DESC;")
    data4charts = pd.DataFrame(cur.fetchall(), columns=['color','votes'])
    #data4charts_csv = data4charts.to_csv('data4charts.csv', index=False)
    data4charts_json = data4charts.to_json(orient='records')
    return render_template('coolcharts.html', data4charts_json=data4charts_json)

@app.route('/submit')
def submitpage():
    return render_template('submit.html')


@app.route('/thanks4submit', methods=["POST"])
def thanks4submit():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    conn.cursor().execute("INSERT INTO COLORS(COLOR_UID, COLOR_NAME) " +
                          "Select COLOR_UID_SEQ.nextval, '" + colorname + "'")
    return render_template("thanks4submit.html", colorname=colorname, username=username)


# Snowflake Connection
conn = sfconnect()
cur = conn.cursor()

app.run()
