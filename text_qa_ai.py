# Text-Based Question Answering using Pattern Matching
# Simple AI Project

text = """
Mary went shopping yesterday. Mary bought a new coat.
She really liked the red one. Later, Mary met John at the mall.
"""

question_patterns = {
    "what did mary buy": "Mary bought z",
    "who did mary meet": "Mary met z"
}

def answer_question(question):
    question = question.lower()

    for q_pattern in question_patterns:
        if q_pattern in question:
            text_pattern = question_patterns[q_pattern]

            for sentence in text.split("."):
                sentence = sentence.strip()
                if text_pattern.replace("z", "") in sentence:
                    answer = sentence.replace(text_pattern.replace("z", ""), "")
                    return answer.strip()

    return "No answer found in the text."

# Example Run
print("Text:", text)
user_question = input("Enter your question: ")
print("Answer:", answer_question(user_question))
