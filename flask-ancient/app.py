from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pythainlp.tokenize import syllable_tokenize

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Example endpoint to receive text updates
@app.route('/api/update-text', methods=['POST'])
def update_text():
    after_text = ""
    text = request.json['text']
    for i in syllable_tokenize(text):
        after_text += thai_text_to_suea(i,1)
    return jsonify({'text': after_text})
def thai_text_to_suea(text,u=0):
  if 'ั' in text:
    vowel_index = text.index('ั')
    if text[vowel_index + 1] in ['่','้','๊','๋']:
      text = text[:vowel_index]+text[vowel_index+1]+text[vowel_index]+text[vowel_index+2:]
      text = text.replace('ั',text[vowel_index+2])
    else:
      text = text.replace('ั',text[vowel_index+1])

  elif 'ึ' in text:
    vowel_index = text.index('ึ')
    if u==0:
      text = " ี"+text[:vowel_index]+text[vowel_index+1:]
    else:
      text = " ื"+text[:vowel_index]+text[vowel_index+1:]

  elif 'ื' in text and 'เ' not in text:
    vowel_index = text.index('ื')
    if text[-1] == 'อ':
      text = " ื"+text[:vowel_index]+text[vowel_index+1:-1]
    else:
      text = " ื"+text[:vowel_index]+text[vowel_index+1:]

  elif text[-1] == 'อ' and 'เ' not in text and len(text) != 1:
    text = text[:-1]

  elif 'เ' in text and 'ี' in text:
    vowel_index = text.index('ี')
    if text[-1] == 'ย':
      text = ' ี'+text[1:vowel_index]+text[vowel_index+1:]+'ย'
    else:
      text = ' ี'+text[1:vowel_index]+text[vowel_index+1:]

  elif 'เ' in text and 'ื' in text:
    vowel_index = text.index('ื')
    if text[-1] == 'อ':
      text = ' ืเ'+text[1:vowel_index]+text[vowel_index+1:]+'อ'
    else:
      text = " ืเ"+text[1:vowel_index]+text[vowel_index+1:]

  elif 'ิ' in text:
    vowel_index = text.index('ิ')
    text = " ิ"+text[:vowel_index]+text[vowel_index+1:]

  elif 'ี' in text:
    vowel_index = text.index('ี')
    text = " ี"+text[:vowel_index]+text[vowel_index+1:]

  elif 'ุ' in text:
    vowel_index = text.index('ุ')
    text = " ุ"+text[:vowel_index]+text[vowel_index+1:]

  elif 'ู' in text:
    vowel_index = text.index('ู')
    text = " ู"+text[:vowel_index]+text[vowel_index+1:]

  elif 'ำ' in text:
    vowel_index = text.index('ำ')
    text = text[:vowel_index]+"ํ"

  return text

if __name__ == '__main__':
    app.run(debug=True)