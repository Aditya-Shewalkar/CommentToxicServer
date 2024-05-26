from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


API_URL = "https://api-inference.huggingface.co/models/Hate-speech-CNERG/indic-abusive-allInOne-MuRIL"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
@app.route('/')
def display():
      return "Hello World"

def getString(label):
    if(label*100<=40):
        return 'NAG'
    if(label*100<=80):
        return 'CAG'
    return 'OAG'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    text = data['text']
    
    # Process the text to generate a numerical value.
    # For demonstration, we'll just return the length of the text.
    output = query({
	"inputs": data,
})
    if(output[1]['label']=='LABEL_1'):
        label=output[1]['score']
    else:
         label=output[0]['score']
    print(output)
    return jsonify({'value': getString(label)})

if __name__ == '__main__':
        app.run(debug=True)
