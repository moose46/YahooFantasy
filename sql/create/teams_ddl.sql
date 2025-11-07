-- public.teams definition

-- Drop table

-- DROP TABLE public.teams;

CREATE TABLE public.teams (
	id serial4 NOT NULL,
	team_name varchar NOT NULL,
	division varchar NOT NULL,
	wins int4 DEFAULT 0 NOT NULL,
	losses int4 DEFAULT 0 NOT NULL,
	"ties" int4 DEFAULT 0 NOT NULL,
	pct float4 NULL,
	www varchar NULL,
	CONSTRAINT teams_pkey PRIMARY KEY (id)
);