import json
import os
from jinja2 import Environment, FileSystemLoader


class Report:
    def __init__(self, data):
        self.data = data

    def save_json(self, filename="report.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def save_html(self, filename="report.html"):
        template_dir = os.path.join(
            os.path.dirname(__file__),
            "templates"
        )

        env = Environment(
            loader=FileSystemLoader(template_dir)
        )

        template = env.get_template("report_template.html")

        html = template.render(report=self.data)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

    def __str__(self):
        return json.dumps(self.data, indent=4)