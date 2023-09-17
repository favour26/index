import random

# Define the length of the OTP
otp_length = 6  # You can adjust this to your desired OTP length

# Generate OTP
otp = ''.join(random.choice('0123456789') for _ in range(otp_length))

print(f'Your OTP is: {otp}')
