from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# =====================================================
# 1. Common Player Info
# =====================================================
class CommonPlayerInfo(db.Model):
    __tablename__ = "common_player_info"
    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    display_first_last = db.Column(db.String(100))
    display_last_comma_first = db.Column(db.String(100))
    display_fi_last = db.Column(db.String(100))
    player_slug = db.Column(db.String(100))
    birthdate = db.Column(db.String(50))
    school = db.Column(db.String(100))
    country = db.Column(db.String(100))
    last_affiliation = db.Column(db.String(100))
    height = db.Column(db.String(20))
    weight = db.Column(db.String(20))
    season_exp = db.Column(db.Integer)
    jersey = db.Column(db.String(10))
    position = db.Column(db.String(20))
    rosterstatus = db.Column(db.String(20))
    team_id = db.Column(db.Integer)
    team_name = db.Column(db.String(100))
    team_abbreviation = db.Column(db.String(10))
    team_code = db.Column(db.String(20))
    team_city = db.Column(db.String(50))
    playercode = db.Column(db.String(50))
    from_year = db.Column(db.Integer)
    to_year = db.Column(db.Integer)
    draft_year = db.Column(db.String(10))
    draft_round = db.Column(db.String(10))
    draft_number = db.Column(db.String(10))


class CommonPlayerInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommonPlayerInfo
        load_instance = True


common_player_info_schema = CommonPlayerInfoSchema()
common_players_info_schema = CommonPlayerInfoSchema(many=True)

# =====================================================
# 2. Draft Combine Stats
# =====================================================
class DraftCombineStats(db.Model):
    __tablename__ = "draft_combine_stats"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # if you have an auto id
    season = db.Column(db.String(255))
    player_id = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    player_name = db.Column(db.String(255))
    position = db.Column(db.String(255))

    height_wo_shoes = db.Column(db.Float)
    height_wo_shoes_ft_in = db.Column(db.String(255))
    height_w_shoes = db.Column(db.Float)
    height_w_shoes_ft_in = db.Column(db.String(255))

    weight = db.Column(db.String(255))
    wingspan = db.Column(db.Float)
    wingspan_ft_in = db.Column(db.String(255))

    standing_reach = db.Column(db.Float)
    standing_reach_ft_in = db.Column(db.String(255))
    body_fat_pct = db.Column(db.String(255))



class DraftCombineStatsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DraftCombineStats
        load_instance = True


draft_combine_schema = DraftCombineStatsSchema()
draft_combines_schema = DraftCombineStatsSchema(many=True)

# =====================================================
# 3. Draft History
# =====================================================
class DraftHistory(db.Model):
    __tablename__ = "draft_history"
    person_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(100))
    season = db.Column(db.String(20))
    round_number = db.Column(db.String(10))
    round_pick = db.Column(db.String(10))
    overall_pick = db.Column(db.String(10))
    draft_type = db.Column(db.String(50))
    team_id = db.Column(db.Integer)
    team_city = db.Column(db.String(50))
    team_name = db.Column(db.String(50))
    team_abbreviation = db.Column(db.String(10))


class DraftHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DraftHistory
        load_instance = True


draft_history_schema = DraftHistorySchema()
draft_histories_schema = DraftHistorySchema(many=True)

# =====================================================
# 4. Game
# =====================================================
class Game(db.Model):
    __tablename__ = "game"
    game_id = db.Column(db.String(20), primary_key=True)
    season_id = db.Column(db.String(20))
    team_id_home = db.Column(db.Integer)
    team_name_home = db.Column(db.String(100))
    team_abbreviation_home = db.Column(db.String(10))
    pts_home = db.Column(db.Integer)
    team_id_away = db.Column(db.Integer)
    team_name_away = db.Column(db.String(100))
    team_abbreviation_away = db.Column(db.String(10))
    pts_away = db.Column(db.Integer)
    game_date = db.Column(db.String(20))
    season_type = db.Column(db.String(20))


class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        load_instance = True


game_schema = GameSchema()
games_schema = GameSchema(many=True)

# =====================================================
# 5. Game Info
# =====================================================
class GameInfo(db.Model):
    __tablename__ = "game_info"
    game_id = db.Column(db.String(20), primary_key=True)
    game_date = db.Column(db.String(20))
    attendance = db.Column(db.Integer)
    game_time = db.Column(db.String(20))


class GameInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GameInfo
        load_instance = True


game_info_schema = GameInfoSchema()
games_info_schema = GameInfoSchema(many=True)

# =====================================================
# 6. Game Summary
# =====================================================
class GameSummary(db.Model):
    __tablename__ = "game_summary"
    game_id = db.Column(db.String(20), primary_key=True)
    game_date_est = db.Column(db.String(20))
    home_team_id = db.Column(db.Integer)
    visitor_team_id = db.Column(db.Integer)
    season = db.Column(db.String(20))


class GameSummarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GameSummary
        load_instance = True


game_summary_schema = GameSummarySchema()
games_summary_schema = GameSummarySchema(many=True)

# =====================================================
# 7. Inactive Players
# =====================================================
class InactivePlayers(db.Model):
    __tablename__ = "inactive_players"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.String(20))
    player_id = db.Column(db.Integer)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    team_id = db.Column(db.Integer)
    team_name = db.Column(db.String(50))


class InactivePlayersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InactivePlayers
        load_instance = True


inactive_schema = InactivePlayersSchema()
inactives_schema = InactivePlayersSchema(many=True)

# =====================================================
# 8. Line Score
# =====================================================
class LineScore(db.Model):
    __tablename__ = "line_score"
    game_id = db.Column(db.String(20), primary_key=True)
    team_id_home = db.Column(db.Integer)
    pts_home = db.Column(db.Integer)
    team_id_away = db.Column(db.Integer)
    pts_away = db.Column(db.Integer)


class LineScoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LineScore
        load_instance = True


line_schema = LineScoreSchema()
lines_schema = LineScoreSchema(many=True)

# =====================================================
# 9. Officials
# =====================================================
class Officials(db.Model):
    __tablename__ = "officials"
    official_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    jersey_num = db.Column(db.String(10))
    game_id = db.Column(db.String(20))


class OfficialsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Officials
        load_instance = True


official_schema = OfficialsSchema()
officials_schema = OfficialsSchema(many=True)

# =====================================================
# 10. Other Stats
# =====================================================
class OtherStats(db.Model):
    __tablename__ = "other_stats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.String(20))
    team_id_home = db.Column(db.Integer)
    pts_paint_home = db.Column(db.Integer)
    team_id_away = db.Column(db.Integer)
    pts_paint_away = db.Column(db.Integer)


class OtherStatsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OtherStats
        load_instance = True


other_schema = OtherStatsSchema()
others_schema = OtherStatsSchema(many=True)

# =====================================================
# 11. Play By Play
# =====================================================
class PlayByPlay(db.Model):
    __tablename__ = "play_by_play"
    game_id = db.Column(db.String(20), primary_key=True)
    eventnum = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.Integer)
    pctimestring = db.Column(db.String(20))
    homedescription = db.Column(db.String(200))
    visitordescription = db.Column(db.String(200))
    score = db.Column(db.String(20))


class PlayByPlaySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlayByPlay
        load_instance = True


play_schema = PlayByPlaySchema()
plays_schema = PlayByPlaySchema(many=True)

# =====================================================
# 12. Teams
# =====================================================
class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    abbreviation = db.Column(db.String(10))
    nickname = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    year_founded = db.Column(db.Integer)


class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        load_instance = True


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)

# =====================================================
# 13. Team Details
# =====================================================
class TeamDetails(db.Model):
    __tablename__ = "team_details"
    team_id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(10))
    nickname = db.Column(db.String(50))
    yearfounded = db.Column(db.Integer)
    city = db.Column(db.String(50))
    arena = db.Column(db.String(100))
    headcoach = db.Column(db.String(100))


class TeamDetailsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TeamDetails
        load_instance = True


team_details_schema = TeamDetailsSchema()
teams_details_schema = TeamDetailsSchema(many=True)

# =====================================================
# 14. Team History
# =====================================================
class TeamHistory(db.Model):
    __tablename__ = "team_history"
    team_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    year_founded = db.Column(db.Integer)
    year_active_till = db.Column(db.Integer)


class TeamHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TeamHistory
        load_instance = True


team_history_schema = TeamHistorySchema()
teams_history_schema = TeamHistorySchema(many=True)

# =====================================================
# 15. Team Info Common
# =====================================================
class TeamInfoCommon(db.Model):
    __tablename__ = "team_info_common"
    team_id = db.Column(db.Integer, primary_key=True)
    season_year = db.Column(db.String(20))
    team_city = db.Column(db.String(50))
    team_name = db.Column(db.String(50))
    team_abbreviation = db.Column(db.String(10))
    w = db.Column(db.Integer)
    l = db.Column(db.Integer)


class TeamInfoCommonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TeamInfoCommon
        load_instance = True


team_info_schema = TeamInfoCommonSchema()
teams_info_schema = TeamInfoCommonSchema(many=True)
