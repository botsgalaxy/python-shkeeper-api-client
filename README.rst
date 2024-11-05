==========================
Python SHKeeper API Client
==========================

A basic Python Async Client for interacting with the SHKeeper API to manage cryptocurrency invoices. 

This library is still under development and is intended for basic usage at the moment.

Features
--------
- Fetch available cryptocurrencies.
- Create and update cryptocurrency invoices.
- Supports integration with multiple cryptocurrencies and fiat currencies.
- Easy-to-use methods for interacting with the SHKeeper API.

Note: This library is still in development, and the API may change in future versions.

Installation
------------
You can install this package via pip (from source) by cloning the repository:

.. code-block:: bash
    git clone https://github.com/botsgalaxy/python-shkeeper-api-client.git
    cd shkeeper-python
    pip install .

Basic Usage
------------
Here is a very basic example of how to use the library:

.. code-block:: python
    from sh_keeper import SHKeeper, Invoice

    # Initialize the SHKeeper client
    base_url = "https://api.shkeeper.io/api/v1"  # The base URL for SHKeeper API
    callback_url = "http://your-callback-url.com"  # Where you receive update about payments
    sh_keeper = SHKeeper(base_url=base_url, callback_url=callback_url)

    # Fetch available cryptocurrencies
    crypto, crypto_list = await sh_keeper.get_crypto_currencies()
    print(crypto)  # List of cryptocurrency symbols
    print(crypto_list)  # List of cryptocurrency display names

    # Create an invoice
    invoice = await sh_keeper.create_invoice(
        crypto_name="ETH-USDC",
        external_id="order_123",
        amount="100",
        api_key="your_api_key",
        callback_url="http://example.com/callback"
    )

    # Access invoice details
    print(f"Invoice Amount: {invoice.amount}")
    print(f"Wallet Address: {invoice.wallet}")

Configuration
-------------
The SHKeeper client requires the following configuration:

- `base_url`: The base URL for the SHKeeper API (e.g., `https://api.shkeeper.io`).
- `api_key`: Your SHKeeper API key for authentication.
- `callback_url`: A URL that SHKeeper will use to send notifications about the created invoices.

You can provide the `callback_url` when initializing the `SHKeeper` class or pass it directly when creating an invoice.

Methods
-------
### SHKeeper.get_crypto_currencies()
Fetches the available cryptocurrencies from the SHKeeper API.

- **Returns**: A tuple containing two lists:
  - A list of cryptocurrency symbols (e.g., `["BTC", "ETH", "BNB"]`).
  - A list of cryptocurrency display names (e.g., `[{"display_name": "Bitcoin", "name": "BTC"}]`).

- **Raises**: `SHKeeperError` if the API call fails or returns an error.

### SHKeeper.create_invoice()
Creates an invoice for a specific cryptocurrency in SHKeeper.

- **Parameters**:
  - `crypto_name` (str): The name of the cryptocurrency (e.g., `"BTC"`, `"ETH-USDC"`).
  - `external_id` (str): The unique order ID or invoice ID from your store.
  - `amount` (str): The amount in fiat currency (e.g., `"100"`).
  - `api_key` (str): Your SHKeeper API key.
  - `fiat` (str): The fiat currency code (default: `"USD"`).
  - `callback_url` (str): The URL to send notifications (optional if set during initialization).

- **Returns**: An `Invoice` object containing the created invoice details.

- **Raises**: `SHKeeperError` if the API call fails or returns an error.

Contributing
------------
This project is open for contributions! If you'd like to help improve it, feel free to fork the repository and submit a pull request.

Issues
------
If you encounter any issues, feel free to open an issue on the GitHub repository.

Author Information
------------------
- **Author**: @BotsGalaxy
- **Telegram**: @primeakash 


Version: 0.1
