-- public.matches definition

-- Drop table

-- DROP TABLE public.matches;

CREATE TABLE public.matches
(
    id            serial4 NOT NULL,
    week          int4    NOT NULL,
    dateutc       date    NOT NULL,
    "location"    varchar NOT NULL,
    hometeam      varchar NOT NULL,
    awayteam      varchar NOT NULL,
    hometeamscore int4    NOT NULL,
    awayteamscore int4    NULL,
    CONSTRAINT matches_pk PRIMARY KEY (id)
);
