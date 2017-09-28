import requests
from flask import Flask, request, jsonify, abort
import os


app = Flask(__name__)
webhook = "insert webhook here"


#function retrieves slack responses and returns a dict with slack response properties. Remove arguments according to what your program needs.
def getSlackResponse(response):
	token = request.form.get('token', None)
	team_id = request.form.get('team_id', None)
	team_domain = request.form.get('team_domain', None)
	channel_id = request.form.get('channel_id', None)
	channel_name = request.form.get('channel_name', None)
	user_id = request.form.get('user_id', None)
	user_name = request.form.get('user_name', None)
	command = request.form.get('command', None)
	text = request.form.get('text', None)
	response_url = request.form.get('text', None)
	return {'token':token, 'team_id': team_id, 'team_domain':team_domain, 'channel_id':channel_id, 'channel_name':channel_name, 'user_id':user_id, 'user_name':user_name, 'command':command, 'text':text}



#build application endpoints, root endpoint preferebly used as an application webpage. replace '/' with endpoints.
@app.route('/')
def root():
	#add Homepage
    return 'Home'


#each endpoint can have multiple arguments, but endpoints preferebly should match the slashcommand.
@app.route('/endpoint1', methods=['POST'])
def endpoint():
	if request.method == 'POST':
		data = getSlackResponse(request.get_data())
		text = data['text']

		#add program logic here where "text" is the slash command argument
		if text == 'argument'
			post_data = requests.post(webhook, json={'text': text_to_send})
		return 

#different slash command with different endpoint.
@app.route('/endpoint2', methods=['POST'])
def endpoint():
	if request.method == 'POST':
		data = getSlackResponse(request.get_data())
		text = data['text']

		#add program logic here where "text" is the slash command argument
		if text == 'argument'
			post_data = requests.post(webhook, json={'text': text_to_send})
		return 


#code to run Flask program.
if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)