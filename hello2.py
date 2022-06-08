#!/usr/bin/python3

import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = "template.html.jinja"

people = [
    {
        'name' : 'Marty',
        'pet' : 'Nani',
    },
    {
        'name' : 'Dima',
        'pet' : 'Scotchy',
    },
    {
        'name' : 'Josh',
        'pet' : 'Hugo',
    },
]

template = templateEnv.get_template(template_file)
outputText = template.render(my_collection=people)  # this is where to put args to the template renderer
print(outputText)
