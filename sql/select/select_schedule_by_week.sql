select
	road.team_name,
	road_score ,
	'@' || home.team_name,
	home_score
from
	games,
	teams as road,
	teams as home
where
	road.id = games.road_team
	and home.id = games.home_team
	and games.game_date = '2025-09-07'