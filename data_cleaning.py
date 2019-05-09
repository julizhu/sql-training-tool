import pandas as pd
import random

input_file = ['rental_data/2163.dat',
'rental_data/2165.dat',
'rental_data/2167.dat',
'rental_data/2168.dat',
'rental_data/2169.dat',
'rental_data/2171.dat',
'rental_data/2173.dat',
'rental_data/2175.dat',
'rental_data/2177.dat',
'rental_data/2179.dat',
'rental_data/2181.dat',
'rental_data/2183.dat',
'rental_data/2185.dat',
'rental_data/2187.dat',
'rental_data/2189.dat']

output_file = ['content/data/actor.csv',
'content/data/category.csv',
'content/data/film.csv',
'content/data/film_actor.csv',
'content/data/film_category.csv',
'content/data/address.csv',
'content/data/city.csv',
'content/data/country.csv',
'content/data/customer.csv',
'content/data/inventory.csv',
'content/data/language.csv',
'content/data/payment.csv',
'content/data/rental.csv',
'content/data/staff.csv',
'content/data/store.csv']

file_header = [['actor_id', 'first_name', 'last_name', 'last_update'],
	['category_id', 'name', 'last_update'],
	['film_id', 'title', 'description', 'release_year', 'language_id', 'rental_duration', 'rental_rate', 'length', 'replacement_cost', 'rating', 'last_update', 'special_features', 'full_test'],
	['actor_id', 'film_id', 'last_update'],
	['film_id', 'category_id', 'last_update'],
	['address_id', 'address', 'address2', 'district', 'city_id', 'postal_code', 'phone', 'last_update'],
	['city_id', 'city', 'country_id', 'last_update'],
	['country_id', 'country', 'last_update'],
	['customer_id', 'store_id', 'first_name', 'last_name', 'email', 'address_id', 'active_bool', 'create_date', 'last_update', 'active'],
	['inventory_id', 'film_id', 'store_id', 'last_update'],
	['language_id', 'name', 'last_update'],
	['payment_id', 'customer_id', 'staff_id', 'rental_id', 'amount', 'payment_date'],
	['rental_id', 'rental_date', 'inventory_id', 'customer_id', 'return_date', 'staff_id', 'last_update'],
	['staff_id', 'first_name', 'last_name', 'address_id', 'email', 'store_id', 'active', 'username', 'password', 'last_update', 'picture'],
	['store_id', 'manager_staff_id', 'address_id', 'last_update']]

for i in range(len(input_file)):
	df = pd.read_csv(input_file[i], sep=None, names=file_header[i], engine='python')
	if output_file[i] == 'actor.csv':
		df.at[110, 'first_name'] = 'Laura'
		df.at[101, 'first_name'] = 'Laura'
		df.at[110, 'last_name'] = 'VerHulst'
		df.at[101, 'last_name'] = 'VerHulst'
	if output_file[i] == 'category.csv':
		df = df.head(14)
	if output_file[i] == 'rental.csv':
		df['return_date'].fillna('1900-02-15 09:45:30', inplace=True)
	df = df[:-1]
	df.to_csv(output_file[i], index=False)
