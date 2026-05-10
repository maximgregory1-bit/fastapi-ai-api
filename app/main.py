from fastapi import FastAPI, HTTPException

from app.schemas import (
    SummarizeRequest,
    SummarizeResponse,
    TranslateRequest,
    TranslateResponse,
    TitleRequest,
    TitleResponse,
    ExplainCodeRequest,
    ExplainCodeResponse,
)

from app.openai_service import (
    summarize_text,
    translate_text,
    generate_titles,
    explain_code,
)

app = FastAPI(
    title="FastAPI OpenAI Practice API",
    description="Simple AI endpoints using FastAPI and OpenAI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "FastAPI OpenAI API is running"
    }


@app.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    try:
        summary = summarize_text(
            text=request.text,
            style=request.style
        )

        return SummarizeResponse(summary=summary)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while summarizing the text."
        )


@app.post("/translate", response_model=TranslateResponse)
def translate(request: TranslateRequest):
    try:
        translation = translate_text(
            text=request.text,
            target_language=request.target_language
        )

        return TranslateResponse(translation=translation)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while translating the text."
        )


@app.post("/generate-title", response_model=TitleResponse)
def create_titles(request: TitleRequest):
    try:
        titles = generate_titles(
            text=request.text,
            count=request.count
        )

        return TitleResponse(titles=titles)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while generating titles."
        )


@app.post("/explain-code", response_model=ExplainCodeResponse)
def explain(request: ExplainCodeRequest):
    try:
        explanation = explain_code(
            code=request.code,
            language=request.language
        )

        return ExplainCodeResponse(explanation=explanation)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while explaining the code."
        )