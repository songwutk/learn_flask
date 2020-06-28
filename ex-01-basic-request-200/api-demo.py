import os
from flask import Flask, request,jsonify
app = Flask(__name__)
 
@app.route("/demo", methods=['GET','POST'])
def demo():
    
    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)
    books = [
        {'id': 0,
        'title': 'Deep',
        'author': 'Vinge',
        'first_sentence': 'The dreamless.',
        'year_published': '1997'},
        {'id': 1,
        'title': 'Walk Away',
        'author': 'Guin',
        'first_sentence': 'With swallows soaring. ',
        'published': '1943'},
        {'id': 2,
        'title': 'Dgren',
        'author': 'Delany',
        'first_sentence': 'the autumnal city.',
        'published': '1935'}
    ]
 

    return jsonify(books)

@app.route("/", methods=['GET','POST'])
def index():
    
    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    return 'ok',200    

@app.route('/favicon.ico')
def favicon():
    # return redirect(url_for('static', filename='favicon.ico'))
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8086,debug=True)