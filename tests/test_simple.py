import pytest
import os
from proxy_check import check

@pytest.mark.skip
def test_env():
    assert os.getenv('PROXY')

@pytest.mark.asyncio
@pytest.mark.skip
async def test_base():
    works, _ =  await check('http://www.instagram.com')
    assert not works
    works, _ = await check(os.getenv('PROXY'))
    assert works
