from application.model.entity.tool import tool
from flask import Flask, render_template, request, url_for
from application import app
from application.model.entity.tool import tool


tool_list = [

    tool(1, "Apenas um Teste Rapaziada", "Teste Testado com muito orgulho" , "https://www.youtube.com/watch?v=JlND89hciZw", ["testeA", "testeB"] )


]

@app.route("/", methods=['GET'])
def index():
  return render_template("index.html", tool_list=tool_list)

