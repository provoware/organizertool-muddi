import pytest
from organizertool.services.search import (
    search_filenames,
    search_text,
    list_filetypes,
    categorize_files,
)

@pytest.mark.asyncio
async def test_search_filenames(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hi")
    result = await search_filenames(str(tmp_path), "hello")
    assert str(file) in result

@pytest.mark.asyncio
async def test_search_text(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("hello world\nsecond line")
    result = await search_text(str(tmp_path), "world")
    assert result[str(file)] == [1]

@pytest.mark.asyncio
async def test_list_filetypes(tmp_path):
    pyf = tmp_path / "a.py"
    txtf = tmp_path / "b.txt"
    pyf.write_text("")
    txtf.write_text("")
    result = await list_filetypes(str(tmp_path), [".py"])
    assert str(pyf) in result and str(txtf) not in result

@pytest.mark.asyncio
async def test_categorize_files(tmp_path):
    img = tmp_path / "pic.jpg"
    img.write_text("")
    categories = await categorize_files(str(tmp_path))
    assert str(img) in categories["image"]
