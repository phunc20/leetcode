select today.id from Weather today
inner join Weather veille
on DATE_SUB(today.RecordDate, INTERVAL 1 DAY) = veille.RecordDate
where today.Temperature > veille.Temperature;
