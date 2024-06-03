# Entry point for the backend server using Flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/players', methods=['GET'])
def get_players():
    # This should return a list of players from your database
    players = [{"name": "Player 1", "team": "Team A", "points": 100}]
    return jsonify(players)

@app.route('/api/player/<int:id>', methods=['GET'])
def get_player(id):
    # This should return details of a specific player
    player = {"id": id, "name": "Player 1", "team": "Team A", "points": 100}
    return jsonify(player)

if __name__ == '__main__':
    app.run(debug=True)
