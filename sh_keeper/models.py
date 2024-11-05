class Invoice:
    def __init__(
        self,
        amount: str,
        display_name: str,
        exchange_rate: str,
        invoice_id: int,
        recalculate_after: int,
        status: str,
        wallet: str,
    ):
        self.amount = amount
        self.display_name = display_name
        self.exchange_rate = exchange_rate
        self.invoice_id = invoice_id
        self.recalculate_after = recalculate_after
        self.status = status
        self.wallet = wallet

    @classmethod
    def from_dict(cls, data: dict) -> "Invoice":
        """
        Converts a dictionary (API response) into an Invoice object.

        Args:
            data (dict): The API response containing invoice information.

        Returns:
            Invoice: The Invoice object with the parsed data.
        """
        return cls(
            amount=data["amount"],
            display_name=data["display_name"],
            exchange_rate=data["exchange_rate"],
            invoice_id=data["id"],
            recalculate_after=data["recalculate_after"],
            status=data["status"],
            wallet=data["wallet"],
        )

    def __repr__(self):
        return (
            f"Invoice(id={self.invoice_id}, amount={self.amount}, display_name={self.display_name}, "
            f"status={self.status}, wallet={self.wallet})"
        )
