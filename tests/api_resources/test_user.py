# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from acctest import Acctest, AsyncAcctest
from tests.utils import assert_matches_type
from acctest.types import UserRetrieveBalanceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_balance(self, client: Acctest) -> None:
        user = client.user.retrieve_balance()
        assert_matches_type(UserRetrieveBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_balance(self, client: Acctest) -> None:
        response = client.user.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: Acctest) -> None:
        with client.user.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveBalanceResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncAcctest) -> None:
        user = await async_client.user.retrieve_balance()
        assert_matches_type(UserRetrieveBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncAcctest) -> None:
        response = await async_client.user.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncAcctest) -> None:
        async with async_client.user.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveBalanceResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
