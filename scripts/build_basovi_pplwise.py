"""Generate CV/RESUME/LETTER/WELCOME BASOVI docx tailored to the vacancy.

Vacancy: AI Software Engineer (m/f/d), Vienna, Austria (Legal-tech B2B SaaS).
Rules (rule.txt + TIPS.md sections 11.x):
  - Company names (hiring agency + customer) and the vacancy REF id are excluded
    from every output file.
  - First paragraph carries a photo. Austria is in Europe (not Germany / not USA)
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

# --- Vacancy facts (company names + REF id intentionally NOT used anywhere) ----
POSITION = "AI Software Engineer (m/f/d)"
LOCATION = "Vienna, Austria"
COMPANY_GENERIC = "a Vienna-based Legal-tech B2B SaaS company"

# Photo selection: Austria -> Europe (not Germany / not USA) -> PHOTO.png
PHOTO = BASE / "tips" / "PHOTO.png"

# Suitable technologies pulled from the job description ("вставить" target).
VACANCY_TECH = (
    "C#/.NET, Node.js, PostgreSQL, MongoDB, RabbitMQ, React/TypeScript, AI/LLM "
    "pipelines (classification, clustering), data-heavy systems, crawlers and "
    "APIs, system design and architecture, testing and monitoring"
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
    line(f"Location: {LOCATION} (remote within Austria, open to relocation) | Need Visa Sponsorship")


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
        "AI-first backend engineer with 10+ years owning and evolving backend "
        "services, AI pipelines, and data-heavy infrastructure. Strong system "
        "design and architecture for scale, speed, and reliability, with hands-on "
        "experience turning messy, real-world data into structured insights using "
        "LLMs, classification, and clustering. Started as a Java/Scala developer, "
        "moved into ML/platform work, and grew into a leadership role. Comfortable "
        "with .NET and Node.js service layers, PostgreSQL/MongoDB, and messaging, "
        "plus React/TypeScript. An ownership-minded, clear communicator who thrives "
        "in startup/scale-up environments and works closely with founders.",
    )

    heading(doc, "Core Technology Stack")
    for item in [
        "Backend services (crawlers, APIs, AI services); ownership end-to-end",
        "C#/.NET and Node.js service layers",
        "AI/LLM pipelines: classification, clustering, GenAI integration",
        "Data-heavy systems and turning raw data into structured insights",
        "PostgreSQL, MongoDB, and messaging systems (RabbitMQ, Kafka)",
        "System design and architecture for scale, speed, and reliability",
        "React/TypeScript for full-stack delivery",
        "Code quality, testing, and monitoring standards",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Relevant Experience")

    subhead(doc, "Upwork | Senior Backend / AI Engineer | 2013-2025")
    for item in [
        "- Owned and evolved backend services and data pipelines, designing systems "
        "for scale, speed, and reliability across data-heavy platforms processing "
        "300,000+ records/day on PostgreSQL, Kafka, Spark, and S3.",
        "- Built AI/LLM pipelines and deployed ML models powering a customer "
        "chatbot (+18% engagement), turning messy real-world data into structured "
        "insights.",
        "- Improved code quality, testing, and monitoring; cut server response time "
        "by 30% and data processing latency by 5% through architecture and tuning.",
        "- Worked closely with stakeholders and founders to identify quick wins, "
        "ship weekly, and own core parts of the architecture.",
    ]:
        bullet(doc, item)

    subhead(doc, "Sberbank | Lead Software Engineer / ML Platform Lead | 2020-2025")
    for item in [
        "- Drove backend and AI decisions, owning system design and defining how "
        "the platform scales, with code review and engineering standards.",
        "- Mentored engineers and helped hire and level up the team.",
    ]:
        bullet(doc, item)

    heading(doc, "Working Style / Leadership")
    body(
        doc,
        "Ownership mindset from day one: I take real responsibility for the systems "
        "I build, make pragmatic decisions, and communicate clearly. I enjoy "
        "shaping technical direction with founders and product, and I care about "
        "team atmosphere and the people I work with.",
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
        "AI-first backend engineer with ~8 years owning backend services, AI/LLM "
        "pipelines, and data-heavy systems. Strong system design across .NET and "
        "Node.js with PostgreSQL, MongoDB, and messaging, plus React/TypeScript. "
        "Ownership mindset and startup/scale-up experience.",
    )

    heading(doc, "Relevant Hard Skills")
    for item in [
        "Backend services (APIs, crawlers, AI services) with C#/.NET and Node.js",
        "AI/LLM pipelines: classification, clustering, GenAI integration",
        "Data-heavy systems; structured insights from messy data",
        "PostgreSQL, MongoDB, and messaging (RabbitMQ, Kafka)",
        "System design and architecture for scale, speed, reliability",
        "React/TypeScript; testing and monitoring standards",
    ]:
        bullet(doc, "- " + item)

    heading(doc, "Experience (Selected, ~8 years)")

    subhead(doc, "Sberbank | Lead Software Engineer / ML Platform Lead | 2020-2025")
    for item in [
        "- Drove backend and AI architecture decisions, defining how the platform "
        "scales; owned code review and engineering standards.",
        "- Mentored engineers and helped grow the team.",
    ]:
        bullet(doc, item)

    subhead(doc, "Upwork | Senior Backend / AI Engineer | 2017-2020")
    for item in [
        "- Owned backend services and data pipelines on PostgreSQL, Kafka, and AWS, "
        "designing for scale across data-heavy systems (300,000+ records/day).",
        "- Built AI/LLM features and React/TypeScript UI; improved server response "
        "time by 30% with strong testing and monitoring.",
    ]:
        bullet(doc, item)

    heading(doc, "Vacancy Fit")
    for item in [
        "Strong backend experience (C#/.NET-friendly) and Node.js service layer",
        "Hands-on AI/LLMs/data pipelines with data-heavy systems",
        "Solid system design; PostgreSQL, MongoDB, and messaging systems",
        "Ownership mindset, clear communicator, startup/scale-up experience",
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
        "positions, and I was excited by an AI-first role with real ownership where "
        "I can shape how AI systems, data pipelines, and infrastructure evolve.",
    )

    body(
        doc,
        "I bring more than 10 years in IT. I started as a Java/Scala developer, "
        "moved into ML and platform work, and grew into a leadership role. My core "
        "hard skills map directly to your stack: " + VACANCY_TECH + ".",
    )

    body(
        doc,
        "In recent roles I owned and evolved backend services and AI pipelines, "
        "designed data-heavy systems for scale and reliability, deployed LLM/ML "
        "models into a production chatbot (+18% engagement), and turned messy "
        "real-world data into structured insights. I improved code quality, "
        "testing, and monitoring, and cut server response time by 30%.",
    )

    body(
        doc,
        "What attracts me is the chance to take real ownership from day one, work "
        "directly with founders in a flat hierarchy, and drive both AI and backend "
        "decisions. For me, team atmosphere and the people I work with matter as "
        "much as the technology; I communicate clearly and enjoy looking at facts "
        "from different angles.",
    )

    body(
        doc,
        "Thank you for your consideration. I would welcome the opportunity to "
        "discuss how my backend depth and AI experience can help scale your product.",
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
