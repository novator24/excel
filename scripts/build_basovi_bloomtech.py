"""Generate CV/RESUME/LETTER/WELCOME BASOVI docx tailored to the vacancy.

Vacancy: Backend Engineer (Fully Remote), Tokyo, Japan (Real Estate AI x SaaS).
Rules (rule.txt + TIPS.md sections 11.x):
  - Company name and the vacancy REF id are excluded from every output file.
  - First paragraph carries a photo. Japan is in Asia (not Germany / not USA)
    -> use tips/PHOTO.png.
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

# --- Vacancy facts (company name + REF id intentionally NOT used anywhere) -----
POSITION = "Backend Engineer (Fully Remote)"
LOCATION = "Tokyo, Japan"
COMPANY_GENERIC = "a Japan-based real estate AI and SaaS company"

# Photo selection: Japan -> Asia (not Germany / not USA) -> PHOTO.png
PHOTO = BASE / "tips" / "PHOTO.png"

# Suitable technologies pulled from the job description ("вставить" target).
VACANCY_TECH = (
    "Ruby, Ruby on Rails, Node.js (TypeScript), AWS (Aurora, ECS, Lambda, Step "
    "Functions), Terraform, RDBMS database design and query optimization, "
    "multi-tenant SaaS, Generative AI / LLM integration, TypeScript, React, GitHub"
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
    line(f"Location: {LOCATION} (fully remote, open to relocation) | Need Visa Sponsorship")


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
        "Backend engineer and tech lead with 10+ years building and operating "
        "production web services and data platforms. Strong in efficient RDBMS "
        "database design and query optimization, scalable multi-tenant "
        "architectures, and AWS infrastructure. Started as a Java/Scala developer, "
        "moved into ML/platform work, and grew into a leadership role. Comfortable "
        "with Node.js/TypeScript services and React frontends, large-scale data "
        "migration and performance tuning, and integrating Generative AI (LLMs) "
        "into production. A collaborative play-and-coach engineer who partners "
        "closely with PMs and cross-functional teams to resolve specification "
        "ambiguity and ship the right product.",
    )

    heading(doc, "Core Technology Stack")
    for item in [
        "Backend web services and operations (10+ years), API and product engineering",
        "Ruby on Rails-style MVC backends; Node.js (TypeScript) services",
        "RDBMS database design and query optimization (PostgreSQL, Aurora-compatible)",
        "AWS infrastructure: Aurora, ECS, Lambda, Step Functions; IaC with Terraform",
        "Multi-tenant SaaS scalability, large-scale data migration, performance tuning",
        "Generative AI / LLM integration into production applications",
        "Frontend with TypeScript and React; full-stack feature delivery",
        "GitHub, CI/CD, code review culture, and maintainable engineering practices",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Relevant Experience")

    subhead(doc, "Upwork | Senior Backend Engineer / Tech Lead | 2013-2025")
    for item in [
        "- Designed efficient RDBMS schemas and optimized queries for cloud data "
        "platforms with real-time and streaming pipelines, supporting e-commerce/"
        "logistics processing 300,000+ orders/day on PostgreSQL, Spark, S3, Kafka.",
        "- Led large-scale data migration and performance tuning: improved server "
        "response time by 30%, reduced data processing latency by 5%, and supported "
        "a 50% increase in concurrent users with no performance degradation.",
        "- Integrated ML/LLM models into a customer chatbot, increasing engagement "
        "by 18%, and delivered features end-to-end with Node.js/TypeScript and "
        "React on AWS.",
        "- Partnered with cross-functional stakeholders (PM, business, ops) to "
        "resolve specification ambiguity and drive development forward.",
    ]:
        bullet(doc, item)

    subhead(doc, "Sberbank | Lead Software Engineer / Tech Lead | 2020-2025")
    for item in [
        "- Led engineering teams and technical tracks for platform modernization, "
        "owning architecture, DB design decisions, and code reviews.",
        "- Set backend engineering standards and mentored engineers, raising "
        "delivery speed and quality across the team.",
    ]:
        bullet(doc, item)

    heading(doc, "Working Style / Leadership")
    body(
        doc,
        "Play-and-coach full-stack engineer: I ship production code while mentoring "
        "peers and collaborating as an equal partner with frontend engineers and "
        "product managers. Having worked across multiple languages, full-stack, and "
        "in a leadership role is an advantage; I connect easily with people and care "
        "about team atmosphere.",
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
        "Backend engineer and tech lead with ~8 years of focused experience in "
        "production web services, RDBMS design and query optimization, and AWS-"
        "hosted scalable systems. Comfortable with Node.js/TypeScript and React, "
        "large-scale data migration, performance tuning, and LLM integration.",
    )

    heading(doc, "Relevant Hard Skills")
    for item in [
        "Backend development and operations (web services, APIs)",
        "RDBMS database design and query optimization (PostgreSQL/Aurora)",
        "Node.js (TypeScript) services; Ruby on Rails-style MVC backends",
        "AWS (Aurora, ECS, Lambda, Step Functions) and Terraform IaC",
        "Large-scale data migration, performance tuning, multi-tenant SaaS",
        "Generative AI / LLM integration; TypeScript and React frontend",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Experience (Selected, ~8 years)")

    subhead(doc, "Sberbank | Lead Software Engineer / Tech Lead | 2020-2025")
    for item in [
        "- Led backend platform modernization, owning architecture and DB design "
        "decisions, with code reviews and engineering standards.",
        "- Mentored engineers and aligned technical execution with business goals.",
    ]:
        bullet(doc, item)

    subhead(doc, "Upwork | Senior Backend Engineer | 2017-2020")
    for item in [
        "- Built and optimized RDBMS-backed services and streaming data platforms "
        "on PostgreSQL, Kafka, and AWS (S3), handling 300,000+ orders/day.",
        "- Delivered features end-to-end with Node.js/TypeScript and React; "
        "improved server response time by 30% through performance tuning.",
    ]:
        bullet(doc, item)

    heading(doc, "Vacancy Fit")
    for item in [
        "4+ years backend web development and operations (10+ in total)",
        "Efficient RDBMS database design and query optimization",
        "AWS infrastructure experience and large-scale data/performance work",
        "Tech-lead experience, LLM integration, and TypeScript/React knowledge",
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
        "currently in active conversations for backend, data-architect, and "
        "tech-lead positions, and I was drawn to a high-growth Real Estate AI x "
        "SaaS team that gives engineers real autonomy over technology selection "
        "and database design.",
    )

    body(
        doc,
        "I bring more than 10 years in IT. I started as a Java/Scala developer, "
        "moved into ML and platform work, and grew into a leadership role. My core "
        "hard skills map directly to your stack: " + VACANCY_TECH + ".",
    )

    body(
        doc,
        "In recent roles I designed efficient RDBMS schemas and optimized queries "
        "for systems processing 300,000+ orders a day, led large-scale data "
        "migration and performance tuning (30% faster server response), and "
        "integrated ML/LLM models into a production chatbot (+18% engagement). I "
        "have worked as a play-and-coach engineer, partnering with PMs and "
        "frontend engineers to define specs and ship end-to-end on AWS.",
    )

    body(
        doc,
        "What attracts me is the chance to architect systems that simplify a "
        "complex domain, with strong investment in technology and a refactoring-"
        "first culture. For me, team atmosphere and the people I work with matter "
        "as much as the technology; I connect easily and enjoy looking at facts "
        "from different angles.",
    )

    body(
        doc,
        "Thank you for your consideration. I would welcome the opportunity to "
        "discuss how my backend depth and full-stack range can help your team.",
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
