from omnicart_pipeline.data_enricher import DataEnricher
import pandas as pd
import pytest


@pytest.fixture
def sample_products():
    return [
  {
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "rating": { "rate": 3.9, "count": 120 }
  },
  {
    "id": 2,
    "title": "Mens Casual Premium Slim Fit T-Shirts ",
    "price": 22.3,
    "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
    "rating": { "rate": 4.1, "count": 259 }
  },
  {
    "id": 3,
    "title": "Mens Cotton Jacket",
    "price": 55.99,
    "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
    "rating": { "rate": 4.7, "count": 500 }
  }]

@pytest.fixture
def sample_users():
    return [
  {
    "address": {
      "geolocation": { "lat": "-37.3159", "long": "81.1496" },
      "city": "kilcoole",
      "street": "new road",
      "number": 7682,
      "zipcode": "12926-3874"
    },
    "id": 1,
    "email": "john@gmail.com",
    "username": "johnd",
    "password": "m38rmF$",
    "name": { "firstname": "john", "lastname": "doe" },
    "phone": "1-570-236-7033",
    "__v": 0
  },
  {
    "address": {
      "geolocation": { "lat": "-37.3159", "long": "81.1496" },
      "city": "kilcoole",
      "street": "Lovers Ln",
      "number": 7267,
      "zipcode": "12926-3874"
    },
    "id": 2,
    "email": "morrison@gmail.com",
    "username": "mor_2314",
    "password": "83r5^_",
    "name": { "firstname": "david", "lastname": "morrison" },
    "phone": "1-570-236-7033",
    "__v": 0
  },
  {
    "address": {
      "geolocation": { "lat": "40.3467", "long": "-30.1310" },
      "city": "Cullman",
      "street": "Frances Ct",
      "number": 86,
      "zipcode": "29567-1452"
    },
    "id": 3,
    "email": "kevin@gmail.com",
    "username": "kevinryan",
    "password": "kev02937@",
    "name": { "firstname": "kevin", "lastname": "ryan" },
    "phone": "1-567-094-1345",
    "__v": 0
  },
  {
    "address": {
      "geolocation": { "lat": "50.3467", "long": "-20.1310" },
      "city": "San Antonio",
      "street": "Hunters Creek Dr",
      "number": 6454,
      "zipcode": "98234-1734"
    },
    "id": 4,
    "email": "don@gmail.com",
    "username": "donero",
    "password": "ewedon",
    "name": { "firstname": "don", "lastname": "romer" },
    "phone": "1-765-789-6734",
    "__v": 0
  }]

def test_data_enricher(sample_products, sample_users):
    enricher = DataEnricher(products=sample_products, users=sample_users)
    enriched_df = enricher.enrich_data()
    
    # Check if the enriched DataFrame has the expected columns
    expected_columns = ['id', 'name', 'username', 'email', 'price', 'description', 'category', 'rate', 'count', 'revenue']
    assert list(enriched_df.columns) == expected_columns
    
    # Check if the number of rows in the enriched DataFrame is correct
    assert len(enriched_df) == 3  # Only 3 products have matching user IDs in this test case
    
    # Check if revenue is calculated correctly for a sample row
    sample_row = enriched_df.iloc[0]
    expected_revenue = sample_row['rate'] * sample_row['count']
    assert sample_row['revenue'] == expected_revenue