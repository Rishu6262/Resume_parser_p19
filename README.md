# 📄 AI Resume Parser Using NLP

## 📌 Project Overview

The AI Resume Parser is a Natural Language Processing (NLP) project that automatically extracts important information from resumes and converts unstructured resume documents into structured data.

The system uses NLP, Regular Expressions (Regex), SpaCy, and Python to identify candidate details such as name, email address, phone number, skills, experience, and organizations from uploaded resumes.

This project demonstrates the practical application of Artificial Intelligence and NLP in recruitment and HR automation.

---

# ❓ Why I Chose This Project?

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing resumes is time-consuming and inefficient.

I chose this project to:

* Learn Natural Language Processing (NLP).
* Work with real-world document data.
* Automate resume screening.
* Understand information extraction techniques.
* Build a practical AI application for HR technology.

---

# 🚀 Project Objectives

* Extract information automatically from resumes.
* Reduce manual resume screening efforts.
* Identify candidate skills efficiently.
* Convert unstructured text into structured data.
* Demonstrate NLP-based information extraction.

---

# 📊 Features Extracted

The system can identify:

### Personal Information

* Candidate Name
* Email Address
* Phone Number

### Professional Information

* Skills
* Experience
* Organizations
* Education Details

### Additional Information

* Projects
* Certifications
* Technical Skills

---

# 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* SpaCy
* Regex (re)
* PyMuPDF (fitz)
* Streamlit
* Pandas
* NumPy

### NLP Techniques

* Named Entity Recognition (NER)
* Text Extraction
* Pattern Matching
* Information Retrieval

---

# 📂 Project Structure

```bash
Resume_Parser_Project/
│
├── app.py
├── model/
├── resume_parser.ipynb
├── requirements.txt
├── README.md
│
└── resumes/
    └── sample_resume.pdf
```

---

# 🔍 Workflow

### Step 1: Upload Resume

The user uploads a resume file.

Supported Formats:

* PDF
* DOCX

---

### Step 2: Extract Text

The system extracts text using:

```python
PyMuPDF (fitz)
```

---

### Step 3: Text Processing

Text preprocessing includes:

* Cleaning text
* Removing unnecessary characters
* Lowercase conversion

---

### Step 4: Information Extraction

Using:

* Regex
* SpaCy NER

The system extracts:

* Email
* Phone Number
* Skills
* Name
* Experience

---

### Step 5: Structured Output

The extracted information is displayed in JSON format.

Example:

```json
{
  "Email": "example@gmail.com",
  "Phone": "9876543210",
  "Skills": ["Python", "Machine Learning", "SQL"],
  "Companies": [],
  "Experience": "2 Years"
}
```

---

# 🤖 NLP Techniques Used

## Regular Expressions (Regex)

Used for:

* Email Extraction
* Phone Number Extraction

Example:

```python
re.findall()
```

---

## SpaCy Named Entity Recognition (NER)

Used for:

* Person Name Detection
* Organization Detection
* Location Detection

Example:

```python
nlp = spacy.load("en_core_web_sm")
```

---

# 💻 Streamlit Application

The project includes a user-friendly Streamlit interface.

### User Actions

* Upload Resume
* Process Resume
* View Extracted Information

### Output

* Name
* Email
* Phone Number
* Skills
* Experience
* Organizations

---

# 📈 Benefits of the Project

* Automates resume screening
* Saves recruiter time
* Reduces manual effort
* Improves candidate shortlisting
* Demonstrates NLP capabilities

---

# ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-parser.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
spacy
pymupdf
numpy
pandas
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Natural Language Processing
* Named Entity Recognition
* Resume Parsing
* Regex Pattern Matching
* Information Extraction
* Document Processing
* Streamlit Deployment
* AI-Powered Recruitment Systems

---

# 🔮 Future Improvements

* Resume Ranking System
* ATS Score Calculator
* Job Description Matching
* Resume Classification
* Candidate Recommendation System
* Multiple Language Support

---

# 🚧 Project Status

This project is currently under development and serves as a learning-focused implementation of Resume Parsing using Natural Language Processing (NLP).

The core functionalities such as text extraction, email detection, phone number extraction, skill identification, and Named Entity Recognition (NER) have been implemented and tested successfully. However, some advanced features and deployment-related issues are still being optimized.

---

### Current Progress

✅ Resume Text Extraction

✅ Email Extraction

✅ Phone Number Detection

✅ Skill Extraction Using NLP

✅ Named Entity Recognition (SpaCy)

✅ Streamlit User Interface

⚠ Experience Extraction Needs Improvement

⚠ Organization Detection Needs Optimization

⚠ Some Resume Formats May Produce Inconsistent Results

⚠ Production Deployment Not Yet Completed

---

### Future Work

* Improve Experience Detection
* Better Organization Extraction
* Support More Resume Formats
* ATS Score Calculation
* Resume Ranking System
* Job Description Matching
* Complete Deployment Pipeline

This project was developed primarily to learn and explore NLP, Information Extraction, Resume Parsing, SpaCy, Regex, and Streamlit application development.


# 📜 Disclaimer

This project is developed for educational and research purposes only.

The extracted information depends on the structure and quality of the uploaded resume. Results may vary for different resume formats and layouts.

---

# ✅ Conclusion

This project demonstrates how Natural Language Processing and Artificial Intelligence can automate resume analysis by extracting important candidate information from unstructured documents. The system improves recruitment efficiency and showcases the practical use of NLP, SpaCy, Regex, and Streamlit in HR and talent acquisition applications.

---

# 👨‍💻 Author

**Rishu Gurjar**

Aspiring Data Science | Machine Learning Enthusiast | Python Developer

### Skills

* Python
* Machine Learning
* Deep Learning
* NLP
* SQL
* Streamlit
* Data Analysis
