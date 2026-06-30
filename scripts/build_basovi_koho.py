"""Generate CV/RESUME/LETTER/WELCOME BASOVI docx tailored to the vacancy.

Vacancy: Senior Software Developer (Full-Stack), Canada (remote-first).
Rules (rule.txt + TIPS.md sections 11.x):
  - Company name and the vacancy REF id are excluded from every output file.
  - First paragraph carries a photo. Canada is in the Americas (not Germany / not
    USA) -> use tips/PHOTO.png.
  - CV: full CV; RESUME: condensed 2-3 roles ~8y; LETTER: cover letter from hint
    with "вставить" replaced by the vacancy hard skills; WELCOME: outreach note.
"""
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = Path(r"C:\Users\leto\Documents\GITLAB\excel")

# --- Personal identity (from rule.txt / hint) ---------------------------------
FIRST_NAME = "IURII"
LAST_NAME = "BASOV"
FULL_NAME = f"{FIRST_NAME} {LAST_NAME}"
EMAIL = "basov.yo@gmail.com"
LINKEDIN = "linkedin.com/in/basovi"
WHATSAPP = "+12518009809"
PROFILE = "x.com/topco"

# --- Vacancy facts (company name + REF id intentionally NOT used anywhere) -----
POSITION = "Senior Software Developer (Full-Stack)"
LOCATION = "Canada"
COMPANY_GENERIC = "a Canadian fintech and financial services company"

# Photo selection: Canada -> Americas (not Germany / not USA) -> PHOTO.png
PHOTO = BASE / "tips" / "PHOTO.png"

# Suitable technologies pulled from the job description ("вставить" target).
VACANCY_TECH = (
    "Go (Golang), PostgreSQL, DynamoDB, AWS, RabbitMQ, event-driven architecture, "
    "distributed systems, caching, observability, REST API design, database schema "
    "design, React, Angular, Ionic, TypeScript, JavaScript, HTML/CSS"
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
    line(f"Location: {LOCATION} (remote, open to relocation) | Need Visa Sponsorship")


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
        "Senior backend-focused full-stack engineer with 10+ years building and "
        "owning production systems end-to-end. Deep expertise designing scalable "
        "services in Go on top of PostgreSQL and DynamoDB, with event-driven "
        "architectures (RabbitMQ) and high-throughput data pipelines. Proven track "
        "record running resilient, observable services on AWS that perform under "
        "load. Comfortable across the full stack, shipping React and Angular/Ionic "
        "interfaces from database schema to UI without handoffs. A collaborative, "
        "growth-minded play-and-coach lead who values strong team culture and the "
        "people behind the product.",
    )

    heading(doc, "Core Technology Stack")
    for item in [
        "Backend services in Go (Golang); scalable, production-owned systems",
        "PostgreSQL and DynamoDB; relational + NoSQL data modeling and schema design",
        "Event-driven architecture and messaging with RabbitMQ and Kafka",
        "Distributed systems: caching, observability, resilient and monitored services",
        "AWS cloud (S3, managed services) and infrastructure for systems at scale",
        "REST API design and end-to-end feature ownership (DB -> API -> UI)",
        "Frontend: React, Angular, Ionic, TypeScript, JavaScript, HTML/CSS",
        "CI/CD, automated testing, and maintainable software engineering practices",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Relevant Experience")

    subhead(doc, "Upwork | Senior Backend / Full-Stack Engineer | 2013-2025")
    for item in [
        "- Designed and operated resilient cloud data-processing platforms with "
        "real-time and streaming pipelines, integrating data across 5 business "
        "units and supporting e-commerce/logistics processing 300,000+ orders/day "
        "using PostgreSQL, Apache Spark, S3, and Kafka.",
        "- Built an online credit risk scoring system on an event-driven stack "
        "(Apache NiFi, Kafka, Hadoop) enabling real-time processing; reduced data "
        "processing latency by 5% and improved model accuracy by 3%.",
        "- Engineered a high-performance Demand-Side Platform server and real-time "
        "stats system, improving server response time by 30% and supporting a 50% "
        "increase in concurrent users with no performance degradation.",
        "- Owned features end-to-end from database schema and API development to "
        "the corresponding UI, eliminating handoffs and shipping complete solutions.",
    ]:
        bullet(doc, item)

    subhead(doc, "Sberbank | Lead Software Engineer / Platform Lead | 2020-2025")
    for item in [
        "- Led engineering teams and technical tracks for platform modernization, "
        "introducing event-driven patterns, caching, and observability to make "
        "services more resilient and monitored.",
        "- Provided architecture guidance, code reviews, and Go/service-design "
        "patterns across the team, raising delivery speed and engineering quality.",
    ]:
        bullet(doc, item)

    heading(doc, "Working Style / Leadership")
    body(
        doc,
        "Play-and-coach full-stack engineer: I ship production code while mentoring "
        "peers, bringing new patterns to the team across both backend (Go service "
        "architecture) and frontend (modern React). I care about team atmosphere and "
        "the people I work with, and actively seek opportunities to work outside my "
        "comfort zone while helping others grow their full-stack skills.",
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
        "Backend-focused full-stack engineer with ~8 years building production "
        "systems in Go on PostgreSQL and DynamoDB, event-driven architectures with "
        "RabbitMQ, and AWS-hosted distributed services. Owns features end-to-end "
        "from schema to React/Angular UI.",
    )

    heading(doc, "Relevant Hard Skills")
    for item in [
        "Go (Golang) backend services, production-owned and scalable",
        "PostgreSQL and DynamoDB data modeling and schema design",
        "Event-driven architecture with RabbitMQ; caching and observability",
        "AWS cloud and resilient distributed systems",
        "REST API design and end-to-end feature delivery",
        "React, Angular/Ionic, TypeScript, JavaScript, HTML/CSS",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Experience (Selected, ~8 years)")

    subhead(doc, "Sberbank | Lead Software Engineer / Platform Lead | 2020-2025")
    for item in [
        "- Led platform modernization with event-driven patterns, caching, and "
        "observability for resilient, monitored services.",
        "- Guided team on Go service architecture, code quality, and scalable "
        "backend design.",
    ]:
        bullet(doc, item)

    subhead(doc, "Upwork | Senior Backend / Full-Stack Engineer | 2017-2020")
    for item in [
        "- Built real-time, streaming data platforms on PostgreSQL, Kafka, and S3 "
        "(AWS), handling 300,000+ orders/day across multiple business units.",
        "- Delivered features end-to-end from database schema and APIs to React/"
        "Angular UI; improved server response time by 30%.",
    ]:
        bullet(doc, item)

    heading(doc, "Vacancy Fit")
    for item in [
        "Deep backend expertise (Go, PostgreSQL, AWS) with proven systems at scale",
        "Comfortable across the full stack and eager to extend React/Angular work",
        "Strong with distributed-systems concepts: event-driven, caching, observability",
        "Owns complete features (DB -> API -> UI) with no handoffs",
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
        "currently in active conversations for senior backend and tech-lead "
        "positions, and I was genuinely drawn to a team breaking down the barriers "
        "between frontend and backend to ship complete features faster.",
    )

    body(
        doc,
        "I bring more than 10 years in IT. I started as a Java/Scala developer, "
        "moved into platform engineering, and grew into a leadership role heading a "
        "platform direction. My core hard skills map directly to your stack: "
        + VACANCY_TECH + ".",
    )

    body(
        doc,
        "In recent roles I designed and owned scalable backend services end-to-end, "
        "built event-driven, real-time data platforms processing 300,000+ orders a "
        "day, and shipped resilient, observable systems on AWS. I have worked as a "
        "play-and-coach full-stack engineer, owning features from database schema "
        "through API to React and Angular UI, with measurable results such as a 30% "
        "improvement in server response time.",
    )

    body(
        doc,
        "What attracts me to your company is the autonomy to build complete "
        "features and the culture of trust and ownership. For me, team atmosphere "
        "and the people I work with matter as much as the technology; I enjoy "
        "exchanging ideas, looking at facts from different angles, and helping "
        "teammates grow their full-stack skills.",
    )

    body(
        doc,
        "Thank you for your consideration. I would welcome the opportunity to "
        "discuss how my backend depth and full-stack range can help your team ship "
        "faster.",
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
