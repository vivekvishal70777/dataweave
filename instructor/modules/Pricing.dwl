%dw 2.0

/**
 * Sample reusable module for Section 11 (Q46).
 * Save as src/main/resources/modules/Pricing.dwl in a Mule app.
 * Import: import withTax from modules::Pricing
 */
fun withTax(amount: Number, rate: Number = 0.18) = amount * (1 + rate)

fun money(n: Number) = n as String {format: "0.00"} as Number
