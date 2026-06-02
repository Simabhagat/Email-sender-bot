# template.py

OTP_TEMPLATE = """Subject: OTP request

Hi {name},

Your OTP for verification is: {otp}

This OTP will expire in 5 minutes.

If you did not request this, please ignore this email.

Thanks,
Your App Team
"""

WELCOME_TEMPLATE = """Subject: Registration Successfull
Hi {name},

Welcome to our platform! 🎉

We're excited to have you onboard.

You can now explore features and get started right away.

If you need any help, feel free to reach out.

Cheers,
Your App Team
"""

def render_otp_email(name, otp):
    return OTP_TEMPLATE.format(name=name, otp=otp)


def render_welcome_email(name):
    return WELCOME_TEMPLATE.format(name=name)