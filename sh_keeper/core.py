import logging
from .api import ApiClient
from .exceptions import SHKeeperError
from .models import Invoice


class SHKeeper:
    def __init__(self, base_url, callback_url=None):
        self.base_url = base_url
        self.callback_url = callback_url
        self.client = ApiClient(self.base_url)

    async def get_crypto_currencies(self):
        """
        Fetches available cryptocurrencies from the API.
        Returns a tuple with two lists:
            - A list of crypto symbols (e.g., ["BTC", "ETH", "BNB"]).
            - A list of crypto display names (e.g., [{"display_name": "Bitcoin", "name": "BTC"}]).
        Raises SHKeeperError if the API call fails or returns an error status.
        """
        try:
            data = await self.client.get("","crypto")

            if data.get("status") != "success":
                raise SHKeeperError(
                    f"Failed to fetch cryptocurrencies: {data.get('status')}"
                )

            crypto = data.get("crypto", [])
            crypto_list = data.get("crypto_list", [])

            return crypto, crypto_list

        except SHKeeperError as e:
            logging.error(f"Error getting cryptocurrencies: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error getting cryptocurrencies: {e}")
            raise SHKeeperError(
                "Unexpected error occurred while fetching cryptocurrencies."
            )

    async def create_invoice(
        self, crypto_name, external_id, amount, api_key, fiat="USD", callback_url=None
    ):
        """
        Creates an invoice in SHKeeper.

        Parameters:
            - crypto_name (str): The name of the cryptocurrency (e.g., "BTC", "ETH-USDC").
            - external_id (str): The unique order ID or invoice ID from your store.
            - amount (str): The amount in fiat currency.
            - fiat (str): The fiat currency code (default: "USD").
            - callback_url (str): The URL to send notifications.

        Returns:
            - Invoice: The Invoice object containing the created invoice details.

        Raises:
            SHKeeperError: If the API call fails or returns an error.
        """

        callback_url = callback_url or self.callback_url
        request_data = {
            "external_id": external_id,
            "fiat": fiat,
            "amount": amount,
            "callback_url": callback_url,
        }

        try:
            response = await self.client.post(
                api_key, f"{crypto_name}/payment_request", data=request_data
            )
            if response.get("status") != "success":
                raise SHKeeperError(
                    f"Invoice creation failed: {response.get('status')}"
                )
            invoice = Invoice.from_dict(response)
            return invoice

        except SHKeeperError as e:
            logging.error(f"Error creating or updating invoice: {e}")
            raise

        except Exception as e:
            logging.error(f"Unexpected error creating or updating invoice: {e}")
            raise SHKeeperError(
                "Unexpected error occurred while creating/updating the invoice."
            )
