from pydantic import BaseModel, Field


# class ChatRequest(BaseModel):
#     message: str


# class ChatResponse(BaseModel):
#     reply: str

class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10)
    style: str = "simple"


class SummarizeResponse(BaseModel):
    summary: str


class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1)
    target_language: str = Field(..., min_length=2)


class TranslateResponse(BaseModel):
    translation: str


class TitleRequest(BaseModel):
    text: str = Field(..., min_length=10)
    count: int = Field(default=5, ge=1, le=10)


class TitleResponse(BaseModel):
    titles: str


class ExplainCodeRequest(BaseModel):
    code: str = Field(..., min_length=5)
    language: str = "auto-detect"


class ExplainCodeResponse(BaseModel):
    explaination: str
