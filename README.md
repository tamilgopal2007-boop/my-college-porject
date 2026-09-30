# LegalEase
AI-assisted legal document drafting starter app.

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

This starter generates editable template-based drafts. It is not legal advice; have important documents reviewed by a qualified lawyer.
