import os
from flask import Flask, request, render_template

music_dir='/home/mohit/Desktop/flaskmedia/static/music' #replace it with proper address of your machine

app= Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	music_files=[f for f in os.listdir(music_dir) if f.endswith('mp3')]
	music_files_number = len(music_files)
	return render_template("index.html",title='Home',music_files_number=music_files_number,
		music_files=music_files)

@app.route('/<filename>')
def song(filename):
	return render_template('play.html',title=filename,music_file=filename)


if __name__== '__main__':
	app.run(host='0.0.0.0', debug=True)
	#in browser localhost:5000

