import pandas as pd
from infixpy import *
from mimesis import Locale
from mimesis.schema import Fieldset


class SyntheticDataGenerator:
    def __init__(self, num_records: int = 10):
        """
        Initializes an instance of the SyntheticDataGenerator class.

        Args:
            num_records (int): The number of records to generate. Default is 10.
        """
        self.fieldset = Fieldset(locale=Locale.EN, i=num_records)
        self.num_records = num_records

    def create_fieldset(self):
        """
        Creates and returns a fieldset dictionary representing the schema for the synthetic data.

        Returns:
            dict: The fieldset dictionary representing the schema for the synthetic data.
        """
        def list_of_random_ids(since: int, to: int) -> IList:
            """
            Generates a list of random IDs within the specified range. There is a conversion
            of types from float to int on the results

            Args:
                since (int): The minimum ID value.
                to (int): The maximum ID value.

            Returns:
                IList: The list of random IDs.
            """
            return Seq(self.fieldset("random.uniform", a=since, b=to, precision=0)).map(int).tolist()

        return {
            'company_id': list_of_random_ids(since=1, to=1000),
            'product_id': list_of_random_ids(since=1001, to=2000),
            'sold_time': self.fieldset("datetime.datetime", start=2020, end=2023),
            'salesperson_id': list_of_random_ids(since=7000, to=1000)
        }

    def generate_data(self):
        return pd.DataFrame.from_records(self.create_fieldset())
