import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def review_code(code,language):
    prompt = f"""
You are an expert software engineer and professional code reviewer.

Programming Language: {language}

Review the following code:

{code}

Analyze the code for:
1. Bugs
2. Security vulnerabilities
3. Performance issues
4. Code quality problems
5. Suggestions for improvement

Important rules:
- If the user hasn't given any code, just say that you must enter some code
- Report only real and meaningful problems.
- Do not invent issues just to fill a category.
- If a category has no meaningful issues, omit it.
- Do not repeat the same underlying problem under multiple categories.
- Distinguish clearly between bugs, security vulnerabilities,
  performance issues, and code-quality problems.
- Only report security issues when there is a realistic security impact.
- For every issue, briefly explain why it is a problem.
- Provide a practical suggestion for fixing each issue.
- Assign each issue one severity: Critical, Warning, or Suggestion.

Severity rules:
- Critical: Use ONLY for severe security vulnerabilities, major data loss,
  exploitable vulnerabilities, crashes, or severe correctness failures that
  can seriously affect the application or its users.
- Warning: Use for real bugs, memory leaks, resource-management problems,
  undefined behavior, significant performance problems, or correctness issues
  that should be fixed but are not severe enough to be Critical.
- Suggestion: Use for code-quality improvements, readability, maintainability,
  modern C++ practices, or minor optimizations.

Important:
- A memory leak by itself is NOT automatically Critical.
- A simple memory leak in a small example program should normally be Warning.
- Do not call an issue Critical unless there is a clear severe impact.
- Severity must be based on the actual context of the submitted code, not merely
  the type of issue.
- The Summary must not describe an issue as Critical unless the issue was
  actually classified as Critical above.
- Do not criticize code simply because it could be written differently.
- Focus on issues that genuinely need to be fixed or improved.
- Be technically accurate.
- Consider C++ behavior and best practices.
- Do not report the same root cause as multiple separate issues.
- Prefer identifying the root cause rather than listing consequences.
- Choose the most appropriate category for each issue.
- Include the exact line number for every issue when possible.
- Use the line numbers provided in the code.
- Do not invent line numbers.

Format the review as:

## Code Review

### Issues

**[Severity] [Category] — Line X**
- Problem: ...
- Why it matters: ...
- Suggested fix: ...

### Summary
Provide a short overall assessment of the code.
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: Unable to review the code.\n\nDetails: {str(e)}"