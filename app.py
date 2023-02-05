from flask import Flask, render_template
from PlaylistGenerator import PlaylistGenerator

app=Flask(__name__,template_folder='/home/KPOP project/templates/')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)