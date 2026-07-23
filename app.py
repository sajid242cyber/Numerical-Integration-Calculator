import streamlit as st
import numpy as np
from integration import calculate_integral
from graph import plot_graph

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Numerical Integration Calculator",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

html,body,[class*="css"]{
    font-family:Arial,sans-serif;
}

.main{
    background:#0f172a;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3,h4,h5,h6{
    color:white;
}

label{
    color:white!important;
}

hr{
    border:1px solid #334155;
}

.stButton>button{

    width:100%;
    background:#2563eb;
    color:white;
    font-size:18px;
    font-weight:bold;
    padding:12px;
    border-radius:10px;
    border:none;

}

.stButton>button:hover{

    background:#1d4ed8;

}

.result-card{

    background:#111827;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #38bdf8;

}

.summary-card{

    background:#111827;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #22c55e;

}

.info-card{

    background:#1e293b;
    padding:20px;
    border-radius:12px;
    border-left:6px solid orange;

}

.footer{

    text-align:center;
    color:#cbd5e1;
    font-size:13px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.title("📈 Numerical Integration Calculator")

st.write(
    "Calculate definite integrals using different Numerical Integration methods."
)

st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("📚 Numerical Methods")

    st.success("Available Methods")

    st.markdown("""
- Trapezoidal Rule

- Simpson 1/3 Rule

- Simpson 3/8 Rule

- Weddle Rule
""")

    st.divider()

    st.info("""
Use valid mathematical expressions.

Examples

x**2

np.sin(x)

np.exp(x)

np.log(x+1)

np.sqrt(x)
""")

# ==========================================================
# TEAM INFORMATION
# ==========================================================

st.markdown("""
<div class="info-card">

<h3>Team Beta</h3>

Numerical Integration Calculator

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# USER INPUT
# ==========================================================

st.header("Input Parameters")

col1,col2=st.columns(2)

with col1:

    function_input=st.text_input(
        "Function f(x)",
        value="x**2"
    )

    lower_limit=st.number_input(
        "Lower Limit (a)",
        value=0.0,
        step=0.1
    )

with col2:

    upper_limit=st.number_input(
        "Upper Limit (b)",
        value=2.0,
        step=0.1
    )

    intervals=st.number_input(
        "Number of Intervals (n)",
        min_value=1,
        value=6,
        step=1
    )

method=st.selectbox(

    "Numerical Method",

    [

        "Trapezoidal Rule",

        "Simpson 1/3 Rule",

        "Simpson 3/8 Rule",

        "Weddle Rule"

    ]

)

st.write("")

calculate=st.button("Calculate Integration")

# ==========================================================
# CALCULATION
# ==========================================================

if calculate:

    try:

        if function_input.strip()=="":

            st.error("Function cannot be empty.")

            st.stop()

        if lower_limit>=upper_limit:

            st.error("Lower limit must be smaller than upper limit.")

            st.stop()

        n=int(intervals)

        if method=="Simpson 1/3 Rule":

            if n%2!=0:

                st.error("Simpson 1/3 Rule requires EVEN intervals.")

                st.stop()

        if method=="Simpson 3/8 Rule":

            if n%3!=0:

                st.error("Simpson 3/8 Rule requires intervals divisible by 3.")

                st.stop()

        if method=="Weddle Rule":

            if n%6!=0:

                st.error("Weddle Rule requires intervals divisible by 6.")

                st.stop()

        def f(x):

            return eval(

                function_input,

                {"__builtins__":{}},

                {

                    "x":x,

                    "np":np,

                    "sin":np.sin,

                    "cos":np.cos,

                    "tan":np.tan,

                    "exp":np.exp,

                    "sqrt":np.sqrt,

                    "log":np.log,

                    "pi":np.pi,

                    "e":np.e

                }

            )

        result=calculate_integral(

            method,

            f,

            lower_limit,

            upper_limit,

            n

        )
                # ==========================================================
        # RESULT
        # ==========================================================

        st.markdown(
            f"""
            <div class="result-card">
                <h3>Integration Result</h3>
                <h2>{result:.10f}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # ==========================================================
        # GRAPH
        # ==========================================================

        figure = plot_graph(
            f,
            lower_limit,
            upper_limit
        )

        st.pyplot(figure)

        st.write("")

        # ==========================================================
        # SUMMARY
        # ==========================================================

        st.markdown(
            f"""
            <div class="summary-card">

            <h3>Summary</h3>

            <b>Function:</b> {function_input}<br>

            <b>Lower Limit:</b> {lower_limit}<br>

            <b>Upper Limit:</b> {upper_limit}<br>

            <b>Intervals:</b> {n}<br>

            <b>Method:</b> {method}<br>

            <b>Integral Value:</b> {result:.10f}

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # ==========================================================
        # DOWNLOAD RESULT
        # ==========================================================

        report = f"""
NUMERICAL INTEGRATION REPORT

-------------------------------------

Function : {function_input}

Lower Limit : {lower_limit}

Upper Limit : {upper_limit}

Intervals : {n}

Method : {method}

Result : {result:.10f}

-------------------------------------

Developed by Team Beta
"""

        st.download_button(
            label="Download Result",
            data=report,
            file_name="integration_result.txt",
            mime="text/plain"
        )

    except Exception as e:

        st.error(f"Error: {e}")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    <b>Developed by Team Beta</b><br><br>

    Adib Mahamud Sajid &nbsp; | &nbsp;
    Ashraful Haque &nbsp; | &nbsp;
    Kamrul Hasan &nbsp; | &nbsp;
    Shutopa Kundu &nbsp; | &nbsp;
    Prethila Bepari

    </div>
    """,
    unsafe_allow_html=True
)