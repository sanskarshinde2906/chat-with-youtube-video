import os

import google.generativeai as genai

from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel("gemini-3.5-flash")


def generate_answer(question, context):
    """
    Generate answer using retrieved context.

    Parameters
    ----------
    question : str
        User question.

    context : list[str]
        Retrieved chunks.

    Returns
    -------
    str
        LLM response.
    """

    context_text = "\n\n".join(context)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context,
reply with:
"I couldn't find the answer in the provided video."

Context:
{context_text}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text