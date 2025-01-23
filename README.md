# Python Gender detector

- Uses library: <https://pypi.org/project/gender-guesser/>
- Detects the gender based on the First name (given name)
- Can be used with **Full names** or with just **First Names**

## Usage

1. install a python version from Microsoft Store
2. install the following python libraries

    ```sh
    pip install gender-guesser
    ```

    ```sh
    pip install pandas
    ```

3. copy the file named ```names.csv``` to the folder where the script is

    - The file should only contain one column, without a header
    - Each line should contain one name. The name can be the full name or just the first name (see example_input.csv).
        - If full name is used, you will prompted to answer wether the name starts with the last name or the first name.

4. run the script with ```python gender_detector.py```
5. answer the questions prompted
6. the result is stored in ```names_with_genders.csv``` in the same folder
7. correct the genders manually for the names that didn't match
