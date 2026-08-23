# Original source material

These files are the unstructured bank the course was built from. Prefer `student/` and `sections/` while teaching.

| File | Contents |
| --- | --- |
| `MuleSoft-DataWeave-Interview-Questions.md` | 60 theory Q&A (easy / moderate / hard) |
| `DataWeave-Programming-Questions.md` | 54 coding drills with solutions |

Do not add third-party books or publisher PDFs here. `LearnJava.pdf` was a copyrighted Sams title and was removed; see [`instructor/PUBLISHING-RIGHTS.md`](../instructor/PUBLISHING-RIGHTS.md).

After editing the two Markdown files, regenerate labs and lectures:

```bash
python3 scripts/generate_udemy_labs.py
python3 scripts/generate_udemy_lectures.py
```
