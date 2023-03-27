# Function to Calculate the Bond Duration as well as the Modified Duration
def bond_duration(face_value, coupon_rate, time_to_maturity, yield_rate, frequency):
    if frequency == 2:
        n = time_to_maturity * 2
        c = coupon_rate / 2
        y = yield_rate / 2
    elif frequency == 1:
        n = time_to_maturity
        c = coupon_rate
        y = yield_rate

    pv_sum = 0
    price = face_value * (1/(1+ y) ** n)
    cf_sum = 0
    year = 1
    for i in range(1, n+1):
        cf = face_value * c
        discount_factor = 1 / (1 + y) ** year
        cf_sum += cf * discount_factor
        pv_sum += cf * discount_factor * year
        year += 1
    cf_sum = price + cf_sum
    pv_sum = price * n + pv_sum
    if frequency == 2:
        mac_duration = (pv_sum / cf_sum) / 2
        mod_duration = mac_duration / (1 + y)
    elif frequency == 1:
        mac_duration = pv_sum / cf_sum
        mod_duration = mac_duration / (1 + y)
    return mac_duration, mod_duration


# Function that can handle multiple bonds and create

def bond_portfolio_duration(face_values, coupon_rates, time_to_maturities, yield_rates, frequencies):
    mac_durations = []
    mod_durations = []
    for i in range(len(face_values)):
        mac_duration, mod_duration = bond_duration(face_values[i], coupon_rates[i], time_to_maturities[i],
                                                   yield_rates[i], frequencies[i])
        mac_durations.append(mac_duration)
        mod_durations.append(mod_duration)

    # Calculate the weighted average duration of the portfolio
    total_face_value = sum(face_values)
    weighted_mac_duration = sum([face_values[i] * mac_durations[i] for i in range(len(face_values))]) / total_face_value
    weighted_mod_duration = sum([face_values[i] * mod_durations[i] for i in range(len(face_values))]) / total_face_value

    return weighted_mac_duration, weighted_mod_duration


# Sample Inputs for the Function

face_values = [1000, 2000, 3000]  # List of face values in USD
coupon_rates = [0.05, 0.04, 0.03]  # List of coupon rates as decimals
time_to_maturities = [10, 5, 7]  # List of years to maturity
yield_rates = [0.06, 0.05, 0.04]  # List of yield to maturity as decimals
frequencies = [2, 2, 1]  # List of frequencies: 2 for semi-annual coupon payments, 1 for annual coupon payments


weighted_mac_duration, weighted_mod_duration = bond_portfolio_duration(face_values, coupon_rates, time_to_maturities,
                                                                       yield_rates, frequencies)

print("Weighted Macaulay Duration: {:.3f} years".format(weighted_mac_duration))
print("Weighted Modified Duration: {:.3f} years".format(weighted_mod_duration))

