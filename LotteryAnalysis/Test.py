import pandas as pd
import os
import random as rd
filePath = r'./files/'
#1976年7月13日，增加為36球。
#1983年8月16日，增加為約40球。
#1988年10月6日，增加為42球。
#1990年01月31日第 08 期增加為 45 球                                                                    
#1996年06月11日第 46 期增加為 47 球                                                   
#2002年07月04日第 53 期增加為 49 球

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
df = pd.read_csv(os.path.join(filePath, 'all_years.csv'))
df = df[(df['YEAR'] > 2002) | ((df['YEAR'] == 2002) & (df['TIMES'] >= 53))]
# Create a DataFrame with numbers 1-49 as strings
#before1990Times08_number_list = [int(i) for i in range(1, 46)]
#before1996Times46_number_list = [int(i) for i in range(1, 48)]
After2020NumberList = [int(i) for i in range(1, 50)] # After 2002, there are 49 balls
doubleDigits = [i for i in After2020NumberList if i >=10] # Check if the number is double-digit
rawData = df.loc[:, 'N1':'S1'].values.ravel()  # Flatten the DataFrame to a 1D array

# Count occurrences ol each number
def count_occurrencesOfEachNumer(data, number_list):
    counts = {num: 0 for num in number_list}
    for number in data:
        if number in counts:
            counts[number] += 1
    return counts
def sum_of_occurrences(df):
    return df['Count'].sum()
def rate_of_occurrences(df,total):
    result = df.copy()
    result['Rate'] = (result['Count'] / total * 100).round(3) if total > 0 else 0
    return result[['MarkSixNumber','Rate']]
def sort_by_count(df):
    return (df.sort_values(by='Count', ascending=False))
# Count occurrences of each number in the raw data
allNumber_counts = count_occurrencesOfEachNumer(rawData, After2020NumberList)
print("All Numbers Occurrences Count: \n", allNumber_counts) #return a dictionary with counts of each number
df_allNumber_counts = pd.DataFrame(list(allNumber_counts.items()), columns=['MarkSixNumber', 'Count'])
# Sort the DataFrame by count in descending order
df_allNumber_counts = sort_by_count(df_allNumber_counts)
print("All Numbers Occurrences: \n", df_allNumber_counts)
# Calculate the sum of occurrences
allNumber_Sum = sum_of_occurrences(df_allNumber_counts)  # Total occurrences of all numbers
print(f"Total occurrences of all numbers: {allNumber_Sum}")
# Calculate the rate of occurrences for all numbers
allNumber_rate = rate_of_occurrences(df_allNumber_counts,allNumber_Sum)  # Rate of occurrences for all numbers
print("Rate of Occurrences for All Numbers:\n", allNumber_rate)

# Filter double-digit numbers and their counts  
doubleDigitsNumber_counts = df_allNumber_counts[(df_allNumber_counts['MarkSixNumber'] >= 10) & (df_allNumber_counts['Count'] > 0)]  # Filter double-digit numbers
print("Double-Digit Numbers Occurrences:\n", doubleDigitsNumber_counts)
# Calculate the sum of double-digit occurrences
doubleDigits_Sum = doubleDigitsNumber_counts['Count'].sum() # Sum of double-digit counts
print(f"Total occurrences of double-digit numbers: {doubleDigits_Sum}")
# Calculate the rate of occurrences for double-digit numbers
doubleDigits_rate = rate_of_occurrences(doubleDigitsNumber_counts, allNumber_Sum)  # Rate of double-digit occurrences
print("Rate of Occurrences for Double-Digit Numbers:\n", doubleDigits_rate)

oddNumbers = df_allNumber_counts[df_allNumber_counts['MarkSixNumber'] % 2 != 0]  # Filter odd numbers
evenNumbers = df_allNumber_counts[df_allNumber_counts['MarkSixNumber'] % 2 == 0]  # Filter even numbers
oddNumbers_Sum = oddNumbers['Count'].sum()  # Sum of odd numbers counts
evenNumbers_Sum = evenNumbers['Count'].sum()  # Sum of even numbers counts
oddNumbers_rate = rate_of_occurrences(oddNumbers, allNumber_Sum)  # Rate of odd numbers occurrences
evenNumbers_rate = rate_of_occurrences(evenNumbers, allNumber_Sum)  # Rate of even numbers occurrences
# Display the occurrences of odd and even numbers 
print("Odd Numbers Occurrences:")
print(oddNumbers)
print("Even Numbers Occurrences:")
print(evenNumbers)
print(f"Total occurrences of odd numbers: {oddNumbers_Sum}")
print(f"Total occurrences of even numbers: {evenNumbers_Sum}")
print("Rate of Occurrences for Odd Numbers:\n", oddNumbers_rate)
print("Rate of Occurrences for Even Numbers:\n", evenNumbers_rate)
print(oddNumbers_rate['Rate'].sum() / oddNumbers_rate['Rate'].count()) 
print(evenNumbers_rate['Rate'].sum() / evenNumbers_rate['Rate'].count())

'''rearch of the sequence of numbers in N1 to S1
number1InN1_counts = df[df['N1']==1].count()['N1']  # Count occurrences of number 1 in N1
print("Occurrences of number 1 in N1:\n", number1InN1_counts)
number1InN2_counts = df[df['N2']==1].count()['N2']  # Count occurrences of number 1 in N1
print("Occurrences of number 1 in N2:\n", number1InN2_counts)
'''
#lastTenTimes = df.tail(1000)  # Get the last 10 rows
#print("Last 20 Times:\n", lastTenTimes, "\n")

#Rgresstion Test
RegresstionTest = df.copy()  # Get the last 100 rows
# Check if the last 10 times contain specific numbers in N1 and N2
target_numbers = []
for i in range(len(RegresstionTest)):
    result = df[(df['N1'] == RegresstionTest.iloc[i]['N1']) & (df['N2'] == RegresstionTest.iloc[i]['N2'])]
    print(f"The MarkSix row:\n {RegresstionTest.iloc[[i]]}")
    print(f"Match for lastTenTimes row {i}:")
    print(result, '\n Occurrences count: ', len(result))
    if len(result) > 30:
        target_numbers.append((RegresstionTest.iloc[i]['N1'], RegresstionTest.iloc[i]['N2'], len(result)))
    print('\n')
print(f"How many combine : {len(target_numbers)} Times:\n")
for number in list(set(target_numbers)):
    print(f"N1: {number[0]}, N2: {number[1]}, Occurrences Count: {number[2]}")
'''
numberInN3_counts = df['N3'].value_counts().reindex(After2020NumberList, fill_value=0)
print("Occurrences of each number in N3:\n", numberInN3_counts)
numberInN4_counts = df['N4'].value_counts().reindex(After2020NumberList, fill_value=0)
print("Occurrences of each number in N4:\n", numberInN4_counts)
numberInN5_counts = df['N5'].value_counts().reindex(After2020NumberList, fill_value=0)
print("Occurrences of each number in N5:\n", numberInN5_counts)
numberInN6_counts = df['N6'].value_counts().reindex(After2020NumberList, fill_value=0)
print("Occurrences of each number in N5:\n", numberInN6_counts)
'''




