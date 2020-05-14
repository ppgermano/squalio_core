# https://stackoverflow.com/questions/20015550/read-file-data-without-saving-it-in-flask
# https://www.programcreek.com/python/example/107718/speech_recognition.AudioFile
# https://stackoverflow.com/questions/52998871/unable-to-resolve-missing-google-api-python-client-module-using-speech-recogniti

import os

from dynaconf import settings
from flask_api import FlaskAPI
import speech_recognition as sr
from flask import request, flash, redirect, render_template

ALLOWED_EXTENSIONS = {'wav'}

app = FlaskAPI(__name__)

app.secret_key = os.urandom(24)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings('PATH_AUTH_GOOGLE')

r = sr.Recognizer()

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/speech-to-text', methods=['GET', 'POST'], strict_slashes=False)
def upload_file():

	default_options = {
		'show_all': 'True',
		'api_type': 'google_web'
	}

	if request.method == 'POST':

		# check if the post request has the file part
		if 'audio_file' not in request.files:
			print('No file part')
			return redirect(request.url)

		file = request.files['audio_file']

		print(request.data)

		# if user does not select file, browser also
		# submit an empty part without filename

		if file.filename == '':
			print('No selected file')
			return redirect(request.url)

		# parse data from post request and changes default values
		for key, value in default_options.items():
			if key in request.data:
				default_options[key] = request.data[key]

		if file and allowed_file(file.filename):

			file = sr.AudioFile(file)
			with file as source:
				audio = r.record(source)

			# recognize_google is default recognition system
			try:
				if default_options['api_type'] == 'google_web':
					resp = r.recognize_google(audio)
				elif default_options['api_type'] == 'google_cloud':
					show_all = eval(default_options['show_all'].capitalize())
					resp = r.recognize_google_cloud(audio, show_all=show_all)
			except sr.UnknownValueError:
				return {'status': 'fail', 'message': 'speech is unintelligible'}, 500
			except sr.RequestError:
				return {'status': 'fail','message': 'speech recognition operation failed'}, 500

			return {"status": "success","data": resp}

	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
