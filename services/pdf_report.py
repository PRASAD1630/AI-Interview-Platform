from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    filename,
    role,
    ats_score,
    skills,
    missing_skills
):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Interview Platform - ATS Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Target Role: {role}",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"ATS Score: {ats_score}%",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Detected Skills",
            styles["Heading3"]
        )
    )

    for skill in skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading3"]
        )
    )

    for skill in missing_skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    pdf.build(content)