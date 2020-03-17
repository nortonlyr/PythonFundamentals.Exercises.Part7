from typing import Dict
import random

def print_lang_only(dict1):
    for key,value in dict1.items():
        print(key, value)

mode_dict = {
    1: 'Admin',
    2: 'User'
}

admin_mode_dict = {
    1: 'Add Language',
    2: 'Edit Greeting'
}

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English',
             2: 'Spanish',
             3: 'Portuguese',
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?',
                    2: '¿Cómo te llamas?',
                    3: 'Qual é o seu nome?',
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: ["Hello", "What's Up", "Good day"],
                  2: ["Hola", "Diga", "Aló"],
                  3: ["Olá", "Oi", "Alô"],
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """

    for key, value in lang_options.items():
        print(f'{key}: {value}')

def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    lang_choice = int(input())
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


def prompt_options(prompt: str, dict_in: Dict[int, str]) -> int:
    print(prompt)
    print_language_options(dict_in)
    choice = language_input()
    while language_choice_is_valid(dict_in, choice) is False:
        print("Invalid selection. Try again.")
        choice = language_input()
    return choice


#Admin mode functions
def add_language(*args):
    print("adding language...")
    print("Enter a language id: ")
    new_lang_id = language_input()
    new_lang_desc = input("What is the name of the new language? ")
    new_lang_prompt = input(f"How do you ask for someone's name in {new_lang_desc}? ")
    new_lang_greeting = input(f"How do you say hello in {new_lang_desc}? ")

    lang_dict[new_lang_id] = new_lang_desc
    name_prompt_dict[new_lang_id] = new_lang_prompt
    greetings_dict[new_lang_id] = [new_lang_greeting]


def edit_greeting():
    print("editing greeting...")
    lang_to_edit = prompt_options("Please choose a language to edit: ", lang_dict)

    greetings_list = greetings_dict.get(lang_to_edit)

    print("Which greeting would you like to edit: ")
    for index, greeting in enumerate(greetings_list):
        print(f"{index}: {greeting}")

    greeting_to_edit = language_input()
    print(f"You've chosen to edit {greeting_to_edit}")

    new_greeting = input("What should the new greeting be?")
    greetings_list[greeting_to_edit] = new_greeting


# User mode functions
def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    # for lang_choice in name_prompt_options:
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

    greeting_list = greetings_options.get(lang_choice)
    random_greeting = random.choice(greeting_list)
    greeting = f'{random_greeting} {name}'
    print(greeting)


def user_mode():
    print("Entering user mode...")
    chosen_lang = prompt_options("Please choose a language: ", lang_dict)
    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)

def admin_mode():
    print("Entering admin mode...")
    chosen_action = prompt_options("Please choose an action.", admin_mode_dict)

    if(chosen_action == 1):
        add_language()
    elif(chosen_action == 2):
        edit_greeting()


def home():
    chosen_mode = prompt_options("Please choose a mode: ", mode_dict)

    if(chosen_mode == 1):
        admin_mode()
    elif (chosen_mode == 2):
        user_mode()
    else:
        print("Invalid mode...")
    home()


if __name__ == '__main__':
    home()
