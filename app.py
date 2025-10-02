from flask import Flask, request, jsonify
from models import (
    db, ma,
    CommonPlayerInfo, common_player_info_schema, common_players_info_schema,
    DraftCombineStats, draft_combine_schema, draft_combines_schema,
    DraftHistory, draft_history_schema, draft_histories_schema,
    Game, game_schema, games_schema,
    GameInfo, game_info_schema, games_info_schema,
    GameSummary, game_summary_schema, games_summary_schema,
    InactivePlayers, inactive_schema, inactives_schema,
    LineScore, line_schema, lines_schema,
    Officials, official_schema, officials_schema,
    OtherStats, other_schema, others_schema,
    PlayByPlay, play_schema, plays_schema,
    Team, team_schema, teams_schema,
    TeamDetails, team_details_schema, teams_details_schema,
    TeamHistory, team_history_schema, teams_history_schema,
    TeamInfoCommon, team_info_schema, teams_info_schema
)

app = Flask(__name__)

# ✅ Connect to your remote MySQL
import os

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
ma.init_app(app)

# Root
@app.route("/")
def index():
    return jsonify({"message": "NBA API is running and connected to MySQL!"})

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "message": "API is alive"}), 200

# =====================================================
# Endpoints
# =====================================================

# 1. Common Player Info
@app.route("/players", methods=["GET"])
def get_players():
    q = CommonPlayerInfo.query
    country = request.args.get("country")
    if country:
        q = q.filter_by(country=country)
    players = q.limit(50).all()
    return common_players_info_schema.jsonify(players)

@app.route("/player/<int:person_id>", methods=["GET"])
def get_player(person_id):
    player = CommonPlayerInfo.query.get(person_id)
    if player:
        return jsonify(common_player_info_schema.dump(player))
    return jsonify({"error": "Player not found"}), 404


# 2. Draft Combine Stats
@app.route("/draft_combine", methods=["GET"])
def get_draft_combine():
    q = DraftCombineStats.query
    season = request.args.get("season")
    if season:
        q = q.filter_by(season=season)
    rows = q.limit(50).all()
    return draft_combines_schema.jsonify(rows)


# 3. Draft History
@app.route("/draft_history", methods=["GET"])
def get_draft_history():
    q = DraftHistory.query
    season = request.args.get("season")
    if season:
        q = q.filter_by(season=season)
    rows = q.limit(50).all()
    return draft_histories_schema.jsonify(rows)


# 4. Games
@app.route("/games", methods=["GET"])
def get_games():
    q = Game.query
    season = request.args.get("season")
    if season:
        q = q.filter_by(season_id=season)
    rows = q.limit(50).all()
    return games_schema.jsonify(rows)

@app.route("/game/<string:game_id>", methods=["GET"])
def get_game(game_id):
    row = Game.query.get(game_id)
    if row:
        return jsonify(game_schema.dump(row))
    return jsonify({"error": "Game not found"}), 404


# 5. Game Info
@app.route("/gameinfo/<string:game_id>", methods=["GET"])
def get_gameinfo(game_id):
    row = GameInfo.query.get(game_id)
    if row:
        return jsonify(game_info_schema.dump(row))
    return jsonify({"error": "Game Info not found"}), 404


# 6. Game Summary
@app.route("/game_summary", methods=["GET"])
def get_game_summary():
    q = GameSummary.query
    season = request.args.get("season")
    if season:
        q = q.filter_by(season=season)
    rows = q.limit(50).all()
    return games_summary_schema.jsonify(rows)


# 7. Inactive Players
@app.route("/inactive", methods=["GET"])
def get_inactive():
    rows = InactivePlayers.query.limit(50).all()
    return inactives_schema.jsonify(rows)


# 8. Line Score
@app.route("/linescore/<string:game_id>", methods=["GET"])
def get_line_score(game_id):
    row = LineScore.query.get(game_id)
    if row:
        return jsonify(line_schema.dump(row))
    return jsonify({"error": "Line Score not found"}), 404


# 9. Officials
@app.route("/officials/<string:game_id>", methods=["GET"])
def get_officials(game_id):
    rows = Officials.query.filter_by(game_id=game_id).all()
    return officials_schema.jsonify(rows)


# 10. Other Stats
@app.route("/otherstats/<string:game_id>", methods=["GET"])
def get_other_stats(game_id):
    rows = OtherStats.query.filter_by(game_id=game_id).all()
    return others_schema.jsonify(rows)


# 11. Play By Play
@app.route("/playbyplay/<string:game_id>", methods=["GET"])
def get_playbyplay(game_id):
    rows = PlayByPlay.query.filter_by(game_id=game_id).limit(100).all()
    return plays_schema.jsonify(rows)


# 12. Teams
@app.route("/teams", methods=["GET"])
def get_teams():
    rows = Team.query.all()
    return teams_schema.jsonify(rows)


# 13. Team Details
@app.route("/teamdetails/<int:team_id>", methods=["GET"])
def get_team_details(team_id):
    row = TeamDetails.query.get(team_id)
    if row:
        return jsonify(team_details_schema.dump(row))
    return jsonify({"error": "Team Details not found"}), 404


# 14. Team History
@app.route("/team_history", methods=["GET"])
def get_team_history():
    rows = TeamHistory.query.limit(50).all()
    return teams_history_schema.jsonify(rows)


# 15. Team Info Common
@app.route("/team_info/<int:team_id>", methods=["GET"])
def get_team_info(team_id):
    row = TeamInfoCommon.query.get(team_id)
    if row:
        return jsonify(team_info_schema.dump(row))
    return jsonify({"error": "Team Info not found"}), 404


# =====================================================
# Run
# =====================================================
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
