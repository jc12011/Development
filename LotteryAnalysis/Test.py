import pandas as pd
import os
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
df = df[(df['YEAR'] >= 2002) & (df['TIMES'] >= 53)]
print(df)
# Create a DataFrame with numbers 1-49 as strings
#before1990Times08_number_list = [int(i) for i in range(1, 46)]
#before1996Times46_number_list = [int(i) for i in range(1, 48)]
fullNumberList = [int(i) for i in range(1, 50)] # After 2002, there are 49 balls
print("Numbers 1-49 as list:")
print(fullNumberList)
rawData = df.loc[:, 'N1':'S1'].values.ravel()  # Flatten the DataFrame to a 1D array
print(rawData)
# Count occurrences ol each number
def count_occurrences(data, number_list):
    counts = {num: 0 for num in number_list}
    for number in data:
        if number in counts:
            counts[number] += 1
    return counts
# Count occurrences of each number in the raw data
number_counts = count_occurrences(rawData, fullNumberList)
# Print the counts
print("Number counts:")
for number, count in number_counts.items():
    print(f"{number}: {count}")
# Create a DataFrame from the counts
counts_df = pd.DataFrame(list(number_counts.items()), columns=['MarkSixNumber', 'Count'])
# Sort the DataFrame by count in descending order
counts_df = counts_df.sort_values(by='Count', ascending=True)
# Print the sorted DataFrame
print("\nSorted counts DataFrame:")
print(counts_df)