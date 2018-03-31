import requests, datetime, re

class BatCall(object):

    def __init__(self, filepath, date_recorded, location):
        self.filepath = filepath
        self.date_recorded = date_recorded
        self.location = location

    def validate(self):
        try:
            datetime.datetime.strptime(self.date_recorded, "%Y-%m-%d %H:%M:%S")
        except:
            return 0
        if(re.match("^-?([1-8]\d\.\d+|90), -?([0-1]?[0-7]\d\.\d+|180)$", self.location) == None):
            return 2
        return 1

    def upload(self):
        files = {"bat_call": open(self.filepath, 'rb')}
        data = {"date_recorded": self.date_recorded, "location": self.location}
        r = requests.post("http://localhost/BatIndentificationProject/BatIdentificationServer/upload_audio.php", files=files, data=data)
        return(r.status_code)
