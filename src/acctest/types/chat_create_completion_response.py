# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "ChatCreateCompletionResponse",
    "Choice",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceMessage",
    "ChoiceMessageToolCall",
    "ChoiceMessageToolCallFunction",
    "Usage",
    "UsageCompletionTokensDetails",
]


class ChoiceLogprobsContentTopLogprob(BaseModel):
    token: Optional[str] = None

    bytes: Optional[List[int]] = None

    logprob: Optional[int] = None


class ChoiceLogprobsContent(BaseModel):
    token: Optional[str] = None

    bytes: Optional[List[int]] = None

    logprob: Optional[int] = None

    top_logprobs: Optional[List[ChoiceLogprobsContentTopLogprob]] = None


class ChoiceLogprobs(BaseModel):
    content: List[ChoiceLogprobsContent]


class ChoiceMessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class ChoiceMessageToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ChoiceMessageToolCallFunction] = None

    type: Optional[str] = None


class ChoiceMessage(BaseModel):
    content: str

    reasoning_content: str

    role: str

    tool_calls: List[ChoiceMessageToolCall]


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    logprobs: Optional[ChoiceLogprobs] = None

    message: Optional[ChoiceMessage] = None


class UsageCompletionTokensDetails(BaseModel):
    reasoning_tokens: int


class Usage(BaseModel):
    completion_tokens: int

    completion_tokens_details: UsageCompletionTokensDetails

    prompt_cache_hit_tokens: int

    prompt_cache_miss_tokens: int

    prompt_tokens: int

    total_tokens: int


class ChatCreateCompletionResponse(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    object: str

    system_fingerprint: str

    usage: Usage
