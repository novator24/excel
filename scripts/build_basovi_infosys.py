"""Generate CV/RESUME/LETTER/WELCOME BASOVI docx tailored to the vacancy.

Vacancy: Big Data Architect, Milpitas, CA, USA.
Rules (rule.txt + TIPS.md sections 11.x):
  - Company name and the vacancy REF id are excluded from every output file.
  - USA -> use tips/NOPHOTO.png.
"""
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor

BASE = Path(r"C:\Users\leto\Documents\GITLAB\excel")

FIRST_NAME = "IURII"
LAST_NAME = "BASOV"
FULL_NAME = f"{FIRST_NAME} {LAST_NAME}"
EMAIL = "basov.yo@gmail.com"
LINKEDIN = "linkedin.com/in/basovi"
WHATSAPP = "+12518009809"
PROFILE = "x.com/topco"

POSITION = "Big Data Architect"
LOCATION = "Milpitas, CA, USA"
COMPANY_GENERIC = "a global IT services and digital consulting firm"

PHOTO = BASE / "tips" / "NOPHOTO.png"

VACANCY_TECH = (
    "Apache Spark, Kafka, SQL, Hadoop, Trino, Pinot, Iceberg; scalable ETL/ELT "
    "pipelines (batch and real-time); large-scale distributed data platforms; "
    "AWS (S3, EC2, Glue, IAM); high-performance data architecture; AI/ML and "
    "predictive analytics; integration strategies, PoC validation, and deployment automation"
)


def add_name_header(doc):
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


def body(doc, text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(2)


def bullet(doc, text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(1)


def subhead(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(1)


def build_cv():
    doc = Document()
    add_name_header(doc)
    body(doc, f"Target Role: {POSITION}")

    heading(doc, "Professional Summary")
    body(
        doc,
        "Big data architect and tech lead with 10+ years designing scalable, secure, and "
        "high-performance data architectures across cloud and distributed platforms. Strong in "
        "batch and real-time ETL/ELT pipelines on Spark, Kafka, SQL, Hadoop, and AWS (S3, EC2, "
        "Glue). Started as a Java/Scala developer, moved into ML and platform engineering, and "
        "grew into Head of an ML platform direction at Sberbank. I analyze requirements for "
        "performance, security, and scalability; compare technology options; validate PoCs; and "
        "collaborate with development teams through build, deployment, and support. A playing-coach "
        "architect who values team atmosphere and clear client alignment.",
    )

    heading(doc, "Core Technology Stack")
    for item in [
        "Large-scale distributed data platforms: Hadoop, Spark, Trino, Pinot, Iceberg",
        "Scalable ETL/ELT pipelines (batch and real-time): Spark, Kafka, Airflow, NiFi",
        "SQL, PostgreSQL, and data modeling for high-volume workloads",
        "AWS cloud data architecture: S3, EC2, Glue, IAM",
        "High-performance, reliable, and scalable data architecture design",
        "AI/ML and predictive analytics integration into data platforms",
        "Integration strategies, PoC validation, deployment automation, and knowledge transfer",
        "Performance analysis, risk identification, and architectural documentation",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Relevant Experience")

    subhead(doc, "Upwork | Lead Data Engineer / Big Data Architect | 2013-2025")
    for item in [
        "- Designed resilient cloud-based data platform architectures with batch and real-time "
        "streaming pipelines processing 300,000+ records/day on Spark, Kafka, PostgreSQL, S3, "
        "and Airflow across 5 business units.",
        "- Built large-scale ETL/ELT flows with Apache NiFi, Kafka, and Hadoop for credit risk "
        "scoring; reduced data processing latency by 5% and improved model accuracy by 3%.",
        "- Led a team of 3 data engineers and service providers; created technical documentation "
        "and supported deployment, troubleshooting, and system stability.",
        "- Integrated AI/ML models into production pipelines (+18% chatbot engagement); improved "
        "server response time by 30% through architecture and performance tuning.",
    ]:
        bullet(doc, item)

    subhead(doc, "Sberbank | Head of ML Platform / Lead Software Engineer | 2020-2025")
    for item in [
        "- Promoted to Head of the ML platform direction; owned enterprise data and system "
        "architecture, technology selection, and engineering standards.",
        "- Drove solution architecture, code review, and knowledge transfer; mentored engineers "
        "as a playing coach.",
    ]:
        bullet(doc, item)

    heading(doc, "Working Style / Leadership")
    body(
        doc,
        "Playing coach and full-stack data specialist. I compare technologies against business "
        "requirements, document architectural frameworks, and ensure smooth transitions through "
        "knowledge transfer. Experience across multiple languages, full-stack delivery, and "
        "leadership is my advantage; I connect easily and care about team atmosphere.",
    )

    heading(doc, "Core Stack (vacancy keywords)")
    body(doc, VACANCY_TECH)

    heading(doc, "Education")
    body(doc, "Moscow State University | MS in Calculus Mathematics")

    doc.save(str(BASE / "CV_BASOVI.docx"))


def build_resume():
    doc = Document()
    add_name_header(doc)
    body(doc, f"Target Role: {POSITION}")

    heading(doc, "Profile")
    body(
        doc,
        "Big data architect with ~8 years designing scalable ETL/ELT pipelines and distributed "
        "data platforms on Spark, Kafka, Hadoop, SQL, and AWS (S3, Glue). Strong in high-volume "
        "architecture, performance tuning, and AI/ML integration. Leadership and playing-coach "
        "experience.",
    )

    heading(doc, "Relevant Hard Skills")
    for item in [
        "Spark, Kafka, SQL, Hadoop, Trino-class distributed data platforms",
        "Scalable batch and real-time ETL/ELT pipelines",
        "AWS (S3, EC2, Glue, IAM) and cloud data architecture",
        "High-performance, reliable, scalable data architecture design",
        "AI/ML and predictive analytics on data platforms",
        "PoC validation, deployment automation, architectural documentation",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Experience (Selected, ~8 years)")

    subhead(doc, "Sberbank | Head of ML Platform / Lead Software Engineer | 2020-2025")
    for item in [
        "- Owned enterprise data architecture and technology selection; set engineering "
        "standards and drove solution design.",
        "- Led engineers as a playing coach; mentored and grew the team.",
    ]:
        bullet(doc, item)

    subhead(doc, "Upwork | Lead Data Engineer / Big Data Architect | 2017-2020")
    for item in [
        "- Designed Spark/Kafka data platforms on AWS (S3) processing 300,000+ records/day "
        "with batch and real-time ETL/ELT pipelines.",
        "- Built Hadoop/NiFi risk scoring pipelines; improved server response time by 30% and "
        "maintained technical documentation and deployment stability.",
    ]:
        bullet(doc, item)

    heading(doc, "Vacancy Fit")
    for item in [
        "Proven big data architecture across Spark, Kafka, SQL, and Hadoop",
        "Large-scale distributed platforms and AWS cloud data design",
        "ETL/ELT (batch + real-time), PoC validation, and deployment automation",
        "AI/ML integration; strong communication and playing-coach leadership",
    ]:
        bullet(doc, "- " + item)

    doc.save(str(BASE / "RESUME_BASOVI.docx"))


def build_letter():
    doc = Document()
    add_name_header(doc)
    body(doc, f"Target Role: Application for {POSITION}")

    body(doc, "Dear Hiring Team,")

    body(
        doc,
        f"My name is Iurii Basov, and I am applying for the {POSITION} role. I am currently in "
        "active conversations for data-architect and tech-lead positions, and I was drawn to a "
        "data-first engineering team that uses AI, ML, and predictive analytics to drive scalable "
        "architectures and continuous improvement.",
    )

    body(
        doc,
        "I bring more than 10 years in IT. I started as a Java/Scala developer, moved into ML and "
        "platform work, and was promoted to Head of an ML platform direction at Sberbank. My core "
        "hard skills map directly to your stack: " + VACANCY_TECH + ".",
    )

    body(
        doc,
        "In recent roles I designed distributed data platforms with batch and real-time pipelines "
        "processing 300,000+ records/day on Spark, Kafka, and AWS; validated architectural PoCs; "
        "created technical documentation; and collaborated with development teams through build, "
        "deployment, and support. I improved server response time by 30% and integrated AI/ML "
        "models into production (+18% engagement).",
    )

    body(
        doc,
        "What attracts me is analyzing requirements for performance, security, and scalability, "
        "recommending optimal architectural solutions, and ensuring knowledge transfer with quality "
        "standards. Having worked across several languages, as a full-stack specialist, and in a "
        "leadership role is my advantage. For me, team atmosphere and the people I work with matter; "
        "I connect easily and enjoy looking at facts from different angles.",
    )

    body(
        doc,
        "Thank you for your consideration. I would welcome the opportunity to discuss how my big "
        "data architecture experience can support your clients and engineering teams.",
    )

    body(doc, "Best regards,")
    tail = doc.add_paragraph()
    r = tail.add_run(
        f"{FULL_NAME}\n{EMAIL}\n{LINKEDIN}\nWhatsApp: {WHATSAPP} | {PROFILE}"
    )
    r.bold = True

    doc.save(str(BASE / "LETTER_BASOVI.docx"))


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
