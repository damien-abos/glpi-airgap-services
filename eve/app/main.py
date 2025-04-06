from eve import Eve
from flask import request

app = Eve()

@app.get('/api/registration/info')
def registration_info():
    if request.method == 'GET':
        return 'OK'
    else:
        return 'KO'

if __name__ == '__main__':
    app.run()