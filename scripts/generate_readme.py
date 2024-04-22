import os
import jinja2

template_file = "README.md.jinja"
output_file = "README.md"
context = {
    "project_name": os.getenv('PROJECT_NAME', 'Default Project Name'),
    "pages_url": os.getenv('PAGES_URL', 'https://default.github.io/repository-name'),
    "project_description": os.getenv('PROJECT_DESCRIPTION', 'Default project description.'),
    "repository_url": os.getenv('REPOSITORY_URL', 'https://github.com/default/repository-name')
}

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(template_file)

outputText = template.render(context)  # this is where to put args to the template renderer
with open(output_file, "w") as f:
    f.write(outputText)