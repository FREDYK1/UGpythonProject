import streamlit as sl


def convert_to_ascii(input_string):
    ascii_char_values = [f"{char}: {ord(char)}" for char in input_string]
    return ', '.join(ascii_char_values)


sl.title("ASCII Converter")
sl.subheader("Let's convert characters of a string ")


user_input = sl.text_input("Enter your string here:", key="string")

if user_input:
    ascii_values = convert_to_ascii(user_input)
    sl.write(f"ASCII values: {ascii_values}")
else:
    sl.write("Please enter a string to convert.")
user_input = input("Enter your string her")
