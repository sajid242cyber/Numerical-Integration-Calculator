# 📈 Numerical Integration Calculator

<p align="center">
  <img src="assets/team-beta.png" alt="Team Beta – Numerical Integration Calculator" width="900">
</p>

<h3 align="center">A Streamlit-based Numerical Integration Web Application</h3>

<p align="center">
  <a href="https://numerical-integration-calculator-9kvmq5669recyxscccvd4a.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Live Demo">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge&logo=matplotlib" alt="Matplotlib">
</p>

---

## 🔗 Live Application

**Try the deployed application:**  
👉 https://numerical-integration-calculator-9kvmq5669recyxscccvd4a.streamlit.app/

---

## 📌 Project Overview

The **Numerical Integration Calculator** is a Python and Streamlit-based web application developed as part of the **Numerical Methods** course.

The application provides an interactive interface for approximating definite integrals using several classical numerical integration techniques. Users can enter a mathematical function, define the integration limits and number of intervals, select an integration method, and instantly view the calculated result together with a graphical representation of the function and integration area.

The project was designed to combine **numerical computation, Python programming, data visualization, and an accessible web interface** in a single application.

---

## 🎯 Project Objectives

- Implement commonly used numerical integration algorithms.
- Provide an easy-to-use graphical interface for numerical calculations.
- Visualize the selected function and integration region.
- Validate method-specific interval requirements.
- Generate a downloadable integration result report.
- Demonstrate the practical use of Python in Numerical Methods.

---

## ✨ Key Features

- ✅ Trapezoidal Rule
- ✅ Simpson's 1/3 Rule
- ✅ Simpson's 3/8 Rule
- ✅ Weddle's Rule
- ✅ Mathematical function input
- ✅ Custom lower and upper limits
- ✅ User-defined number of intervals
- ✅ Method-specific input validation
- ✅ Function graph visualization
- ✅ Shaded integration region
- ✅ Numerical result displayed with high precision
- ✅ Calculation summary
- ✅ Downloadable `.txt` result report
- ✅ Streamlit-based responsive interface

---

## 🧮 Numerical Methods Implemented

### 1. Trapezoidal Rule

Approximates a definite integral by dividing the interval into smaller sections and representing each section as a trapezoid.

**General requirement:** `n ≥ 1`

---

### 2. Simpson's 1/3 Rule

Uses quadratic interpolation to approximate the area under a curve.

**Requirement:**  
The number of intervals must be **even**.

---

### 3. Simpson's 3/8 Rule

Uses cubic interpolation over groups of three intervals.

**Requirement:**  
The number of intervals must be **divisible by 3**.

---

### 4. Weddle's Rule

A higher-order Newton–Cotes numerical integration technique that operates over groups of six intervals.

**Requirement:**  
The number of intervals must be **divisible by 6**.

---

## 🖥️ Application Workflow

```text
Enter Function f(x)
        │
        ▼
Set Lower & Upper Limits
        │
        ▼
Set Number of Intervals
        │
        ▼
Select Numerical Method
        │
        ▼
Validate Inputs
        │
        ▼
Calculate Numerical Integral
        │
        ├──────────────► Display Result
        │
        ├──────────────► Plot Function & Area
        │
        └──────────────► Generate Downloadable Report
```

---

## 🧪 Example Input

```text
Function: x**2
Lower Limit: 0
Upper Limit: 2
Intervals: 6
Method: Trapezoidal Rule
```

The application then displays:

- Numerical integration result
- Function graph
- Shaded integration area
- Calculation summary
- Downloadable report

---

## 📐 Supported Mathematical Expressions

Examples of valid expressions include:

```python
x**2
x**3 + 2*x
np.sin(x)
np.cos(x)
np.tan(x)
np.exp(x)
np.log(x + 1)
np.sqrt(x)
```

Common mathematical functions and constants are also supported:

```python
sin(x)
cos(x)
tan(x)
exp(x)
sqrt(x)
log(x)
pi
e
```

> **Note:** The selected function should be mathematically valid over the specified integration interval.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web application interface |
| **NumPy** | Numerical computation |
| **Matplotlib** | Function plotting and visualization |

---

## 📂 Project Structure

```text
Numerical-Integration-Calculator/
│
├── app.py
├── integration.py
├── graph.py
├── requirements.txt
├── README.md
│
└── assets/
    ├── team-beta.png
    └── team/
        ├── kamrul-hasan-kabir.png
        ├── prethila-bepari.png
        ├── adib-mahamud-sajid.png
        ├── shutopa-kundu.png
        └── ashraful-haque.png
```

### File Responsibilities

- **`app.py`** — Streamlit user interface, input handling, validation, result display and report download.
- **`integration.py`** — Numerical integration algorithms and method selection.
- **`graph.py`** — Function plotting and integration-area visualization.
- **`requirements.txt`** — Python package dependencies.
- **`assets/`** — Project/team presentation images used by this README.

---

## ⚙️ Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/saijd242cyber/Numerical-Integration-Calculator.git
cd Numerical-Integration-Calculator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will normally open in your browser at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

This project is deployed using **Streamlit Community Cloud**.

### Live URL

https://numerical-integration-calculator-9kvmq5669recyxscccvd4a.streamlit.app/

---

## 👥 Team Beta

<p align="center">

| Team Member | Student ID |
|---|---|
| <img src="assets/team/kamrul-hasan-kabir.png" width="90"><br>**Kamrul Hasan Kabir** | 242-15-782 |
| <img src="assets/team/prethila-bepari.png" width="90"><br>**Prethila Bepari** | 242-15-472 |
| <img src="assets/team/adib-mahamud-sajid.png" width="90"><br>**Adib Mahamud Sajid** | 242-15-137 |
| <img src="assets/team/shutopa-kundu.png" width="90"><br>**Shutopa Kundu** | 242-15-091 |
| <img src="assets/team/ashraful-haque.png" width="90"><br>**Ashraful Haque** | 242-15-025 |

</p>

---

## 🎓 Academic Information

**Course:** Numerical Methods  
**Department:** Computer Science and Engineering  
**Institution:** Daffodil International University

### Course Teacher

**Noor Muhammad**  
Lecturer  
Department of Computer Science and Engineering  
Daffodil International University

---

## 📊 What the Application Demonstrates

This project demonstrates practical implementation of:

- Numerical integration
- Algorithm design
- Python programming
- Numerical computation with NumPy
- Mathematical expression handling
- Data visualization with Matplotlib
- Input validation
- Interactive web application development with Streamlit
- Basic software project organization

---

## 🔮 Possible Future Improvements

Potential extensions for future versions include:

- Exact/analytical integration for comparison
- Numerical error calculation
- Relative and absolute error analysis
- Method-to-method result comparison
- More numerical integration techniques
- Interactive Plotly visualizations
- Calculation history
- Export to PDF/CSV
- More advanced expression parsing and validation
- Improved accessibility and UI customization

---

## 📜 Academic Note

This application was developed for academic and educational purposes as a project for the **Numerical Methods** course. The implementation is intended to demonstrate the practical application of numerical integration algorithms using Python.

---

## 🙏 Acknowledgement

We would like to express our gratitude to **Noor Muhammad, Lecturer, Department of Computer Science and Engineering, Daffodil International University**, for his guidance and academic support throughout the course and project work.

---

<p align="center">
  <b>Developed with Python • Streamlit • NumPy • Matplotlib</b><br>
  <i>Team Beta — Numerical Integration Calculator</i>
</p>
