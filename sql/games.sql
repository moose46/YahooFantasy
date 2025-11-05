-- public.games definition

-- Drop table

-- DROP TABLE public.games;

CREATE TABLE public.games (
	id int4 DEFAULT nextval('game_id_seq'::regclass) NOT NULL,
	week_num int4 NOT NULL,
	home_team int4 NOT NULL,
	road_team int4 NOT NULL,
	game_date date DEFAULT CURRENT_DATE NOT NULL,
	road_score int4 DEFAULT 0 NOT NULL,
	home_score int4 DEFAULT 0 NOT NULL,
	CONSTRAINT games_pk PRIMARY KEY (id)
);


-- public.games foreign keys

ALTER TABLE public.games ADD CONSTRAINT game_teams_fk FOREIGN KEY (home_team) REFERENCES public.teams(id);
ALTER TABLE public.games ADD CONSTRAINT game_teams_fk_1 FOREIGN KEY (road_team) REFERENCES public.teams(id);