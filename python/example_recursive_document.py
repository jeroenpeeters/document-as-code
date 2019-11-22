"""
    example document - demonstrate how 'Document as Code' works
"""
import pathlib

from yattag import indent

from domain.document.content import fragments
from format.bootstrap import BootstrapDoc


doc, tag, text = BootstrapDoc().tagtext()

headings = (doc.h1, doc.h1, doc.h2, doc.h3, doc.h4)


def show_recursive_fragments(headings, *fragments):

    if headings:
        heading = headings[0]
        remaining_headings = headings[1:]
    else:
        heading = doc.p
        remaining_headings = []

    for fragment in fragments:
        heading(fragment.get_title())
        if fragment.lead:
            doc.p(fragment.lead, klass='lead')
        if fragment.text:
            doc.p(fragment.text)
        show_recursive_fragments(remaining_headings, *(fragment.fragments))


with tag('html'):

    doc.head(fragments.F0.title)

    with tag('body'):

        with tag('div', klass='container'):

            show_recursive_fragments(headings, fragments.F0)


file_path = pathlib.Path(__file__).resolve()
project_dir = file_path.resolve().parent.parent
report_dir = project_dir / "report"
report_file = report_dir / file_path.with_suffix(".html").name

report_file.write_text(indent(doc.getvalue()))

print(f"Ouput in {report_file}")
