from flask import Flask, request
from flask import jsonify
from gogoanime_io import search, newanime
import json  
       


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
        return jsonify({
            'author': 'Yash Aggarwal',
            'email': 'yaggarwal@deloitte.com'
        })

@app.route('/search_animie', methods = ['GET'])
def search_animie():
    try:
        if 'word' in request.args:
            search_animie_word= request.args.get('word')
            if len(search_animie_word) <=2:
                return json.dumps({'Searched': word, 'Exception': '"Word Entered lenght should be greater then 2"'}, indent = 4)
            return json.dumps(search(search_animie_word), indent = 4) 
        else:
            return 'Pass something is url \"search_animie?word=charset\"'
    except e:
        return json.dumps({'Exception': str(e)}, indent = 4)

@app.route('/new_animie', methods = ['GET'])
def new_animie():
    return json.dumps(newanime(), indent = 4) 
    
if __name__ == '__main__':
    app.run(debug=True)



@app.route('/bcorps', methods = ['GET'])
def bcorps():
    if 'country' in request.args:            
        country = request.args.get('country')
        if len(country)==2:
            country_name = pycountry.countries.get(alpha_2=country)
            return filtered_data(country_name.name) if country_name is not None else 'Enter correct Country code/Country name'
        return filtered_data(country)
    else:
        return json_data()
    return country

if __name__ == '__main__':
    app.run(debug=False)
