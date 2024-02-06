import pytest
from assignment0.extract import extractincidents

def test_extractincidents():
    # Replace 'incident_data_sample' with actual incident data from a PDF
    incident_data_sample = b"Sample PDF Data"
    incidents = extractincidents(incident_data_sample)
    assert isinstance(incidents, list)
    assert len(incidents) > 0
    # Add more specific assertions based on the expected structure of incidents
