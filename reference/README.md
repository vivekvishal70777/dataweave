# Original source material

These files are the unstructured bank the course was built from. Prefer `student/` and `sections/` while teaching.

| File | Contents |
| --- | --- |
| `MuleSoft-DataWeave-Interview-Questions.md` | 60 theory Q&A (easy / moderate / hard) |
| `DataWeave-Programming-Questions.md` | 54 coding drills with solutions |
| `LearnJava.pdf` | Extra Java notes (not part of the DataWeave Udemy path) |

After editing the two Markdown files, regenerate labs and lectures:

```bash
python3 scripts/generate_udemy_labs.py
python3 scripts/generate_udemy_lectures.py
```
