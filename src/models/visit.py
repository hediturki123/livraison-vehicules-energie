class Visit:
    def __init__(self, vi_id: int, label: str, demand: int):
        self.vi_id = vi_id
        self.label = label
        self.demand = demand

    @classmethod
    def from_csv_row(cls, visit_csv_row: dict[str, str]):
        return cls(
            int(visit_csv_row['visit_id']),
            visit_csv_row['visit_name'],
            int(visit_csv_row['demand'])
        )
