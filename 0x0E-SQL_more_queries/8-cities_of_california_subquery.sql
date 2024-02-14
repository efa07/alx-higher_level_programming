-- Lists all cities of CA in the database hbtn_0d_usa.
-- and show in ordered by ascending cities.id.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	        FROM `states`
	       WHERE `name` = "California")
ORDER BY `id`;
