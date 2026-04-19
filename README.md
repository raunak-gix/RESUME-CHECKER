# 🧠 AI Resume Analyzer

A web-based application that analyzes resumes and provides an ATS-style score along with personalized suggestions to improve content, skills, and formatting.

---

## 🚀 Features

* 📄 Upload Resume (PDF)
* 📊 ATS Score (out of 100)
* ✅ Detected Skills
* ❌ Missing Skills
* 💡 Smart Suggestions for Improvement
* ⚡ Fast and lightweight (Flask-based)

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Libraries:** pdfplumber
* **Optional AI Integration:** OpenAI API

---

## 📂 Project Structure

```
resume-analyzer/
│
├── app.py
├── requirements.txt
├── uploads/
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. Text is extracted using `pdfplumber`
3. Resume is analyzed based on:

   * Skills match
   * Resume length
   * Project presence
   * Basic formatting checks
4. A score is generated along with suggestions

---

## 📊 Scoring Criteria

| Parameter         | Marks |
| ----------------- | ----- |
| Skills Match      | 40    |
| Resume Length     | 20    |
| Projects Included | 20    |
| Basic Formatting  | 20    |
| **Total**         | 100   |

---

## 💡 Example Output

* **ATS Score:** 72/100
* **Skills Found:** Python, HTML, CSS
* **Missing Skills:** AWS, React
* **Suggestions:**

  * Add more relevant skills
  * Include project details
  * Improve formatting

---

## 🔒 Notes

* Ensure the `uploads/` folder exists or is auto-created
* File names are sanitized using `secure_filename()`
* Works best with text-based PDFs

---

## 🚀 Future Improvements

* 🤖 AI-based suggestions using OpenAI
* 📈 Visual analytics (charts, graphs)
* 🌐 Deployment (Netlify + Render/AWS)
* 📎 Support for DOCX files
* 🎯 Job-role based analysis

---

## 📸 Screenshots

*Add your project screenshots here*

---

## 📜 License

This project is open-source and free to use.

---

## 🙌 Acknowledgements

* Flask Documentation
* pdfplumber Library

---

## 👨‍💻 Author

**Raunak Das**

* GitHub: https://github.com/your-username
* Portfolio: (Add your link)

---
