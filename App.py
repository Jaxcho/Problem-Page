from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()

url = os.environ.get('SUPABASE_URL')
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

#
# @app.route('/table', methods=['POST'])
# def test():
#     return render_template("output.html")



if __name__ == "__main__":
    app.run(debug=True)