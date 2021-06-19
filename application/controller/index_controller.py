from application import app
from flask import render_template, request, url_for, redirect
from application.model.dao.tooldao import  ToolDAO
from application.model.entity.tool import Tool

toolDAO = ToolDAO()
tool_list = toolDAO.listar_tool()


@app.route("/", methods=['GET'])
def index():
    return render_template ("index.html", tool_list = tool_list)

#id:int, titulo: str, descricao: str, link: str, tags: list
@app.route("/adicionar", methods=['POST'])
def adicionar():
    id = len(tool_list) + 1
    titulo = request.form.get("form_titulo", None)
    descricao = request.form.get("form_descricao", None)
    link = request.form.get("form_link", None)
    tags = request.form.get("form_tags", None).split(" ")
    tool = Tool(id , titulo , link, descricao, tags)
    tool_list.append(tool)
    return render_template ("index.html", tool_list = tool_list)

@app.route("/excluir/<int:id>", methods=["GET"])
def excluir(id: int):
    for i in tool_list:
        if i.id == id:
            tool_list.remove(i)
            return render_template("index.html", tool_list = tool_list)
    return render_template("index.html",tool_list = tool_list)


@app.route("/buscar", methods=["GET"])
def buscar():
    tool_busca_list = []
    buscar = request.args.get("search")
    buscar_tag = request.args.get("only_tag")
    for tool in tool_list:
        if buscar_tag == "only_tag":
            if buscar in tool.tags:
                tool_busca_list.append(tool)
        elif buscar_tag == None:
            if buscar in tool.titulo or buscar in tool.descricao:
                tool_busca_list.append(tool)

    return render_template("index.html",tool_list = tool_busca_list)



