import pytest 

@pytest.mark.skip(reason="Фича в раработке")
def test_feature_in_development(self):
    ...


@pytest.mark.skip(reason="Фича")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...
    
    def test_feature_in_development_2(self):
        ...