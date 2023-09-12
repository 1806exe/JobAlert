import pytest
from datetime import datetime
from src.main import scrape_ajirayako  # Import the function from your module

@pytest.mark.parametrize("test_url", ["https://ajirayako.co.tz/"])  # Test with different URLs
def test_scrape_ajirayako(tmpdir, test_url):
    # Set up a temporary directory for testing
    tmp_dir = tmpdir.mkdir("test_folder")

    # Change working directory to the temporary directory
    with tmp_dir.as_cwd():
        scrape_ajirayako(test_url)

        # Verify that the file is created
        times = datetime.now().strftime("%H%M")
        file_name = f"ajirayako_{times}.txt"
        file_path = tmp_dir.join(file_name)
        assert file_path.exists()

        # You can add more assertions here to check the contents of the file or other aspects of the function's behavior

# Run the tests
if __name__ == "__main__":
    pytest.main()
