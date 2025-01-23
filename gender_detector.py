import gender_guesser.detector as gender
import pandas as pd

def shorten_gender(gender):
    if gender == 'male':
        return 'm'
    elif gender == 'female':
        return 'f'
    else:
        return gender

data_frame = pd.read_csv('names.csv', header=None)
name_column = data_frame.iloc[:, 0].str.strip()

name_type = input(
        "Do you use full names or first names? (full/first): "
    ).strip().lower()

if name_type == 'full':
    direction = input(
        "Are the names in 'LastName FirstName' ('Vezetéknév Keresztnév') order? (yes/no): "
    ).strip().lower()

    if direction == 'yes':
        data_frame['First Name'] = name_column.str.split().str.get(-1)
    elif direction == 'no':
        data_frame['First Name'] = name_column.str.split().str.get(0)
    else:
        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

elif name_type == 'first':
    data_frame['First Name'] = name_column
    
else:
    raise ValueError("Invalid input. Please enter 'full' or 'first'.")

detector = gender.Detector(case_sensitive=False)

data_frame['Gender'] = data_frame['First Name'].apply(detector.get_gender)
data_frame['Gender'] = data_frame['Gender'].apply(shorten_gender)

data_frame.to_csv('names_with_genders.csv', index=False, encoding='utf-8-sig')
print('Done')
