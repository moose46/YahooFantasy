-- public.dashboard definition

-- Drop table

-- DROP TABLE public.dashboard;

CREATE TABLE public.dashboard
(
    id       int8 GENERATED ALWAYS AS IDENTITY ( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE) NOT NULL,
    division varchar(32)                                                                                                          NOT NULL, -- nfl division AFC North, NFC West ...
    teamname varchar(64)                                                                                                          NOT NULL,
    wins     int4   DEFAULT 0                                                                                                     NOT NULL,
    loses    int4   DEFAULT 0                                                                                                     NOT NULL,
    "ties"   int4   DEFAULT 0                                                                                                     NOT NULL,
    pct      float4 DEFAULT 0                                                                                                     NOT NULL, -- name["wins"] / (name["wins"] + name["losses"]
    CONSTRAINT dashboard_pk PRIMARY KEY (id),
    CONSTRAINT dashboard_unique UNIQUE (teamname)
);

-- Column comments

COMMENT ON COLUMN public.dashboard.division IS 'nfl division AFC North, NFC West ...';
COMMENT ON COLUMN public.dashboard.pct IS 'name["wins"] / (name["wins"] + name["losses"]';