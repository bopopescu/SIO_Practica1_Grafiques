class RelRestMitj:
    def __init__(self, id, mitjana):
        self.id = id
        self.mitjana = mitjana

    def __str__(self):
        return str(self.id)+","+str(self.mitjana)