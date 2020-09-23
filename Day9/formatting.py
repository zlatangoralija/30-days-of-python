msg_template = """
    Hello {name}, 
    Thank you for joining {website}
"""

def format_msg(name='Zlatan', website='30DaysOfPython'):
    msg = msg_template.format(name=name, website=website)
    return msg


