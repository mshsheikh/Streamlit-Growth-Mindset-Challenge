import streamlit as st

# ----
# CSS
# ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

:root {
    --primary: #2563eb;
    --secondary: #14b8a6;
    --success: #22c55e;
    --error: #ef4444;
    --background: #f8fafc;
    --text: #1e293b;
    --card-bg: #0e1117;
}

* {
    font-family: 'Inter', sans-serif;
}

body {
    background: var(--background);
    color: var(--text);
}

.main-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

.header {
    text-align: center;
    margin-bottom: 2.5rem;
    padding: 1.5rem;
    background: var(--card-bg);
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(0, 0, 0, 0.05);
}

.header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--primary);
    margin: 0;
    background: linear-gradient(135deg, #2563eb 0%, #14b8a6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.question-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.question-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.progress-container {
    margin: 2rem 0;
    position: relative;
}

.progress-bar {
    height: 8px;
    background: rgba(203, 213, 225, 0.3);
    border-radius: 4px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
    transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.progress-text {
    position: absolute;
    right: 0;
    top: -30px;
    color: var(--primary);
    font-weight: 600;
    font-size: 0.875rem;
}

.stRadio [role=radiogroup] {
    gap: 1rem;
}

.stRadio [role=radio] {
    background: var(--card-bg);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.25rem;
    transition: all 0.2s ease;
}

.stRadio [role=radio]:hover {
    border-color: var(--primary);
    transform: translateY(-1px);
}

.stRadio [role=radio][aria-checked=true] {
    background: var(--primary);
    color: white !important;
    border-color: var(--primary);
}

.stButton button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s ease;
    width: 100%;
    margin-top: 1rem;
}

.stButton button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.result-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 3rem 2rem;
    margin: 2rem 0;
    text-align: center;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.result-score {
    font-size: 3rem;
    font-weight: 700;
    color: var(--primary);
    margin: 1rem 0;
}

.correct-answer {
    color: var(--success);
    font-weight: 600;
}

.wrong-answer {
    color: var(--error);
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# -----
# Quiz
# -----
quiz_data = [
    {"question": "What is the correct way to create a function in Python?", 
     "options": ["def myFunction():", "create myFunction():", "function myFunction():", "myFunction():"], 
     "answer": "def myFunction():"},
    
    {"question": "Which of the following is used to add comments in Python?", 
     "options": ["// This is a comment", "# This is a comment", "<!-- This is a comment -->", "/* This is a comment */"], 
     "answer": "# This is a comment"},
    
    {"question": "What will be the output of print(type(10))?", 
     "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"], 
     "answer": "<class 'int'>"},
    
    {"question": "Which operator is used for exponentiation in Python?", 
     "options": ["^", "**", "//", "%"], 
     "answer": "**"},
    
    {"question": "What is the output of len('hello')?", 
     "options": ["4", "5", "6", "7"], 
     "answer": "5"},
    
    {"question": "Which data type is mutable in Python?", 
     "options": ["String", "Tuple", "List", "Integer"], 
     "answer": "List"},
    
    {"question": "What does the append() method do in Python?", 
     "options": ["Adds an element to the end of a list", "Removes the last element of a list", "Sorts a list", "Reverses a list"], 
     "answer": "Adds an element to the end of a list"},
    
    {"question": "Which keyword is used to define a loop in Python?", 
     "options": ["for", "while", "loop", "Both for and while"], 
     "answer": "Both for and while"},
    
    {"question": "What is the result of 3 == 3.0 in Python?", 
     "options": ["True", "False", "Error", "None"], 
     "answer": "True"},
    
    {"question": "What is the purpose of the break statement?", 
     "options": ["To stop the program", "To exit the current loop", "To skip the current iteration", "To restart the loop"], 
     "answer": "To exit the current loop"},
]

# ------
# Logic
# ------
def main():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="header">
        <h1>Python Mastery Quiz</h1>
    </div>
    """, unsafe_allow_html=True)

    # Session state
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []

    # Progress Bar
    progress = (st.session_state.current_question / len(quiz_data)) * 100
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-text">Complete: {int(progress)}%</div>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Current Question
    current_q = st.session_state.current_question
    if current_q < len(quiz_data):
        question_data = quiz_data[current_q]
        st.markdown(f"""
        <div class="question-card">
            <h3>Question {current_q + 1}</h3>
            <p>{question_data['question']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Display Options
        selected_option = st.radio(
            "Select your answer:",
            question_data["options"],
            key=f"q{current_q}",
            index=None
        )

        # Submit Button
        if st.button("Submit Answer"):
            if selected_option == question_data["answer"]:
                st.session_state.score += 1
            st.session_state.answers.append((selected_option, question_data["answer"]))
            st.session_state.current_question += 1
            st.rerun()
    else:
        # Final Score
        result_html = f"""
        <div class="result-card">
            <h2>Quiz Completed!</h2>
            <div class="result-score">{st.session_state.score}/{len(quiz_data)}</div>
            <h3>Detailed Results:</h3>
        </div>
        """
        st.markdown(result_html, unsafe_allow_html=True)

        # Show Answers
        for i, (selected, correct) in enumerate(st.session_state.answers):
            answer_html = f"""
            <div class="question-card">
                <h4>Question {i+1}</h4>
                <p>{quiz_data[i]['question']}</p>
                <p class={'correct-answer' if selected == correct else 'wrong-answer'}>
                    Your answer: {selected or "No answer"}
                </p>
                <p class="correct-answer">Correct answer: {correct}</p>
            </div>
            """
            st.markdown(answer_html, unsafe_allow_html=True)

        # Restart
        if st.button("Retake Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answers = []
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()