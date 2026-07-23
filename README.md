# 📈 Numerical Integration Calculator

A professional Streamlit web application for solving definite integrals using popular Numerical Integration methods.

---

# Features

- Trapezoidal Rule
- Simpson's 1/3 Rule
- Simpson's 3/8 Rule
- Weddle Rule
- Function Graph Visualization
- Input Validation
- Numerical Integration Report Download
- Professional User Interface
- Responsive Design

---

# Technologies Used

- Python
- Streamlit
- NumPy
- Matplotlib

---

# Project Structure

```text
Numerical_Integration_Project/
│
├── app.py
├── integration.py
├── graph.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone or download the project.

Install the required packages.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

---

# Supported Mathematical Functions

Examples:

```python
x**2
```

```python
x**3 + 2*x
```

```python
np.sin(x)
```

```python
np.cos(x)
```

```python
np.exp(x)
```

```python
np.log(x + 1)
```

```python
np.sqrt(x)
```

---

# Numerical Methods

### Trapezoidal Rule

Approximates the area under a curve using trapezoids.

---

### Simpson's 1/3 Rule

Uses quadratic interpolation.

**Requirement:** Number of intervals must be even.

---

### Simpson's 3/8 Rule

Uses cubic interpolation.

**Requirement:** Number of intervals must be divisible by 3.

---

### Weddle Rule

Provides higher-order numerical integration.

**Requirement:** Number of intervals must be divisible by 6.

---

# Example

Function

```text
x**2
```

Lower Limit

```text
0
```

Upper Limit

```text
2
```

Intervals

```text
6
```

Method

```text
Trapezoidal Rule
```

---

# Output

- Numerical Integration Result
- Function Graph
- Summary
- Downloadable Report

---

# Developed By

## Team Beta

- Adib Mahamud Sajid
- Ashraful Haque
- Kamrul Hasan
- Shutopa Kundu
- Prethila Bepari

---

**Thank you for using the Numerical Integration Calculator.**