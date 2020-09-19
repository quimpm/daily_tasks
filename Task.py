class Task():
    
    def __init__(self,datetime,title,description):
        self.datetime = datetime
        self.title = title
        self.description = description

    def asdict(self):
        return { 'datetime' : self.datetime, 'title' : self.title, 'description' : self.description }

    class Builder():
        
        def __init__(self):
            self.datetime = None
            self.title = None
            self.description = None

        def addDatetime(self,datetime):
            self.datetime = datetime
            return self

        def addTitle(self,title):
            self.title = title
            return self

        def addDescription(self,description):
            self.description = description
            return self

        def build(self):
            return Task(self.datetime, self.title, self.description)