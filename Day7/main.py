#Introuction to Python functions.

def my_print(txt):
    print(txt)

msg_template = """
    Hello {name}, 
    Thank you for joining {website}
"""

def format_msg(name='Zlatan', website='30DaysOfPython'):
    msg = msg_template.format(name=name, website=website)
    return msg

names = [
    'Justin',
    'Mike',
    'John',
    'Mark'
]

for name in names:
    this_person_msg = format_msg(name=name)
    print(this_person_msg)

#Funcion parameters types
"""
    "{} {}".format('abc', 123) - Positional parameters (*args)
    "{name} {number}".format('abc', 123) - Keyword arguments  (**kwargs)  
"""

def base_function(*args, **kwargs):
    print(args, kwargs)

