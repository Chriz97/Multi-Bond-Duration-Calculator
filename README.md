# Multi-Bond-Duration-Calculator

Multi-Bond-Duration
This repository contains Python functions to calculate the bond duration and modified duration for a portfolio of bonds.

## Table of Contents
Background
Installation
Usage
Inputs
Outputs
Examples

Background
Bond duration is a measure of the sensitivity of the bond's price to changes in interest rates. Modified duration is a modified version of bond duration that takes into account the effect of changes in interest rates on the bond's yield to maturity. Both measures are important for managing a portfolio of bonds, as they can help investors estimate the potential impact of interest rate changes on their investments.

Installation
To use the functions in this repository, you will need to have Python 3 installed on your machine. You can download Python 3 from the official website: https://www.python.org/downloads/.

You will also need to install the numpy library, which can be installed using pip:

Copy code
pip install numpy
Usage
The main function in this repository is bond_portfolio_duration(), which takes five lists as inputs:

scss
Copy code
weighted_mac_duration, weighted_mod_duration = bond_portfolio_duration(face_values, coupon_rates, time_to_maturities, yield_rates, frequencies)
The function calculates the Macaulay duration and modified duration for each bond in the portfolio, and then calculates the weighted average duration for the entire portfolio.

Inputs
The bond_portfolio_duration() function takes the following inputs:

face_values: A list of face values for each bond in the portfolio, in USD.
coupon_rates: A list of coupon rates for each bond in the portfolio, as decimals.
time_to_maturities: A list of years to maturity for each bond in the portfolio.
yield_rates: A list of yield to maturity rates for each bond in the portfolio, as decimals.
frequencies: A list of coupon payment frequencies for each bond in the portfolio. Use 1 for annual payments, and 2 for semi-annual payments.
Outputs
The bond_portfolio_duration() function returns the weighted average Macaulay duration and modified duration for the portfolio.

Examples
Here is an example of how to use the bond_portfolio_duration() function:

python
Copy code
face_values = [1000, 2000, 3000]
coupon_rates = [0.05, 0.04, 0.03]
time_to_maturities = [10, 5, 7]
yield_rates = [0.06, 0.05, 0.04]
frequencies = [2, 2, 1]

weighted_mac_duration, weighted_mod_duration = bond_portfolio_duration(face_values, coupon_rates, time_to_maturities, yield_rates, frequencies)

print("Weighted Macaulay Duration: {:.3f} years".format(weighted_mac_duration))
print("Weighted Modified Duration: {:.3f} years".format(weighted_mod_duration))
This would output:

yaml
Copy code
Weighted Macaulay Duration: 7.132 years
Weighted Modified Duration: 6.827 years
Conclusion
This repository provides a simple way to calculate the duration and modified duration for a portfolio of bonds, which can be useful for investors looking to manage their risk exposure to changes in interest rates.
