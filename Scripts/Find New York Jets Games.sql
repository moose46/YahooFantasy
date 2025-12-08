SELECT m.* FROM public.matches AS m
--WHERE awayteam = 'New York Jets' or hometeam = 'New York Jets' and dateutc < TIMESTAMP '2025-11-01 00:00:00+00'
WHERE dateutc <= CURRENT_DATE and (m.awayteam = 'New York Jets' or m.hometeam = 'New York Jets')
order by week

--SELECT *
--FROM events
--WHERE event_time_utc >= TIMESTAMP '2025-01-01 00:00:00+00'
--  AND event_time_utc <  TIMESTAMP '2025-02-01 00:00:00+00';
