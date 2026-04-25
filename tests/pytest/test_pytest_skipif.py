import pytest 

SYSTEM_VERSION = "v1.2.0"

@pytest.mark.skipif(
       SYSTEM_VERSION = "v1.3.0", #"v1.2.0" == "v1.3.0" -> False
       reason="Тест не может быть запущен на системе версии 1.3.0"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
       SYSTEM_VERSION = "v1.2.0", 
       reason="Тест не может быть запущен на системе версии 1.2.0" #SYSTEM_VERSION == "v1.2.0" -> False
)
def test_system_version_invalid():
    ...
