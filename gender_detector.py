import gender_guesser.detector as gender
import pandas as pd

HIGHEST_FREQUENCY = 'D'
PREFER_HUNGARIAN_NAMES = True

def add_external_names_to_detector(detector, external_names, gender, country):
    country_index = (detector.COUNTRIES.index(country))

    for name in external_names[0]:
        name = name.lower()
        if name in detector.names:
            gender_country_dict = detector.names[name]

            # if gender matches the one in the dictionary
            if gender in gender_country_dict:
                detector._set(name, gender, gender_country_dict[gender][:country_index] + HIGHEST_FREQUENCY + gender_country_dict[gender][country_index + 1:])
            else:
                detector._set(name, gender, ' ' * country_index + HIGHEST_FREQUENCY + ' ' * (len(detector.COUNTRIES) - country_index))
        else:
            detector._set(name, gender, ' ' * country_index + HIGHEST_FREQUENCY + ' ' * (len(detector.COUNTRIES) - country_index))

def shorten_gender(gender):
    if gender == 'male':
        return 'm'
    elif gender == 'female':
        return 'f'
    else:
        return gender

data_frame = pd.read_csv('names.csv', header=None, encoding='utf-8-sig')
name_column = data_frame[0].str.strip()

name_type = input(
        "Do you use full names or first names? (full/first): "
    ).strip().lower()

if name_type == 'full':
    is_lastname_first = input(
        "Are the names in 'LastName FirstName' ('Vezetéknév Keresztnév') order? (yes/no): "
    ).strip().lower()

    if is_lastname_first == 'yes':
        data_frame['First Name'] = name_column.str.split().str.get(-1)
    elif is_lastname_first == 'no':
        data_frame['First Name'] = name_column.str.split().str.get(0)
    else:
        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

elif name_type == 'first':
    data_frame['First Name'] = name_column
    
else:
    raise ValueError("Invalid input. Please enter 'full' or 'first'.")

external_hungarian_names_female = pd.read_csv('data/external_hungarian_names_female.csv', header=None)
external_hungarian_names_male = pd.read_csv('data/external_hungarian_names_male.csv', header=None)

detector = gender.Detector(case_sensitive=False)

add_external_names_to_detector(detector, external_hungarian_names_female, 'female', 'hungary')
add_external_names_to_detector(detector, external_hungarian_names_male, 'male', 'hungary')

if(PREFER_HUNGARIAN_NAMES):
    data_frame['Gender'] = data_frame['First Name'].apply(lambda name: detector.get_gender(name, 'hungary'))
else:
    data_frame['Gender'] = data_frame['First Name'].apply(detector.get_gender)

data_frame['Gender'] = data_frame['Gender'].apply(shorten_gender)

data_frame.to_csv('names_with_genders.csv', index=False, encoding='utf-8-sig')
print('Done')
