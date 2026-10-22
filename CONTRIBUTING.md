# Contributing to Python for AI

Thanks for helping make this learning repository clearer and more useful. Lessons should be accessible to beginners while remaining technically accurate and runnable.

## Lesson structure

When practical, a lesson should include:

1. **Overview** — what the lesson covers and prerequisites.
2. **Learning objectives** — specific skills the learner should gain.
3. **Concept explanations** — short, precise explanations with examples.
4. **Runnable code** — focused cells with clear variable names.
5. **Expected output** — text output or a chart and an explanation of the result.
6. **Common mistakes** — likely errors and how to resolve them.
7. **Exercises** — basic, intermediate, and applied tasks.
8. **Solutions** — separate reference answers so learners can try first.
9. **Mini-project** — a small end-to-end application.
10. **Summary and references** — recap and reliable further reading.

## Notebook standards

- Keep one main idea per section and use descriptive Markdown headings.
- Put explanation before code and interpret output immediately after it.
- Import dependencies near the beginning and use a consistent random seed when randomness affects an example.
- Prefer small, reproducible datasets; explain any external data requirements.
- Avoid hidden state: notebooks should run from top to bottom in a fresh kernel.
- Clear accidental tracebacks and irrelevant intermediate output before committing.
- Do not claim a notebook was tested unless it was actually executed.
- Do not put poster-only visual styling or large decorative elements into technical notebooks.

## Code standards

- Use descriptive names and conventional Python formatting.
- Explain non-obvious logic; avoid comments that merely repeat each line.
- Handle common edge cases where relevant.
- Keep examples focused and provide expected output when it improves learning.
- Use relative paths or explain the expected working directory.

## Exercises and projects

- State the task, input assumptions, expected behavior, and success criteria.
- Put learner prompts separately from reference solutions.
- Prefer applications that reinforce the lesson instead of adding unrelated dependencies.

## Visual identity

Presentation materials use the HAZEM ELSHAFEY identity: charcoal `#191919`, yellow `#FFDC52`, white `#FFFFFF`, cream `#FAF8F0`, orange `#FF6B35`, and a blue accent. Use the visual identity in slide assets. Keep the notebook primarily functional and readable.

## Before submitting

- [ ] Links and relative paths work.
- [ ] Code is syntactically valid.
- [ ] Notebook cells run from top to bottom in a clean environment.
- [ ] Expected outputs match the code.
- [ ] Exercises and solutions are aligned.
- [ ] New dependencies are documented in `requirements.txt`.
- [ ] The README or lesson index is updated if needed.
