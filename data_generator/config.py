from dataclasses import dataclass
from pulsar.schema import Record, Integer


@dataclass
class PulsarConfig:
    topic_name: str
    producer_name: str
    pulsar_url: str


pulsar_config = PulsarConfig(
    topic_name="data-source-topic",
    producer_name="synthetic-producer",
    pulsar_url="pulsar://localhost:6650"
)


class DataSourceTopicSchema(Record):
    company_id: Integer()
    product_id: Integer()
    sold_time: Integer()  # Pulsar doesn't have Datetime as type. Using Unix datetime instead
    salesperson_id: Integer()
