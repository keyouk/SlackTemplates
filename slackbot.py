from flask import Flask, request, abort, make_response
import json

app = Flask(__name__)



#Post the url verification to your application/challenge
@app.route("/challenge", methods=["GET", "POST"])
def challenge():
    if request.method == 'POST':
        response = request.data	
        return response['challenge']


@app.route("/challenge", methods=["GET", "POST"])


if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)



