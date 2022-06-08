#!/usr/bin/python3

import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html.jinja"

people = [
    {
        'name' : 'Marty',
        'dog' : 'Nani',
    },
    {
        'name' : 'Josh',
        'dog' : 'Hugo',
    },
]

template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(my_collection=people)  # this is where to put args to the template renderer
print(outputText)