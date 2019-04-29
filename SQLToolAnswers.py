import pandas as pd
from sqlalchemy import create_engine

# Note: if an interpreter error occurs, the traceback could reveal the answers

''' Question-Answer Frameworks '''

# Base functions to make the questions
# Evaluates questions where the answer is a string
def StringQuestion(user_answer, string_ans):
	if user_answer.upper() == string_ans.upper():
		print ("Correct!")
	else:
		print ("Let's think about this one again.")
	return

# Evalulates questions where the answer is a query's output
# Requires that the field names are the same aka no aliases
def QueryComparison(user_answer, query):
	engine = create_engine('postgresql+psycopg2://andrewmahler@localhost:5432/sqltool')
	true_answer = pd.read_sql_query(query, con=engine).sort_index(axis=1)
	# First check: do they have the same fields?
	true_fields_dtypes = true_answer.dtypes.to_dict()
	user_fields_dtypes = user_answer.dtypes.to_dict()
		# Second check: are these fields the same data type?
	for key, value in true_fields_dtypes.items():
		# Statement to indentify whether the field in the true answer is present in the user answer
		if key in user_fields_dtypes.keys():
			if value != user_fields_dtypes[key]:
				''' If they have the same field but they're different data types then cast the user column to the true column's type '''
				user_answer[key] = user_answer[key].astype(value)
		else:
			print ("Let's think about this one again")
			return 
		
	# Last check: are the dataframes the same?
	score = true_answer.equals(user_answer)
	if score == True:
		return print ("Correct!")
	elif score == False:
		return print ("Let's think about this one again.")
	
	engine.dispose()

	return

''' ACTUAL QUESTIONS '''

# Question 1.1
def PaymentPrimaryKeyQuestion(answer):
	StringQuestion(answer, "payment_id")

# Question 1.2
def CustomerPrimaryKeyQuestion(answer):
	StringQuestion(answer, "customer_id")

# Question 2
def PaymentDataTypeQuestion(answer):
	StringQuestion(answer, "numeric")

# Question 3
def AfricanEggQuestion(answer):
	query = """
	select description, release_year, rental_rate 
	from film 
	where UPPER(title) = 'AFRICAN EGG'
	"""

	# Answer is in the form of 
	QueryComparison(answer.DataFrame().sort_index(axis=1), query)