from __main__ import app

@app.route('/admin/', methods=['GET'])
def AdminIndex():
    return "yooooo"