from application.model.entity.tool import Tool


tool_list = [
    Tool(1,"Netflix", "https://www.netflix.com/browse","Netflix é uma provedora global de filmes", ["a", "b"]),
    Tool(2,"Youtube", "https://www.youtube.com","YouTube é uma plataforma de compartilhamento de vídeos com sede em San Bruno", ["b", "c"]),

]



class ToolDAO():
    def __init__(self, tool_list = tool_list):
        self.tool_list = tool_list



    def listar_tool(self):
        return self.tool_list
    
    