import pytest
import os
from proxy_check import check

def test_env():
    assert os.getenv('PROXY')

@pytest.mark.asyncio
async def test_base():
    works, _ =  await check('http://www.instagram.com')
    assert not works
    works, _ = await check(os.getenv('PROXY'))
    assert works
