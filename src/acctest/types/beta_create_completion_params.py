# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BetaCreateCompletionParams"]


class BetaCreateCompletionParams(TypedDict, total=False):
    echo: Required[bool]

    frequency_penalty: Required[int]

    logprobs: Required[int]

    max_tokens: Required[int]

    model: Required[str]

    presence_penalty: Required[int]

    prompt: Required[str]

    stop: Required[None]

    stream: Required[bool]

    stream_options: Required[None]

    suffix: Required[None]

    temperature: Required[int]

    top_p: Required[int]
