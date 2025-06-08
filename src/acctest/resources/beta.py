# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import beta_create_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.beta_create_completion_response import BetaCreateCompletionResponse

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/acctest-python#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/acctest-python#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        echo: bool,
        frequency_penalty: int,
        logprobs: int,
        max_tokens: int,
        model: str,
        presence_penalty: int,
        prompt: str,
        stop: None,
        stream: bool,
        stream_options: None,
        suffix: None,
        temperature: int,
        top_p: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaCreateCompletionResponse:
        """The FIM (Fill-In-the-Middle) Completion API.

        User must set
        `base_url="https://api.deepseek.com/beta"` to use this feature.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/beta/completions",
            body=maybe_transform(
                {
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "model": model,
                    "presence_penalty": presence_penalty,
                    "prompt": prompt,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "suffix": suffix,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                beta_create_completion_params.BetaCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaCreateCompletionResponse,
        )


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/acctest-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/acctest-python#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        echo: bool,
        frequency_penalty: int,
        logprobs: int,
        max_tokens: int,
        model: str,
        presence_penalty: int,
        prompt: str,
        stop: None,
        stream: bool,
        stream_options: None,
        suffix: None,
        temperature: int,
        top_p: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaCreateCompletionResponse:
        """The FIM (Fill-In-the-Middle) Completion API.

        User must set
        `base_url="https://api.deepseek.com/beta"` to use this feature.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/beta/completions",
            body=await async_maybe_transform(
                {
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "model": model,
                    "presence_penalty": presence_penalty,
                    "prompt": prompt,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "suffix": suffix,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                beta_create_completion_params.BetaCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaCreateCompletionResponse,
        )


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.create_completion = to_raw_response_wrapper(
            beta.create_completion,
        )


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.create_completion = async_to_raw_response_wrapper(
            beta.create_completion,
        )


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.create_completion = to_streamed_response_wrapper(
            beta.create_completion,
        )


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.create_completion = async_to_streamed_response_wrapper(
            beta.create_completion,
        )
