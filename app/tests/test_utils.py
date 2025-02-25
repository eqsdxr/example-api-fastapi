import pytest
from fastapi import UploadFile

from ..utils import calculate_sha256
from ..config import get_settings


@pytest.mark.anyio
async def test_calculate_sha256():
    with open(get_settings().test_static_dir / "test_img1.jpg", "rb") as f:
        file = UploadFile(f)
        img_hash = await calculate_sha256(file)
    assert isinstance(img_hash, str)
    assert (
        img_hash
        == "24b3a9e4b92d9f253b9510ed42e4d33a5ac39cdf3e96b53e8e3c4e7146ea5491"
    )
