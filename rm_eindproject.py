def main():
	Total_Dutch_population = 17282163
	Dutch_population = 16171304
	Bulgarian_population = 31208
	Moroccan_population = 36495
	Polish_population = 144001
	Turkish_population = 74834
	
	Total_Dutch_crimes = 220280
	Dutch_crimes = 196980
	Bulgarian_crimes = 730
	Moroccan_crimes = 3440
	Polish_crimes = 3510
	Turkish_crimes = 1880
	
	crime_percentage_Dutch = Dutch_crimes / Total_Dutch_crimes * 100
	crime_percentage_Bulgarian = Bulgarian_crimes / Total_Dutch_crimes * 100
	crime_percentage_Moroccan = Moroccan_crimes / Total_Dutch_crimes * 100
	crime_percentage_Polish = Polish_crimes / Total_Dutch_crimes * 100
	crime_percentage_Turkish = Turkish_crimes / Total_Dutch_crimes * 100
	
	pop_percentage_Dutch = Dutch_population / Total_Dutch_population * 100
	pop_percentage_Bulgarian = Bulgarian_population / Total_Dutch_population * 100
	pop_percentage_Moroccan = Moroccan_population / Total_Dutch_population * 100
	pop_percentage_Polish = Polish_population / Total_Dutch_population * 100
	pop_percentage_Turkish = Turkish_population / Total_Dutch_population * 100
	
	print("The Dutch people are accountable for {0}% of the crimes. People with a Dutch background are {1}% of the Dutch population. ".format(round(crime_percentage_Dutch , 2) , round(pop_percentage_Dutch , 2)))
	print("The Bulgarian people are accountable for {0}% of the crimes. People with a Bulgarian background are {1}% of the Dutch population. ".format(round(crime_percentage_Bulgarian , 2) , round(pop_percentage_Bulgarian , 2)))
	print("The Moroccan people are accountable for {0}% of the crimes. People with a Moroccan background are {1}% of the Dutch population. ".format(round(crime_percentage_Moroccan , 2) , round(pop_percentage_Moroccan , 2)))
	print("The Polish people are accountable for {0}% of the crimes. People with a Polish background are {1}% of the Dutch population. ".format(round(crime_percentage_Polish , 2) , round(pop_percentage_Polish , 2)))
	print("The Turkish people are accountable for {0}% of the crimes. People with a Turkish background are {1}% of the Dutch population. ".format(round(crime_percentage_Turkish , 2) , round(pop_percentage_Turkish , 2)))

	
main()
	
	




