"""Generate CV/RESUME/LETTER/WELCOME BASOVI docx tailored to the vacancy.

Vacancy: Accelerator Program - Backend Engineer (Java), Risk, Hong Kong SAR.
Rules (rule.txt + TIPS.md sections 11.x):
  - Company name and the vacancy REF id are excluded from every output file.
  - First paragraph carries a photo. Hong Kong is in Asia (not Germany / not USA)
    -> use tips/PHOTO.png.
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

POSITION = "Backend Engineer (Java), Risk"
LOCATION = "Hong Kong, Hong Kong SAR"
COMPANY_GENERIC = "a leading global blockchain and digital-asset exchange"

PHOTO = BASE / "tips" / "PHOTO.png"

VACANCY_TECH = (
    "Java (multithreading, concurrency, JVM, networking), Spring / Spring Cloud "
    "microservices, MySQL, Redis, RabbitMQ, Kafka, real-time risk control and "
    "decisioning services, fraud detection, AML, account security, big data, "
    "AI/ML applied to security, risk rules, scoring models, and feature pipelines"
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
        "Backend engineer and tech lead with 10+ years in IT, specializing in Java/Scala "
        "services, real-time data platforms, and risk-oriented systems. Strong foundation "
        "in multithreading, concurrency, JVM, and networking, with hands-on experience in "
        "Spring-style microservices, MySQL/PostgreSQL, Redis, RabbitMQ, and Kafka. Built "
        "an online credit risk scoring system with real-time pipelines and ML models, and "
        "led platform work as Head of an ML platform direction at Sberbank. Comfortable "
        "with fraud/risk workflows, big data, and AI/ML applied to security scenarios. "
        "A play-and-coach engineer who values team atmosphere and clear collaboration.",
    )

    heading(doc, "Core Technology Stack")
    for item in [
        "Java / Scala backend (multithreading, concurrency, JVM, networking)",
        "Spring / Spring Cloud microservices and service-oriented architecture",
        "MySQL, PostgreSQL, Redis, RabbitMQ, Kafka",
        "Real-time risk control, scoring models, and feature pipelines",
        "Fraud detection, AML, account security, and transaction monitoring patterns",
        "Big data: Apache Spark, Airflow, NiFi, Hadoop, S3",
        "AI/ML applied to risk and security scenarios; MLOps",
        "Technical documentation, troubleshooting, QA collaboration, system stability",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Relevant Experience")

    subhead(doc, "Upwork | Senior Backend / Risk Data Engineer | 2013-2025")
    for item in [
        "- Developed an online credit risk scoring system using Apache NiFi, Kafka, and "
        "Hadoop, enabling real-time risk assessment workflows and improving credit scoring "
        "accuracy and efficiency.",
        "- Designed resilient cloud data platform architectures with real-time and streaming "
        "pipelines processing 300,000+ records/day on PostgreSQL, Spark, S3, and Kafka.",
        "- Deployed ML models for risk-related customer interactions (+18% chatbot engagement); "
        "reduced data processing latency by 5% and improved server response time by 30%.",
        "- Prepared technical documentation and collaborated with QA to resolve issues and "
        "maintain system stability.",
    ]:
        bullet(doc, item)

    subhead(doc, "Sberbank | Head of ML Platform / Lead Software Engineer | 2020-2025")
    for item in [
        "- Promoted to Head of the ML platform direction; owned architecture for scalable "
        "backend and data services with strong engineering standards and code review.",
        "- Led engineers as a playing coach; mentored, hired, and levelled up the team.",
    ]:
        bullet(doc, item)

    heading(doc, "Working Style / Leadership")
    body(
        doc,
        "Playing coach and full-stack data specialist. Experience across multiple languages, "
        "full-stack delivery, and leadership is my advantage. I connect easily, communicate "
        "clearly, and care about team atmosphere and the people I work with.",
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
        "Backend engineer with ~8 years building Java-oriented services, real-time risk "
        "pipelines, and data platforms. Strong in Spring-style microservices, MySQL/PostgreSQL, "
        "Redis, RabbitMQ, Kafka, and AI/ML for risk and security scenarios.",
    )

    heading(doc, "Relevant Hard Skills")
    for item in [
        "Java backend (multithreading, concurrency, JVM, networking)",
        "Spring / Spring Cloud microservices",
        "MySQL, Redis, RabbitMQ, Kafka",
        "Real-time risk rules, scoring models, and feature pipelines",
        "Fraud detection, AML, big data, and AI/ML for security",
        "Technical documentation, troubleshooting, and system stability",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Experience (Selected, ~8 years)")

    subhead(doc, "Sberbank | Head of ML Platform / Lead Software Engineer | 2020-2025")
    for item in [
        "- Owned backend and platform architecture; set engineering standards, code review, "
        "and monitoring practices.",
        "- Led engineers as a playing coach; mentored and grew the team.",
    ]:
        bullet(doc, item)

    subhead(doc, "Upwork | Senior Backend / Risk Data Engineer | 2017-2020")
    for item in [
        "- Built an online credit risk scoring system with Kafka, NiFi, and Hadoop for "
        "real-time risk assessment workflows.",
        "- Designed data platforms on PostgreSQL, Kafka, and Spark processing 300,000+ "
        "records/day; improved server response time by 30%.",
    ]:
        bullet(doc, item)

    heading(doc, "Vacancy Fit")
    for item in [
        "Solid Java foundation with microservices and middleware experience",
        "Hands-on risk scoring, fraud/AML-oriented data pipelines, and big data",
        "Kafka, Redis, RabbitMQ, MySQL; AI/ML interest applied to security",
        "Strong logical thinking, teamwork, learning ability, and play-and-coach style",
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
        f"My name is Iurii Basov, and I am applying for the {POSITION} role. I am "
        "currently in active conversations for data-architect and tech-lead positions, "
        "and I was excited by a real-time risk control team that protects users at scale "
        "with high-throughput, low-latency decisioning.",
    )

    body(
        doc,
        "I bring more than 10 years in IT. I started as a Java/Scala developer, moved into "
        "ML and platform work, and was promoted to Head of an ML platform direction at "
        "Sberbank. My core hard skills map directly to your stack: " + VACANCY_TECH + ".",
    )

    body(
        doc,
        "In recent roles I built an online credit risk scoring system with real-time Kafka "
        "pipelines, designed data platforms processing 300,000+ records/day, deployed ML "
        "models into production (+18% engagement), and improved server response time by 30%. "
        "I write and maintain technical documentation, troubleshoot issues with QA, and "
        "collaborate to keep systems stable.",
    )

    body(
        doc,
        "What attracts me is tackling fraud detection, AML, and account security at scale "
        "with rule engines, big data, and AI/ML. Having worked across several languages, "
        "as a full-stack specialist, and in a leadership role is my advantage. For me, team "
        "atmosphere and the people I work with matter; I connect easily and enjoy looking "
        "at facts from different angles.",
    )

    body(
        doc,
        "Thank you for your consideration. I would welcome the opportunity to discuss how "
        "my Java backend depth and risk-platform experience can contribute to your team.",
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
