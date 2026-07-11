from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path
from datetime import datetime

def generate_report(tweet, result):

    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    filename = reports_folder / f"Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(str(filename))

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Women Safety AI Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Date:</b> {datetime.now()}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Input Text</b>", styles["Heading2"]))
    story.append(Paragraph(tweet, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Prediction Result</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Sentiment : {result['sentiment']}",
        styles["BodyText"]
    ))

    story.append(Paragraph(
        f"Risk Level : {result['risk_level']}",
        styles["BodyText"]
    ))

    story.append(Paragraph(
        f"Risk Score : {result['risk_score']}/10",
        styles["BodyText"]
    ))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Detected Keywords</b>", styles["Heading2"]))

    if result["keywords"]:

        for word in result["keywords"]:
            story.append(Paragraph(f"• {word}", styles["BodyText"]))

    else:

        story.append(Paragraph("None", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Recommendations</b>", styles["Heading2"]))

    for rec in result["recommendation"]:
        story.append(Paragraph(f"• {rec}", styles["BodyText"]))

    doc.build(story)

    return filename