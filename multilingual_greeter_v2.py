from typing import Dict

def print_lang_only(dict1):
    for key,value in dict1.items():
        print(key, value)

mode_dict = {
    1: 'Admin',
    2: 'User'
}

admin_mode_dict = {
    1: 'Add Language',
    2: 'Update Language',
    3: 'Delete Language',
    4: 'Exit'
}

def print_mode_option(dict1):
    print('Please choose a mode option: ')
    for key, value in dict1.items():
        print(key, value)

def mode_input():
    return int(input())

def get_mode(mode_key):
    return mode_dict[mode_key]

def print_mode_action(dict1):
    print('Please choose an Admin action: ')
    for key, value in dict1.items():
        print(key, value)

def get_admin_mode_option():
    return int(input())

def add_language_prompt():
    lang_add = input('Enter a language to add: ')
    return lang_add

def add_language_loop(dict1):
    total = 0
    for key in dict1:
        total += 1
    return total

def add_lang_fcn(dict1, num1, string1):
    dict1[num1+1] = string1

def update_language_prompt():
    lang_update = int(input('Enter a current language key to update: '))
    return lang_update

def update_language_prompt2():
    lang_update2 = input('Enter a new language value: ')
    return lang_update2

def del_language_prompt():
    lang_del = int(input('Choose a language key to delete: '))
    return lang_del

def del_language_fcn(dict1, key1):
    return dict1.pop(key1)


# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English',
             2: 'Spanish',
             3: 'Portuguese'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?',
                    2: '¿Cómo te llamas?',
                    3: 'Qual é o seu nome?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: 'Hello',
                  2: 'Hola',
                  3: 'Olá'}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print('Please choose a language: ')
    for key, value in lang_options.items():
        print(f'{key}: {value}')

def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    lang_choice = int(input('Enter a language number:'))
    return lang_choice


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    #lang_options = lang_dict.keys()

    return lang_choice in lang_options


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """

    return name_prompt_options[lang_choice]


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    your_name = input(name_prompt)
    return your_name


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """

    print(greetings_options[lang_choice] + ' ' + name)





if __name__ == '__main__':

    print_mode_option(mode_dict)
    mode_choice = mode_input()


    if mode_choice == 1:
        cond = True
        while cond:
            print_mode_action(admin_mode_dict)
            action_choice = get_admin_mode_option()


            if action_choice == 1:
                lang_add_choice = add_language_prompt()

                if ((type(lang_add_choice) == str) and (lang_add_choice.capitalize() not in lang_dict.values())):
                    print(f'{lang_add_choice} added')
                    lang_num = add_language_loop(lang_dict)
                    add_lang_fcn(lang_dict, lang_num, lang_add_choice)
                    print_lang_only(lang_dict)


                elif ((type(lang_add_choice) == str)) and (lang_add_choice.capitalize() in lang_dict.values()):
                    print(f'{lang_add_choice} already exists')
                    print_lang_only(lang_dict)

                else:
                    print(f'{lang_add_choice} is an invalid language')
                    print_mode_action(admin_mode_dict)

            elif action_choice == 2:
                print_lang_only(lang_dict)
                lang_update_choice = update_language_prompt()
                print(lang_update_choice)

                if lang_update_choice in lang_dict.keys():
                    lang_update_choice2 = update_language_prompt2()
                    lang_dict[lang_update_choice] = lang_update_choice2
                    print(f'{lang_update_choice2} has been udpated to {lang_update_choice2}')
                    print_lang_only(lang_dict)

                else:
                    print(f'{lang_update_choice} is not a valid selection')

            elif action_choice == 3:
                print_lang_only(lang_dict)
                lang_del_choice = del_language_prompt()

                if lang_del_choice in lang_dict.keys():
                    lang_del_choice = del_language_fcn(lang_dict, lang_del_choice)
                    print(f'{lang_del_choice} has been removed')
                    print_lang_only(lang_dict)

                else:
                    print(f'{lang_del_choice} is not a valid selection')

            elif action_choice == 4:
                break

    elif mode_choice == 2:
        print_language_options(lang_dict)
        chosen_lang = language_input()
        while language_choice_is_valid(lang_dict, chosen_lang) is False:
            print("Invalid selection. Try again.")
            chosen_lang = language_input()

        selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
        chosen_name = name_input(selected_prompt)
        greet(chosen_name, greetings_dict, chosen_lang)