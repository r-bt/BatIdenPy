import requests

class BatCall(object):

    def __init__(self, filepath, date_recorded, location):
        self.filepath = filepath
        self.data_recorded = date_recorded
        self.location = location

    def upload(self):
        files = {"bat_call": open(self.filepath, 'rb')}
        data = {"date_recorded": self.data_recorded, "location": self.location}
        r = requests.post("http://localhost/BatIndentificationProject/upload_audio.php", files=files, data=data)
        return(r.status_code)

tmpCall = BatCall("audio.mp3", "2017-11-12 11:44:22", "40.741895, -73.989308")
print(tmpCall.upload())
