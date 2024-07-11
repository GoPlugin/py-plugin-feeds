# Plugin Feeds : Python Package

## Install

```sh
pip install py-plugin-feeds
```

## Example to pull the price CIFI/USDT 

```python

from web3 import HTTPProvider, Web3
from py_plugin_feeds import get_token_price

def main():
    json_rpc_url = "https://rpc-amoy.polygon.technology"
    pair = "CIFI/USDT"
    web3 = Web3(HTTPProvider(json_rpc_url))
    web3.middleware_onion.clear()
    result= get_token_price(web3,pair,"latestAnswer")
    print("result:::",result)

if __name__ == "__main__":
    main()

```
