select
    score,
    DENSE_RANK() OVER ( ORDER BY score DESC ) `rank`
from Scores;
