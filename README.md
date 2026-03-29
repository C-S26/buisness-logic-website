# Business Logic Vulnerability Lab

This project is a simple Flask-based web application built to demonstrate **business logic vulnerabilities**.

## Vulnerability

The server directly trusts user input for discount values.

* No validation on discount
* User can send large values
* Price becomes negative → item becomes free

## Example Exploit

* Original price: ₹1000
* Send discount: 2000
* Result: price = -1000 → item free

## What this shows

* Server-side validation is missing
* Client input should not be trusted
* Business logic flaws can lead to financial impact

## Tools Used

* Flask (for app)
* Manual testing / Burp Suite (for request manipulation)
