# Project_ML
Group Project of Machine Learning.

If you have never opened this project before, and therefore have none of the csv files downloaded then follow all the steps below. If you already have the "csv_files_1week" and the "household_power_consumption" folders then go directly to step 3.

1- Create a folder in your local depository called household_power_consumption with all the data from the  kaggle dataset https://www.kaggle.com/datasets/ecoco2/household-appliances-power-consumption . This file is very heavy and is ignored with the .gitignore file on the remote depository.

2- Create an empty folder in your local depository called csv_files_1week. Launch the file data_week_minute_printer.ipynb. All the files containing one week of data with a 1-min timestamp should be added to the folder. This operation takes about 20 minutes.

3- Run the files you want (classification_device.ipynb, classification_category, classification_category_without_other or Random_Forest)

# file explaination

1. Classification_device is the notebook that contains all the classifiers (except for Random forest) for classification based on appliances.
2. Classification_category is the notebook that contain all the classifiers (except for Random forest) for classification based on categories.
3. Classification_category_without_other is the notebook that contain all the classifiers for classification based on categories without considering the category called "other".
4. data_week_minute_printer is the notebook that contains the code for dividing the original month long data into weeks and summing the second long data up into minute long data.
5. exploration_data is the notebook where we explore the data, to try and come up with ways of categorizing it and what features would make sense.
6. name_and_cat is the notebook where the devices are put into a dictionary where each file has information on what appliance it is and what category it belongs to.
7. .gitignore is for ignoring the large dataset, so that it is not so heavy to run.
8. test.csv is a file used for assuring that the code works as intended.
9. test.ipynb is a notebook that is used for assuring that some other code works as intended.
10. household_power_consumption contains the original dataset.
11. csv_files_1week contains that excel files when they have been divided into weeks and summed up to minutes.
12. Random_Forest contains all the categorizations for the random forest. This means that it contains the classifications of appliances, categories, and categories without other. 