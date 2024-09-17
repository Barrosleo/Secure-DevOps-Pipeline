import pytest
import subprocess

def test_sast():
    result = subprocess.run(['bandit', '-r', 'src/'], capture_output=True, text=True)
    assert 'No issues identified' in result.stdout, "SAST issues found"

def test_dependency_check():
    result = subprocess.run(['safety', 'check'], capture_output=True, text=True)
    assert 'No known security vulnerabilities found' in result.stdout, "Dependency vulnerabilities found"

if __name__ == "__main__":
    pytest.main()
