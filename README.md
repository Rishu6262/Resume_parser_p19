# 📄 AI Resume Parser Using NLP

## 📌 Project Overview

The **AI Resume Parser Using Natural Language Processing (NLP)** is an **End-to-End Artificial Intelligence** project designed to automatically extract meaningful information from resumes and convert unstructured resume documents into structured, machine-readable data. The project streamlines the resume screening process by leveraging **Natural Language Processing (NLP)** techniques to identify and organize essential candidate information.

The system utilizes **Python**, **SpaCy**, **Regular Expressions (Regex)**, **PyMuPDF**, and **Streamlit** to extract important details such as **candidate name**, **email address**, **phone number**, **technical skills**, **education**, **work experience**, **organizations**, **projects**, and **certifications** from uploaded resume files.

Before information extraction, the resume text is processed through a series of **text preprocessing** steps, including document parsing, text cleaning, normalization, and pattern matching. Advanced **Named Entity Recognition (NER)** techniques are then applied to recognize and classify key entities, enabling accurate extraction of candidate information.

The extracted data is presented in a structured format, making it easier for recruiters, HR professionals, and Applicant Tracking Systems (ATS) to analyze candidate profiles efficiently. By automating the resume screening process, the system significantly reduces manual effort, improves recruitment efficiency, and accelerates the candidate shortlisting process.

This project demonstrates practical expertise in **Artificial Intelligence**, **Natural Language Processing (NLP)**, **Information Extraction**, **Named Entity Recognition (NER)**, **Document Processing**, **Python Development**, and **Interactive Web Application Development**, making it an excellent portfolio project for aspiring **AI Engineers**, **Machine Learning Engineers**, **NLP Engineers**, **Python Developers**, and **Data Scientists**.

---

## ✨ Key Features

- 📄 Automatic Resume Parsing
- 🧠 Natural Language Processing (NLP)
- 🏷️ Named Entity Recognition (NER)
- 📧 Email & Phone Number Extraction
- 👨‍💻 Technical Skill Detection
- 🎓 Education & Experience Extraction
- 🏢 Organization Identification
- 📂 Project & Certification Detection
- 📊 Structured JSON Output
- 🌐 Interactive Streamlit Web Application
- 🚀 Deployment Ready
---

# 💡 Why Choose This Project?

Recruiters and hiring managers often receive **hundreds or even thousands of resumes** for a single job opening. Manually reviewing each resume is time-consuming, labor-intensive, and prone to human error, making the recruitment process slower and less efficient.

The **AI Resume Parser Using NLP** addresses this challenge by automatically extracting meaningful candidate information from unstructured resume documents using **Natural Language Processing (NLP)**, **Named Entity Recognition (NER)**, and **Regular Expressions (Regex)**. By converting resumes into structured, machine-readable data, the system helps streamline candidate screening, improve recruitment efficiency, and reduce manual effort.

### ⭐ Why I Chose This Project

- 🤖 Learn and apply **Natural Language Processing (NLP)** techniques.
- 📄 Work with real-world resume and document datasets.
- 🧠 Explore **Named Entity Recognition (NER)** and information extraction.
- 🔍 Practice **Regular Expressions (Regex)** for pattern matching.
- 💼 Understand AI applications in **HR Technology** and **Recruitment Automation**.
- 📊 Convert unstructured resume data into structured formats for analysis.
- 🌐 Build an interactive AI-powered application using **Streamlit**.
- 🚀 Develop an end-to-end NLP project that solves a real-world business problem.
- 💻 Strengthen practical skills in **Python**, **Artificial Intelligence**, **Natural Language Processing**, and **Document Processing**.

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
