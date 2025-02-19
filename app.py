from re import DEBUG
from flask import Flask, render_template, request
import google.generativeai as genai
import time



genai.configure(api_key="")

app=Flask(__name__)


class Data:
    traceback = []  # Stores text

    @staticmethod
    def add_text(text):
        Data.traceback.append(text)

    @staticmethod
    def storage():
        return Data.traceback
    

    
@app.route('/', methods=["POST", "GET"])


      

def home():
    
    if request.method=="GET":
      return render_template("home.jinja2")
    elif request.method=="POST":
        text = request.form.get("user_input")
        
        
        if not text:
            return render_template("response.jinja2", response="Please enter a message.")

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f'prompt:chatbot,previous prompts for reference:{Data().storage()},new prompt:{text}')
            Data.add_text(text)
            return render_template("response.jinja2", response=response.text)
        except Exception as e:
            return render_template("error.jinja2", error_message=str(e))
    else:
       return render_template('error.html')

if __name__ == '__main__':
  app.run()
 
  
