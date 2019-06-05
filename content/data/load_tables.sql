create table actor(
 actor_id int primary key,
 first_name varchar(50),
 last_name varchar(50),
 last_update timestamp
);

create table category(
 category_id int primary key,
 name varchar(50),
 last_update timestamp
);

create table film(
 film_id int primary key,
 title varchar(150),
 description varchar(300),
 release_year double precision,
 language_id double precision,
 rental_duration double precision,
 rental_rate double precision,
 length int,
 replacement_cost double precision,
 rating varchar(50),
 last_update timestamp,
 special_features varchar[],
 full_text varchar(300)
);

create table film_actor(
 actor_id int,
 film_id double precision,
 last_update timestamp
);

create table film_category(
 film_id double precision,
 category_id double precision,
 last_update timestamp
);

create table address(
 address_id int primary key,
 address varchar(200),
 address2 varchar(200),
 district varchar(100),
 city_id double precision,
 postal_code double precision,
 phone varchar(20),
 last_update varchar(50)
);

create table city(
 city_id int primary key,
 city varchar(50),
 country_id double precision, 
 last_update timestamp
);

create table country(
 country_id float primary key,
 country varchar(50),
 last_update varchar(50)
);

create table customer(
 customer_id int primary key,
 store_id float,
 first_name varchar(100),
 last_name varchar(100),
 email varchar(100),
 address_id varchar(100),
 active_bool varchar(10),
 create_date timestamp,
 last_update timestamp,
 active varchar(10)
);

create table inventory(
 inventory_id varchar(20) primary key,
 film_id float,
 store_id float,
 last_update timestamp
);

create table language(
 language_id int primary key,
 name varchar(50),
 last_update timestamp
);

create table payment(
 payment_id int primary key,
 customer_id float,
 staff_id varchar(10),
 rental_id varchar(10),
 amount varchar(10),
 payment_date timestamp
);

create table rental(
 rental_id double precision primary key,
 rental_date timestamp,
 inventory_id double precision,
 customer_id double precision,
 return_date timestamp,
 staff_id int,
 last_update timestamp
);

create table staff(
 staff_id int primary key,
 first_name varchar(50),
 last_name varchar(50),
 address_id varchar(10),
 email varchar(100),
 store_id varchar(10),
 active varchar(10),
 username varchar(100),
 password varchar(100),
 last_update varchar(100),
 picture varchar(100)
);

create table store(
 store_id int,
 manager_staff_id double precision,
 address_id double precision,
 last_update varchar(50)
);

\copy actor from 'content/data/actor.csv' delimiter ',' csv header;
\copy category from 'content/data/category.csv' delimiter ',' csv header;
\copy film from 'content/data/film.csv' delimiter ',' csv header;
\copy film_actor from 'content/data/film_actor.csv' delimiter ',' csv header;
\copy film_category from 'content/data/film_category.csv' delimiter ',' csv header;
\copy address from 'content/data/address.csv' delimiter ',' csv header;
\copy city from 'content/data/city.csv' delimiter ',' csv header;
\copy country from 'content/data/country.csv' delimiter ',' csv header;
\copy customer from 'content/data/customer.csv' delimiter ',' csv header;
\copy inventory from 'content/data/inventory.csv' delimiter ',' csv header;
\copy language from 'content/data/language.csv' delimiter ',' csv header;
\copy payment from 'content/data/payment.csv' delimiter ',' csv header;
\copy rental from 'content/data/rental.csv' delimiter ',' csv header;
\copy staff from 'content/data/staff.csv' delimiter ',' csv header;
\copy store from 'content/data/store.csv' delimiter ',' csv header;
