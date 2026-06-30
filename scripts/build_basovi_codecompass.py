"""Generate CV/RESUME/LETTER/WELCOME BASOVI docx tailored to the vacancy.

Vacancy: Code Compass (specialist IT recruitment, HQ Wallisellen/Zurich, CH).
Target opening: AI Engineer - Zurich, Switzerland.
Rules (rule.txt + TIPS.md sections 11.x):
  - Company name and any vacancy REF id are excluded from every output file.
  - First paragraph carries a photo. Switzerland is in Europe (not Germany /
    not USA) -> use tips/PHOTO.png.
  - CV: full CV; RESUME: condensed 2-3 roles ~8y; LETTER: cover letter from hint
    with "вставить" replaced by the vacancy hard skills; WELCOME: outreach note.
"""
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor

BASE = Path(r"C:\Users\leto\Documents\GITLAB\excel")

# --- Personal identity (from rule.txt / hint) ---------------------------------
FIRST_NAME = "IURII"
LAST_NAME = "BASOV"
FULL_NAME = f"{FIRST_NAME} {LAST_NAME}"
EMAIL = "basov.yo@gmail.com"
LINKEDIN = "linkedin.com/in/basovi"
WHATSAPP = "+12518009809"
PROFILE = "x.com/topco"

# --- Vacancy facts (company name + any REF id intentionally NOT used) ----------
POSITION = "AI Engineer"
LOCATION = "Zurich, Switzerland"
COMPANY_GENERIC = "a Switzerland-based specialist IT recruitment company"

# Photo selection: Switzerland -> Europe (not Germany / not USA) -> PHOTO.png
PHOTO = BASE / "tips" / "PHOTO.png"

# Suitable technologies derived from the vacancy focus ("вставить" target).
VACANCY_TECH = (
    "Python, Machine Learning, AI/GenAI, Large Language Models (LLMs), data "
    "engineering, Java/Scala, .NET/C#, Node.js, JavaScript/TypeScript, React, "
    "cloud (AWS, Azure, GCP), Kafka and streaming pipelines, PostgreSQL, Docker, "
    "CI/CD, Linux"
)


def add_name_header(doc):
    """First paragraph: photo + name (image lives next to the first paragraph)."""
    p = doc.add_paragraph()
    run_img = p.add_run()
    run_img.add_picture(str(PHOTO), width=Inches(1.0))
    run_name = p.add_run("  " + FULL_NAME)
    run_name.bold = True
    run_name.font.size = Pt(18)

    def line(text):
        para = doc.add_paragraph(text)
        para.paragraph_format.space_after = Pt(0)
        return para

    line(f"Email: {EMAIL} | LinkedIn: {LINKEDIN}")
    line(f"WhatsApp: {WHATSAPP} | Profile: {PROFILE}")
    line(f"Location: {LOCATION} (open to relocation) | Need Visa Sponsorship")


def heading(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1F, 0x3B, 0x5B)
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    return p


def body(doc, text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(2)
    return p


def bullet(doc, text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(1)
    return p


def subhead(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(1)
    return p


# ------------------------------------------------------------------ CV --------
def build_cv():
    doc = Document()
    add_name_header(doc)

    body(doc, f"Target Role: {POSITION}")

    heading(doc, "Professional Summary")
    body(
        doc,
        "AI and machine-learning engineer with 10+ years across end-to-end "
        "analytics, ML platforms, and full-stack delivery. Started as a Java/Scala "
        "developer, moved into ML, and grew into a leadership role heading an ML "
        "platform direction. Designs and ships production AI/GenAI and data systems "
        "in Python on cloud (AWS, Azure, GCP), with strong engineering discipline, "
        "streaming pipelines, and observability. A collaborative play-and-coach "
        "specialist who values team culture and the people behind the product, and "
        "who comfortably works full-stack from data and models to the UI.",
    )

    heading(doc, "Core Technology Stack")
    for item in [
        "Python production engineering for ML/AI and data services",
        "Machine Learning, AI/GenAI, and Large Language Models (LLMs)",
        "Data engineering: streaming and batch pipelines (Kafka, Spark, Airflow)",
        "Backend across Java/Scala and .NET/C#, plus Node.js services",
        "Full-stack delivery with JavaScript/TypeScript and React",
        "Cloud deployment on AWS, Azure, and GCP-compatible architectures",
        "PostgreSQL and relational/non-relational data modeling",
        "Docker, CI/CD pipelines, testing standards, and Linux operations",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Relevant Experience")

    subhead(doc, "Upwork | Lead ML Ops / AI & Data Engineer | 2013-2025")
    for item in [
        "- Designed and operated resilient cloud data platforms with real-time and "
        "streaming pipelines, integrating data across 5 business units and "
        "supporting e-commerce/logistics processing 300,000+ orders/day using "
        "Airflow, PostgreSQL, Apache Spark, S3, and Kafka.",
        "- Built an online credit risk scoring system on Apache NiFi, Kafka, and "
        "Hadoop, and deployed ML models powering a customer chatbot; reduced data "
        "processing latency by 5%, improved model accuracy by 3%, and lifted "
        "chatbot engagement by 18%.",
        "- Engineered a high-performance Demand-Side Platform and real-time stats "
        "system, improving server response time by 30% and supporting a 50% "
        "increase in concurrent users with no performance degradation.",
        "- Worked full-stack from data and models to JavaScript/React interfaces, "
        "with CI/CD and maintainable engineering practices.",
    ]:
        bullet(doc, item)

    subhead(doc, "Sberbank | Lead Software Engineer / ML Platform Lead | 2020-2025")
    for item in [
        "- Led teams and technical tracks for ML platform modernization and AI "
        "solution deployment, with promotion to head of the ML platform direction.",
        "- Provided architecture guidance, code reviews, and Python/ML engineering "
        "standards, raising delivery speed and quality across the team.",
    ]:
        bullet(doc, item)

    heading(doc, "Working Style / Leadership")
    body(
        doc,
        "Play-and-coach full-stack data specialist: I ship production code while "
        "mentoring peers and bringing new ML and engineering patterns to the team. "
        "Having worked across multiple languages, full-stack, and in a leadership "
        "role is an advantage; I connect easily with people, enjoy looking at facts "
        "from different angles, and care about team atmosphere.",
    )

    heading(doc, "Education")
    body(doc, "Moscow State University | MS in Calculus Mathematics")

    doc.save(str(BASE / "CV_BASOVI.docx"))


# -------------------------------------------------------------- RESUME --------
def build_resume():
    doc = Document()
    add_name_header(doc)

    body(doc, f"Target Role: {POSITION}")

    heading(doc, "Profile")
    body(
        doc,
        "AI/ML engineering lead with ~8 years of focused experience in production "
        "AI/GenAI and data delivery. Strong in Python, machine learning, streaming "
        "data, and full-stack implementation on AWS/Azure/GCP, with a track record "
        "of measurable performance and quality improvements.",
    )

    heading(doc, "Relevant Hard Skills")
    for item in [
        "Python, machine learning, and AI/GenAI delivery",
        "LLM integration and ML model deployment to production",
        "Data engineering with Kafka, Spark, Airflow, and PostgreSQL",
        "Backend across Java/Scala and .NET/C#; Node.js services",
        "JavaScript/TypeScript and React full-stack implementation",
        "Cloud (AWS, Azure, GCP), Docker, CI/CD, and Linux",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Experience (Selected, ~8 years)")

    subhead(doc, "Sberbank | Lead Software Engineer / ML Platform Lead | 2020-2025")
    for item in [
        "- Led AI and platform initiatives, aligning business objectives with "
        "technical execution and ML deployment.",
        "- Guided the team on Python/ML engineering standards, code quality, and "
        "scalable platform design.",
    ]:
        bullet(doc, item)

    subhead(doc, "Upwork | Senior AI / Data Engineer | 2017-2020")
    for item in [
        "- Built real-time, streaming data and ML platforms on PostgreSQL, Kafka, "
        "Spark, and S3 (AWS), handling 300,000+ orders/day across business units.",
        "- Delivered ML-powered features end-to-end, from data and models to "
        "JavaScript/React UI; improved server response time by 30%.",
    ]:
        bullet(doc, item)

    heading(doc, "Vacancy Fit")
    for item in [
        "Deep Python and machine-learning expertise with production AI systems",
        "Comfortable across the full stack (Java/Scala, .NET/C#, Node, React)",
        "Strong data engineering: streaming, pipelines, cloud, observability",
        "Delivers ML solutions end-to-end with strong engineering discipline",
    ]:
        bullet(doc, "- " + item)

    doc.save(str(BASE / "RESUME_BASOVI.docx"))


# -------------------------------------------------------------- LETTER --------
def build_letter():
    doc = Document()
    add_name_header(doc)

    body(doc, f"Target Role: Application for {POSITION}")

    body(doc, "Dear Hiring Team,")

    body(
        doc,
        f"My name is Iurii Basov, and I am applying for the {POSITION} role. I am "
        "currently in active conversations for data-architect and tech-lead "
        "positions, and I was glad to connect through a specialist tech-recruitment "
        "team that places world-class engineers with leading companies.",
    )

    body(
        doc,
        "I bring more than 10 years in IT. I started as a Java/Scala developer, "
        "moved into ML and platform work, and was promoted at Sberbank to head an "
        "ML platform direction. My core hard skills map directly to the role: "
        + VACANCY_TECH + ".",
    )

    body(
        doc,
        "In recent roles I designed and shipped production AI/ML and data systems "
        "end-to-end: real-time, streaming platforms processing 300,000+ orders a "
        "day, ML models powering a customer chatbot (+18% engagement), and "
        "performance work that improved server response time by 30%. I have acted "
        "as a play-and-coach full-stack data specialist, delivering from data and "
        "models through to React interfaces.",
    )

    body(
        doc,
        "What attracts me is the chance to work with a strong network across "
        "Europe and to join a team that values quality and long-term relationships. "
        "Having worked across several languages, as a full-stack engineer, and in a "
        "leadership role is an advantage I bring; I connect easily with people, "
        "enjoy looking at facts from different angles, and care about team culture.",
    )

    body(
        doc,
        "Thank you for your consideration. I would welcome the opportunity to "
        "discuss how my AI/ML depth and full-stack range can help your team.",
    )

    body(doc, "Best regards,")
    tail = doc.add_paragraph()
    r = tail.add_run(
        f"{FULL_NAME}\n{EMAIL}\n{LINKEDIN}\nWhatsApp: {WHATSAPP} | {PROFILE}"
    )
    r.bold = True

    doc.save(str(BASE / "LETTER_BASOVI.docx"))


# ------------------------------------------------------------- WELCOME --------
def build_welcome():
    doc = Document()
    text = (
        "Day good. I was recommended to contact you. I like the company where you "
        "work, and I want to work with you. Could you please recommend me through HR "
        f"for the position {POSITION}, {COMPANY_GENERIC}, {LOCATION}? Thank you in "
        "advance. Here is the link to my cv - bit.ly/cv_basovi, link to my resume - "
        "bit.ly/resume_basovi, link to my cover letter - bit.ly/cover_letter."
    )
    doc.add_paragraph(text)
    doc.save(str(BASE / "WELCOME_BASOVI.docx"))


def main():
    build_cv()
    build_resume()
    build_letter()
    build_welcome()
    print("BUILT: CV_BASOVI.docx, RESUME_BASOVI.docx, LETTER_BASOVI.docx, WELCOME_BASOVI.docx")


if __name__ == "__main__":
    main()
