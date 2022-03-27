from django import template

register = template.Library()

@register.filter(name='comma_format')
def comma_format(value):

    input = str(value).split(".")[0]
    if len(input) <= 3:
        return str(value)
    else:
        response = ""
        for char in input[::-1]:
            response = char + response
            if len("".join(response.split(","))) % 3 == 0:
                response = "," + response
        if response[0] == ",":
            response = response[1:]
        return response