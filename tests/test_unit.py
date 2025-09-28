from src.app import validate_patient

def test_validate_patient():
    assert validate_patient({"id": "1", "name": "A"}) is True 
    assert validate_patient({"id": "", "name": "A"}) is False
    assert validate_patient({"id": "1", "name": ""}) is False
    assert validate_patient({}) is False
