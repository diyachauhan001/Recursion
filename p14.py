def reverse_string(s):
    if s == "":
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

input_string = "hello"
print(f"The reversed string of '{input_string}' is: {reverse_string(input_string)}")
