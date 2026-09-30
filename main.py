from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="LegalEase", version="1.0.0")

class DraftRequest(BaseModel):
    document_type: str
    party_a: str
    party_b: str
    effective_date: str = ""
    terms: str = ""
    jurisdiction: str = ""

@app.get("/", response_class=HTMLResponse)
def home():
    with open("app/templates/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/api/generate")
def generate(req: DraftRequest):
    today = req.effective_date.strip() or str(date.today())
    common = f"\nDOCUMENT: {req.document_type}\nEffective date: {today}\nJurisdiction: {req.jurisdiction or '[Specify jurisdiction]'}\n\nPARTIES\nParty A: {req.party_a}\nParty B: {req.party_b}\n\n"
    if req.document_type == "NDA":
        body = ("CONFIDENTIALITY AGREEMENT\n\nThe parties agree to use confidential information only for the stated purpose, "
                "to protect it with reasonable care, and not to disclose it except as authorized or required by law. "
                "Confidentiality obligations do not apply to information that is public, already known lawfully, "
                "independently developed, or rightfully received from another source.\n\n")
    elif req.document_type == "Lease Agreement":
        body = ("LEASE AGREEMENT\n\nThe parties intend Party A to act as landlord and Party B as tenant. "
                "The premises, rent, deposit, term, utilities, maintenance duties, permitted use, and termination "
                "conditions must be completed and agreed in writing before signing.\n\n")
    else:
        body = ("EMPLOYMENT AGREEMENT\n\nThe parties intend Party A to act as employer and Party B as employee. "
                "Role, responsibilities, compensation, working hours, leave, benefits, confidentiality, "
                "termination, and applicable policies must be completed and agreed before signing.\n\n")
    return {"document": common + body + "KEY TERMS\n" + (req.terms or "[Add agreed terms]") +
            "\n\nSIGNATURES\nParty A: ____________________  Date: __________\n"
            "Party B: ____________________  Date: __________\n\n"
            "DRAFTING NOTE: This is a starting template, not legal advice. Review for local law and your circumstances."}
