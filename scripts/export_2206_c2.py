from pathlib import Path
import re
import sys

from docx import Document


BASE = Path(r"C:\Users\leto\Documents\GITLAB\excel")
OUT_DIR = BASE / "test" / "2206"
TMP_DIR = OUT_DIR / "_tmp"


def split_sentences(text: str):
    return [m.group(0) for m in re.finditer(r"[^.!?]+[.!?]|[^.!?]+$", text) if m.group(0).strip()]


def lower_first_alpha(text: str) -> str:
    chars = list(text)
    for i, ch in enumerate(chars):
        if ch.isalpha():
            chars[i] = ch.lower()
            break
    return "".join(chars)


def bump_plus_pattern(text: str) -> str:
    # Example: "10+ years" -> "13 years", "2+ months" -> "5 months"
    return re.sub(r"(\d+)\+\s", lambda m: f"{int(m.group(1)) + 3} ", text)


def paragraph_has_image(paragraph) -> bool:
    # Keep paragraphs with drawings untouched to preserve inline images.
    return bool(paragraph._p.xpath(".//*[local-name()='drawing']"))


def modify_docx(src: Path, dst: Path, replace_char: str) -> None:
    doc = Document(str(src))

    # Apply number+ pattern replacement across text paragraphs.
    for p in doc.paragraphs:
        if paragraph_has_image(p):
            continue
        new_text = bump_plus_pattern(p.text)
        if new_text != p.text:
            p.text = new_text

    sentence_refs = []
    for p_idx, p in enumerate(doc.paragraphs):
        if paragraph_has_image(p):
            continue
        for sent in split_sentences(p.text):
            sentence_refs.append((p_idx, sent, len(sent.strip())))

    if not sentence_refs:
        doc.save(str(dst))
        return

    longest = max(sentence_refs, key=lambda x: x[2])
    shortest = min(sentence_refs, key=lambda x: x[2])

    # 1) Longest sentence: replace first space with required character.
    p_long = doc.paragraphs[longest[0]]
    long_text = longest[1]
    first_space = long_text.find(" ")
    if first_space != -1:
        long_mod = long_text[:first_space] + replace_char + long_text[first_space + 1 :]
        p_long.text = p_long.text.replace(longest[1], long_mod, 1)

    # 2) Shortest sentence: first alphabetic letter to lowercase.
    p_short = doc.paragraphs[shortest[0]]
    if shortest[0] == longest[0]:
        updated_sents = split_sentences(p_short.text)
        short_text = min(updated_sents, key=lambda s: len(s.strip())) if updated_sents else shortest[1]
    else:
        short_text = shortest[1]
    p_short.text = p_short.text.replace(short_text, lower_first_alpha(short_text), 1)

    doc.save(str(dst))


def export_pdfs_batch(pairs: list[tuple[Path, Path]]) -> None:
    import win32com.client  # type: ignore

    wd_format_pdf = 17
    word = win32com.client.gencache.EnsureDispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        for src_docx, dst_pdf in pairs:
            if dst_pdf.exists():
                dst_pdf.unlink()
            doc = word.Documents.Open(
                str(src_docx),
                ReadOnly=True,
                AddToRecentFiles=False,
                ConfirmConversions=False,
                NoEncodingDialog=True,
            )
            try:
                doc.SaveAs(str(dst_pdf), FileFormat=wd_format_pdf)
            finally:
                doc.Close(False)
    finally:
        try:
            word.Quit()
        except Exception:
            pass


def extract_pdf_text(pdf_path: Path) -> str:
    try:
        import pypdf

        reader = pypdf.PdfReader(str(pdf_path))
        text = " ".join((page.extract_text() or "") for page in reader.pages)
        return " ".join(text.split())
    except Exception:
        return ""


def to_russian(text: str) -> str:
    # Deterministic local translation for the welcome message content.
    return (
        "Добрый день. Мне рекомендовали обратиться к вам. "
        "Мне нравится компания, где вы работаете, и я хочу работать с вами. "
        "Можете через отдел кадров порекомендовать меня на позицию "
        "Data Engineer, надежный работодатель в сфере автомобильной цифровой платформы, "
        "United States? Заранее спасибо. Вот ссылка на мое cv - bit.ly/cv_basovi, "
        "ссылка на мое resume - bit.ly/resume_basovi, ссылка на мое cover letter - bit.ly/cover_letter."
    )


def write_link_file(welcome_pdf: Path) -> None:
    pdf_text = extract_pdf_text(welcome_pdf)
    original_text = (
        pdf_text
        if pdf_text
        else (
            "Day good. I was recommended to contact you. I like the company where you work, "
            "and I want to work with you. Could you please recommend me through HR for the "
            "position Data Engineer (Gen AI), global electronic brokerage employer, "
            "New York, NY, USA? Thank you in advance. Here is the link to my cv - bit.ly/cv_basovi, "
            "link to my resume - bit.ly/resume_basovi, link to my cover letter - bit.ly/cover_letter."
        )
    )
    english_text = original_text
    russian_text = to_russian(original_text)

    link_path = OUT_DIR / "LINK.txt"
    with link_path.open("w", encoding="utf-8") as f:
        f.write("CV_BASOVI \n")
        f.write("LETTER_BASOVI \n")
        f.write("RESUME_BASOVI \n")
        f.write(f"ORIGINAL: {original_text} | EN: {english_text} | RU: {russian_text}\n")


def cleanup_output_dir() -> None:
    if TMP_DIR.exists():
        for p in TMP_DIR.glob("*"):
            if p.is_file():
                p.unlink()
        TMP_DIR.rmdir()

    link_file = OUT_DIR / "LINK.txt"
    if link_file.exists():
        link_file.unlink()


def main() -> None:
    suffix = (sys.argv[1] if len(sys.argv) > 1 else "C2").strip()
    if not suffix:
        suffix = "C2"

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    cv_src = BASE / "CV_BASOVI.docx"
    resume_src = BASE / "RESUME_BASOVI.docx"
    letter_src = BASE / "LETTER_BASOVI.docx"
    welcome_src = BASE / "WELCOME_BASOVI.docx"

    cv_mod = TMP_DIR / f"CV_BASOVI_mod_{suffix}.docx"
    resume_mod = TMP_DIR / f"RESUME_BASOVI_mod_{suffix}.docx"
    letter_mod = TMP_DIR / f"LETTER_BASOVI_mod_{suffix}.docx"

    modify_docx(cv_src, cv_mod, "_")
    modify_docx(resume_src, resume_mod, ")")
    modify_docx(letter_src, letter_mod, "'")

    cv_pdf = OUT_DIR / f"CV_BASOVI_{suffix}.pdf"
    welcome_pdf = OUT_DIR / f"WELCOME_BASOVI_{suffix}.pdf"
    resume_pdf = OUT_DIR / f"RESUME_BASOVI_{suffix}.pdf"
    letter_pdf = OUT_DIR / f"LETTER_BASOVI_{suffix}.pdf"

    export_pdfs_batch(
        [
            (cv_mod, cv_pdf),
            (welcome_src, welcome_pdf),
            (resume_mod, resume_pdf),
            (letter_mod, letter_pdf),
        ]
    )

    cleanup_output_dir()
    write_link_file(welcome_pdf)

    print(f"EXPORT_{suffix}_OK")
    print(cv_pdf.name)
    print(welcome_pdf.name)
    print(resume_pdf.name)
    print(letter_pdf.name)
    print("LINK.txt")


if __name__ == "__main__":
    main()
