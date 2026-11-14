from jinja2 import Environment, FileSystemLoader

def render_markdown(profile):

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template(
        "me_template.md"
    )

    return template.render(**profile)
