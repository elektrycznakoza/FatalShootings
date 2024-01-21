import pandas as pd
import matplotlib.pyplot as plt

police_shootings_path = "C:/Users/leszek.stanislawski/Downloads/Kodilla/Python/Pandas/Advanced/fatal-police-shootings-data.csv"
police_shootings_df = pd.read_csv(police_shootings_path)
transformed_df = police_shootings_df.groupby(['race', 'signs_of_mental_illness']).size().unstack(fill_value=0)
print('Przekształcona tabela:', transformed_df)
transformed_df.plot(kind='bar', stacked=True)
plt.title('Liczba ofiar interwencji według rasy i oznak choroby psychicznej')
plt.xlabel('Rasa')
plt.ylabel('Liczba ofiar')
plt.show()

transformed_df['percentage_mental_illness'] = transformed_df[True] / transformed_df.sum(axis=1)
max_mental_illness_race = transformed_df['percentage_mental_illness'].idxmax()
print("Przekształcona tabela z odsetkiem oznak choroby psychicznej:")
print(transformed_df)
print("\nNajwiększy odsetek oznak choroby psychicznej występuje wśród osób rasy:", max_mental_illness_race)
police_shootings_df['day_of_week'] = pd.to_datetime(police_shootings_df['date']).dt.day_name()
incidents_by_day = police_shootings_df['day_of_week'].value_counts().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
incidents_by_day.plot(kind='bar', xlabel='Day of the Week', ylabel='Number of Incidents', title='Incidents by Day of the Week')
plt.show()

population_path = "C:/Users/leszek.stanislawski/Downloads/Kodilla/Python/Pandas/Advanced/List_2.csv"
population_df = pd.read_csv(population_path)
population_df.columns = ['Rank_2020', 'Rank_2010', 'State', 'Census population, April 1, 2020', 'Census population, April 1, 2010',
                         'Percent change, 2010–2020', 'Absolute change, 2010-2020', 'Total seats in the U.S. House of Representatives, 2023–2033',
                         'Census population per electoral vote', 'Census population per House seat', 'Percent of the total U.S. population, 2020']
merged_df = pd.merge(police_shootings_df, population_df, how='left', left_on='state', right_on='State')
merged_df['incidents_per_1000'] = merged_df.groupby('state')['id'].transform('count') / (merged_df['Census population, April 1, 2020'] / 1000)

