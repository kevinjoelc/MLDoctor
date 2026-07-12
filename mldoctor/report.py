import json

class Report:

    def __init__(self,data):

        self.data=data

    def save_json(self,file):

        with open(file,"w") as f:

            json.dump(self.data,f,indent=4)

    def __str__(self):

        return json.dumps(self.data,indent=4)