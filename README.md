# Spreadconnect Python SDK

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

A Python SDK for the [Spreadconnect API](https://api.spreadconnect.app/docs/),
developed by [SHOP4FANS](https://shop4fans.io).
This SDK provides a simple way to interact with the Spreadconnect REST API to manage
articles, orders, product types, stock levels, designs, and subscriptions.

> **Note:** This SDK is **not an official product** of Spreadconnect.
> Spreadconnect is operated by a third party:
> **Spreadconnect** – [Website](https://www.spreadshop.com/spreadconnect) – business@spreadconnect.app
> Terms of Service: [View here](https://faq.spod.com/hc/en-us/articles/360020630280)

---

## 📦 Installation

```bash
pip install spreadconnect-python-sdk
```

---

## 🚀 Quick Start

### 1. Import & Initialize

```python
from spreadconnect_python_sdk import Spreadconnect

spreadconnect = Spreadconnect(
    base_url="https://api.spreadconnect.app",  # or staging: https://api.spreadconnect-staging.app
    token="YOUR_API_TOKEN",
)
```

---

### 2. Example: List Subscriptions

```python
subs = spreadconnect.subscriptions.list()
for s in subs.__root__:
    print(s.id, s.event_type, s.url)
```

---

### 3. Example: List Articles

```python
articles = spreadconnect.articles.list(limit=10)
for art in articles.items or []:
    print(art.title, art.id)
```

---

## 📚 Supported API Modules

The SDK wraps the main Spreadconnect API endpoints:

| API Module        | Class               | Example Call                                   |
| ----------------- | ------------------- | ---------------------------------------------- |
| **Articles**      | `ArticlesApi`       | `spreadconnect.articles.list(limit=10)`        |
| **Orders**        | `OrdersApi`         | `spreadconnect.orders.get(order_id)`           |
| **Subscriptions** | `SubscriptionsApi`  | `spreadconnect.subscriptions.create({...})`    |
| **Product Types** | `ProductTypesApi`   | `spreadconnect.product_types.list()`           |
| **Stocks**        | `StocksApi`         | `spreadconnect.stocks.list()`                  |
| **Designs**       | `DesignsApi`        | `spreadconnect.designs.upload(...)`            |

---

## 🔗 Useful Links

- **Official Spreadconnect API Documentation:**
  [https://api.spreadconnect.app/docs/](https://api.spreadconnect.app/docs/)

- **Spreadconnect Website:**
  [https://www.spreadshop.com/spreadconnect](https://www.spreadshop.com/spreadconnect)

- **SHOP4FANS Website:**
  [https://shop4fans.io](https://shop4fans.io)

---

## 📄 License

This project is licensed under the **Apache 2.0 License** – see [LICENSE](LICENSE) for details.
