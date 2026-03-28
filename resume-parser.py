import fitz
import re
import spacy

# load spacy model
nlp = spacy.load("en_core_web_sm")

def parse_resume(uploaded_file):
    # read pdf
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    text = ""
    for page in doc:
        text += page.get_text()

    text_lower = text.lower()

    # email
    email = re.findall(r'\S+@\S+', text)

    # phone
    phone = re.findall(r'\d{10}', text)

    # skills
    skills_list = [
        "python", "java", "sql", "machine learning",
        "deep learning", "pandas", "numpy", "tensorflow",
        "pytorch", "excel"
    ]

    found_skills = []
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)

    # spacy NER
    doc_nlp = nlp(text)

    companies = []
    for ent in doc_nlp.ents:
        if ent.label_ == "ORG":
            companies.append(ent.text)

    # experience
    experience = re.findall(r'\d+\.?\d*\+?\s+years?', text_lower)

    # final output
    data = {
        "Email": email[0] if email else None,
        "Phone": phone[0] if phone else None,
        "Skills": list(set(found_skills)),
        "Companies": list(set(companies)),
        "Experience": experience[0] if experience else None
    }

    return data