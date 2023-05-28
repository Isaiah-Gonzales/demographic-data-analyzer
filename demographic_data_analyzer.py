import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    males = df[df['sex'] == 'Male']
    average_age_men = round(males['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree? (highest education is bachelors) 
    number_highest_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round(((number_highest_bachelors/df.shape[0])*100),1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df[df['education'].str.contains('|'.join(['Bachelors','Masters','Doctorate']))]
    lower_education = df[~df['education'].str.contains('|'.join(['Bachelors','Masters','Doctorate']))]

    # percentage with salary >50K
    higher_education_rich = round((((higher_education[higher_education['salary'] == '>50K'].shape[0])/(higher_education.shape[0])) *100),1)
    lower_education_rich = round((((lower_education[lower_education['salary'] == '>50K'].shape[0])/(lower_education.shape[0])) *100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = int(((min_workers[min_workers['salary'] == '>50K'].shape[0])/(num_min_workers))*100)

    # What country has the highest percentage of people that earn >50K?
    df = df.rename(columns={'native-country':'native_country'})
    unique_countries = df.native_country.unique()
    percent_high_earners_in_country = {}
    for x in unique_countries:
      num_high_salary = len(df[(df['native_country']==str(x)) & (df['salary']=='>50K')])
      country_population = len(df[(df['native_country']==str(x))])
      percent_high = (num_high_salary/country_population)*100
      percent_high_earners_in_country.update({str(x):percent_high})
    highest_earning_country = max(percent_high_earners_in_country, key=percent_high_earners_in_country.get)
    highest_earning_country_percentage = round(max(percent_high_earners_in_country.values()),1)
  
    #another way to solve this using what I learned during "Identify the most popular occupation for those who earn >50K in India"
    #df3 = df[df['salary']=='>50K']
    #highest_earning_country = df3['native_country'].mode()[0]
    #highest_earning_country_percentage = ((df3['native_country']==highest_earning_country).shape[0]/(df['native_country']==highest_earning_countr()).shape[0])*100

    # Identify the most popular occupation for those who earn >50K in India.
    df2 = df[(df['native_country']=='India') & (df['salary']=='>50K')]
    top_IN_occupation = df2['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
