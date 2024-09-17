import pytest
import subprocess

def test_code_style():
    result = subprocess.run(['flake8', 'src/'], capture_output=True, text=True)
    assert result.returncode == 0, "Code style issues found"

def test_license_check():
    result = subprocess.run(['license-checker', '--json'], capture_output=True, text=True)
    assert 'MIT' in result.stdout, "Non-compliant licenses found"

if __name__ == "__main__":
    pytest.main()
