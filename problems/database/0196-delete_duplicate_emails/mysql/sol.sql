--SELECT Email, COUNT(Email) FROM Person GROUP BY Email HAVING COUNT(Email) > 1;

-- | MariaDB [gfg]> SELECT Email, COUNT(Email) FROM Person GROUP
-- | BY Email HAVING COUNT(Email) > 1;
-- | +------------------+--------------+
-- | | Email            | COUNT(Email) |
-- | +------------------+--------------+
-- | | john@example.com |            2 |
-- | +------------------+--------------+
-- | 1 row in set (0.001 sec)
-- | 
-- | MariaDB [gfg]> SELECT Email, COUNT(Email) as nombre FROM Per
-- | son GROUP BY Email HAVING nombre > 1;
-- | +------------------+--------+
-- | | Email            | nombre |
-- | +------------------+--------+
-- | | john@example.com |      2 |
-- | +------------------+--------+
-- | 1 row in set (0.002 sec)

DELETE t1 FROM Person t1
INNER JOIN Person t2
WHERE
  t1.Id > t2.Id AND
  t1.Email = t2.Email;


