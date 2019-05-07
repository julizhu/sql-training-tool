create table actor(
 actor_id int primary key,
 first_name varchar(50),
 last_name varchar(50),
 last_update timestamp
);

create table rental(
 rental_id int primary key,
 rental_date timestamp,
 inventory_id int,
 customer_id int,
 return_date timestamp,
 staff_id int,
 last_update timestamp
);

create table film_actor(
 actor_id int,
 film_id int,
 last_update timestamp
);

create table language(
 language_id int,
 name varchar(50),
 last_update timestamp
);

create table film(
 film_id int primary key,
 title varchar(150),
 description varchar(300),
 release_year int,
 language_id int,
 rental_duration int,
 rental_rate double precision,
 length int,
 replacement_cost double precision,
 rating varchar(50),
 last_update timestamp,
 special_features varchar[],
 full_text varchar(300)
);

create table film_category(
 film_id float,
 category_id float,
 last_update timestamp
);

create table category(
 category_id int primary key,
 name varchar(50),
 last_update timestamp
);

\copy actor from 'content/data/actor.csv' delimiter ',' csv header;
\copy film from 'content/data/film.csv' delimiter ',' csv header;
\copy film_actor from 'content/data/film_actor.csv' delimiter ',' csv header;
\copy rental from 'content/data/rental.csv' delimiter ',' csv header;
\copy language from 'content/data/language.csv' delimiter ',' csv header;
\copy category from 'content/data/category.csv' delimiter ',' csv header;
\copy film_category from 'content/data/film_category.csv' delimiter ',' csv header;