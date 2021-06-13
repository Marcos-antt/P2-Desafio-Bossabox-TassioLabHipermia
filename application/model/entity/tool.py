class tool:
    def __init__(self, id:int, titulo: str, descricao: str, link: str, tags: list):
        self._id = id
        self._titulo = titulo
        self._link = link
        self._descricao = descricao
        self._tags = tags
    

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self.descricao = value

    @property
    def link(self):
        return self._link
    
    @link.setter
    def link(self, value):
        self._link = value
    
    @property
    def tags(self):
        return self._tags
    
    @tags.setter
    def tags(self, value):
        self._tags = value
    
