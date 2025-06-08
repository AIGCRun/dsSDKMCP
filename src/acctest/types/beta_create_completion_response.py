# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BetaCreateCompletionResponse", "Choice", "ChoiceLogprobs", "Usage", "UsageCompletionTokensDetails"]


class ChoiceLogprobs(BaseModel):
    text_offset: List[int]

    token_logprobs: List[int]

    tokens: List[str]

    top_logprobs: List[object]


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    logprobs: Optional[ChoiceLogprobs] = None

    text: Optional[str] = None


class UsageCompletionTokensDetails(BaseModel):
    reasoning_tokens: int


class Usage(BaseModel):
    completion_tokens: int

    completion_tokens_details: UsageCompletionTokensDetails

    prompt_cache_hit_tokens: int

    prompt_cache_miss_tokens: int

    prompt_tokens: int

    total_tokens: int


class BetaCreateCompletionResponse(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    object: str

    system_fingerprint: str

    usage: Usage
