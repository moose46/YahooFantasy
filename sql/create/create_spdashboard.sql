-- DROP PROCEDURE public.create_dashboard();

CREATE OR REPLACE PROCEDURE public.create_dashboard()
    LANGUAGE plpgsql
AS
$procedure$
BEGIN
    delete from dashboard;
    insert into dashboard (division, teamname) select division, name from teams;
END;
$procedure$
;
