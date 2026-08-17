import logging

from docxtpl import DocxTemplate

logger = logging.getLogger(__name__)


class DocxTemplateFiller:
    def __init__(self, template_path: str):
        self.template_path = template_path

    def render(self, values: dict, output_path: str) -> None:
        logger.info("Opening template: %s", self.template_path)
        doc = DocxTemplate(self.template_path)

        logger.info("Rendering %d placeholder(s)", len(values))
        doc.render(values)

        doc.save(output_path)
        logger.info("Saved filled document to: %s", output_path)
