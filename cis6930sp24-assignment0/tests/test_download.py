import pytest
from assignment0.main import fetchincidents

def test_fetchincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-01_daily_incident_summary.pdf"
    incidents = fetchincidents(url)
    assert isinstance(incidents, bytes)
    assert len(incidents) > 0
