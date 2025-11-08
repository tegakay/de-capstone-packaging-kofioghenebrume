from omnicart_pipeline.data_analyzer import DataAnalyzer
import pandas as pd
import pytest

@pytest.fixture
def sample_data():
    data = pd.DataFrame([
        {'username': 'user1', 'revenue': 100.0},
        {'username': 'user2', 'revenue': 150.5},
        {'username': 'user1', 'revenue': 200.75},
        {'username': 'user3', 'revenue': 300.0},
        {'username': 'user2', 'revenue': 50.25},
    ])
    return data

@pytest.fixture
def sample_results():
    return {
        'user1': {
            'total_revenue': 300.75,
            'product_count': 2,
            'average_product_price': 150.38
        },
        'user2': {
            'total_revenue': 200.75,
            'product_count': 2,
            'average_product_price': 100.38
        },
        'user3': {
            'total_revenue': 300.0,
            'product_count': 1,
            'average_product_price': 300.0
        }
    }

def test_analyze_data(sample_data,sample_results):
    analyzer = DataAnalyzer(sample_data)
    result = analyzer.analyze_data()
    
    expected_result = sample_results
    
    assert result == expected_result