
# SEPA Debit Response

## Structure

`SEPADebitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iban_last_chars` | `str` | Optional | The last characters of the IBAN used to pay.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `34`, *Pattern*: `[a-zA-Z0-9]{4}` |
| `account_holder_name` | `Any` | Optional | - |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | The portable international postal address. Maps to [AddressValidationMetadata](https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling form controls: the autocomplete attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute). |
| `authorization_details` | [`SEPADebitAuthorizationDetails`](../../doc/models/sepa-debit-authorization-details.md) | Optional | Authorization details. |

## Example (as JSON)

```json
{
  "iban_last_chars": "iban_last_chars4",
  "account_holder_name": {
    "key1": "val1",
    "key2": "val2"
  },
  "billing_address": {
    "address_line_1": "address_line_12",
    "address_line_2": "address_line_28",
    "admin_area_2": "admin_area_28",
    "admin_area_1": "admin_area_14",
    "postal_code": "postal_code0",
    "country_code": "country_code8"
  },
  "authorization_details": {
    "status": "NOT_SUPPORTED"
  }
}
```

