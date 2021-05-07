import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import csv

df = pd.read_csv('StudentsPerformance.csv')

math_list = df["math score"].tolist()
reading_list = df["reading score"].tolist()
writing_list = df["writing score"].tolist()

math_mean = st.mean(math_list)
reading_mean = st.mean(reading_list)
writing_mean = st.mean(writing_list)

math_median = st.median(math_list)
reading_median = st.median(reading_list)
writing_median = st.median(writing_list)

math_mode = st.mode(math_list)
reading_mode = st.mode(reading_list)
writing_mode = st.mode(writing_list)

print('mean , median and mode for the Math score is {} , {} and {} respectively'.format(math_mean,math_median,math_mode))
print('mean , median and mode for the reading score is {} , {} and {} respectively'.format(reading_mean,reading_median,reading_mode))
print('mean , median and mode for the writing score is {} , {} and {} respectively'.format(writing_mean,writing_median,writing_mode))

math_std_dev = st.stdev(math_list)
reading_std_dev = st.stdev(reading_list)
writing_std_dev = st.stdev(writing_list)

math_first_std_dev_start,math_first_std_dev_end = math_mean-math_std_dev,math_mean+math_std_dev
math_second_std_dev_start,math_second_std_dev_end = math_mean-(2*math_std_dev),math_mean+(2*math_std_dev)
math_third_std_dev_start,math_third_std_dev_end = math_mean-(3*math_std_dev),math_mean+(3*math_std_dev)

reading_first_std_dev_start,reading_first_std_dev_end = reading_mean-reading_std_dev,reading_mean+reading_std_dev
reading_second_std_dev_start,reading_second_std_dev_end = reading_mean-(2*reading_std_dev),reading_mean+(2*reading_std_dev)
reading_third_std_dev_start,reading_third_std_dev_end = reading_mean-(3*reading_std_dev),reading_mean+(3*reading_std_dev)

writing_first_std_dev_start,writing_first_std_dev_end = writing_mean-writing_std_dev,writing_mean+writing_std_dev
writing_second_std_dev_start,writing_second_std_dev_end = writing_mean-(2*writing_std_dev),writing_mean+(2*writing_std_dev)
writing_third_std_dev_start,writing_third_std_dev_end = writing_mean-(3*writing_std_dev),writing_mean+(3*writing_std_dev)

math_list_of_data_within_first_std_dev = [result for result in math_list if result>math_first_std_dev_start and result<math_first_std_dev_end]
math_list_of_data_within_second_std_dev = [result for result in math_list if result>math_second_std_dev_start and result<math_second_std_dev_end]
math_list_of_data_within_third_std_dev = [result for result in math_list if result>math_third_std_dev_start and result<math_third_std_dev_end]

reading_list_of_data_within_first_std_dev = [result for result in reading_list if result>reading_first_std_dev_start and result<reading_first_std_dev_end]
reading_list_of_data_within_second_std_dev = [result for result in reading_list if result>reading_second_std_dev_start and result<reading_second_std_dev_end]
reading_list_of_data_within_third_std_dev = [result for result in reading_list if result>reading_third_std_dev_start and result<reading_third_std_dev_end]

writing_list_of_data_within_first_std_dev = [result for result in writing_list if result>writing_first_std_dev_start and result<writing_first_std_dev_end]
writing_list_of_data_within_second_std_dev = [result for result in writing_list if result>writing_second_std_dev_start and result<writing_second_std_dev_end]
writing_list_of_data_within_third_std_dev = [result for result in writing_list if result>writing_third_std_dev_start and result<writing_third_std_dev_end]

percentage_math_infirst_std_dev = (len(math_list_of_data_within_first_std_dev)/len(math_list))*100
percentage_math_insecond_std_dev = (len(math_list_of_data_within_second_std_dev)/len(math_list))*100
percentage_math_inthird_std_dev = (len(math_list_of_data_within_third_std_dev)/len(math_list))*100

percentage_reading_infirst_std_dev = (len(reading_list_of_data_within_first_std_dev)/len(reading_list))*100
percentage_reading_insecond_std_dev = (len(reading_list_of_data_within_second_std_dev)/len(reading_list))*100
percentage_reading_inthird_std_dev = (len(reading_list_of_data_within_third_std_dev)/len(reading_list))*100

percentage_writing_infirst_std_dev = (len(writing_list_of_data_within_first_std_dev)/len(writing_list))*100
percentage_writing_insecond_std_dev = (len(writing_list_of_data_within_second_std_dev)/len(writing_list))*100
percentage_writing_inthird_std_dev = (len(writing_list_of_data_within_third_std_dev)/len(writing_list))*100

print('{}% of data for math lies between first standard deviation'.format(percentage_math_infirst_std_dev))
print('{}% of data for math lies between second standard deviation'.format(percentage_math_insecond_std_dev))
print('{}% of data for math lies between third standard deviation'.format(percentage_math_inthird_std_dev))

print('{}% of data for reading lies between first standard deviation'.format(percentage_reading_infirst_std_dev))
print('{}% of data for reading lies between second standard deviation'.format(percentage_reading_insecond_std_dev))
print('{}% of data for reading lies between third standard deviation'.format(percentage_reading_inthird_std_dev))

print('{}% of data for writing lies between first standard deviation'.format(percentage_writing_infirst_std_dev))
print('{}% of data for writing lies between second standard deviation'.format(percentage_writing_insecond_std_dev))
print('{}% of data for writing lies between third standard deviation'.format(percentage_writing_inthird_std_dev))