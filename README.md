# AcademiaChat 🎓💬

**AcademiaChat** is a role-based academic assistant web app that enables students and teachers to interact with curriculum-based documents using natural language. The app provides contextual responses from uploaded documents (Excel, PDF, etc.) and allows document management through a simple web interface.

---

## 📌 Features

- 🔐 **Role-Based Authentication**: Secure login for students and teachers using `streamlit_authenticator`.
- 📊 **Document Upload & Query**: Upload `.xlsx` or `.pdf` files and ask questions related to their contents.
- 🧠 **LLM Integration Ready**: Incorporates `LangChain` for question-answering over academic content.
- 📁 **Multi-Format Support**: Works with Excel (`openpyxl`) and PDF files (`PyPDF2`).
- 🗃️ **Document Storage & Retrieval**: Backend CRUD operations for managing files and responses.
- 📄 **Environment Security**: Sensitive data managed via `.env` file.

---

# 🛠️ Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Frontend     | Streamlit                 |
| Auth System  | streamlit-authenticator   |
| Backend      | Python                    |
| Document I/O | openpyxl, PyPDF2          |
| Environment  | python-dotenv (`.env`)    |
| LLM Support  | LangChain                 |
| DB Interface | MySQL (via connector)     |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AcademiaChat.git
cd AcademiaChat
```
### 2. Set Up Environment

```bash
# .env
EMAIL=youremail@example.com
PASSWORD=yourpassword
OPENAI_API_KEY=yourkey
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the App
```bash
streamlit run app.py
```
