import pandas as pd

from data_generator.synthetic_generator import SyntheticDataGenerator


class TestSyntheticDataGenerator:
    def test_init(self):
        """
        Test that the SyntheticDataGenerator class is initialized correctly with default and custom num_records values.
        """
        # Test with default num_records
        generator = SyntheticDataGenerator()
        assert generator.num_records == 10

        # Test with custom num_records
        generator = SyntheticDataGenerator(num_records=20)
        assert generator.num_records == 20

    def test_create_fieldset(self):
        """
        Test that the create_fieldset method returns a fieldset dictionary with the correct keys and values.
        """
        generator = SyntheticDataGenerator()
        fieldset = generator.create_fieldset()

        # Test that fieldset has the correct keys
        assert set(fieldset.keys()) == {'company_id', 'product_id', 'sold_time', 'salesperson_id'}

        # Test that fieldset values are correct types
        assert isinstance(fieldset['company_id'], list)
        assert isinstance(fieldset['product_id'], list)
        assert isinstance(fieldset['sold_time'], list)
        assert isinstance(fieldset['salesperson_id'], list)

        # Test that fieldset values have the correct lengths
        assert len(fieldset['company_id']) == 10
        assert len(fieldset['product_id']) == 10
        assert len(fieldset['sold_time']) == 10
        assert len(fieldset['salesperson_id']) == 10

    def test_generate_data(self):
        """
        Test that the generate_data method returns a pandas DataFrame with the correct columns and values.
        """
        generator = SyntheticDataGenerator()
        data = generator.generate_data()

        # Test that data is a pandas DataFrame
        assert isinstance(data, pd.DataFrame)

        # Test that data has the correct columns
        assert set(data.columns) == {'company_id', 'product_id', 'sold_time', 'salesperson_id'}

        # Test that data values have the correct lengths
        assert len(data['company_id']) == 10
        assert len(data['product_id']) == 10
        assert len(data['sold_time']) == 10
        assert len(data['salesperson_id']) == 10
