DROP DATABASE IF EXISTS anime;
CREATE DATABASE anime;
\c anime;

--
----Structure for anime ratings table
--

DROP TABLE IF EXISTS animeRatings;
CREATE TABLE animeRatings(
    name varchar(100) NOT NULL,
    genre1 varchar(35) default '' NOT NULL,
    genre2 varchar (35) default '' NOT NULL,
    genre3 varchar(35) default '' NOT NULL,
    rating int NOT NULL,
    enjoy int NOT NULL
);