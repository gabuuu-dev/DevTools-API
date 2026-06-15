from fastapi import APIRouter
from urllib.parse import urlparse
import re
import json
import ipaddress

router = APIRouter(prefix="/validators", tags=["Validators"])

@router.get("/")
async def validators():
    return {"endpoints": ["email", "url", "json", "credit-card", "ip"]}

@router.post("/email")
async def validateEmail(email: str):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return {"valid": bool(re.fullmatch(pattern, email))}


@router.post("/url")
async def validateURL(url: str):
    try:
        result = urlparse(url)
        # A valid URL needs at least a scheme (http, https, etc)
        # and a netloc (the domain, like "example.com")
        return {"valid": all([result.scheme, result.netloc])}
    except ValueError:
        return {"valid": False}

@router.post("/credit-card")
async def validateCC(cc_number: str):
    # People often write card numbers with spaces or dashes
    # (e.g. "4532 0151 1283 0366"), so we strip those before validating
    cc_number = cc_number.replace(" ", "").replace("-", "")

    # If what's left isn't all digits, it can't be valid
    if not cc_number.isdigit():
        return {"valid": False, "reason": "The number must only contain digits, spaces, or dashes"}

    digits = [int(x) for x in cc_number]

    # Luhn's algorithm:
    # Starting from the second digit counting from the right,
    # and moving left in steps of two, we double each digit.
    #
    # range(len(digits) - 2, -1, -2) generates those indices:
    #   - starts at the second-to-last digit (len - 2)
    #   - ends at the first one (-1 is the exclusive limit, so it reaches 0)
    #   - steps backwards by 2
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2

        # If doubling the digit gives a result greater than 9 (e.g. 8*2=16),
        # we subtract 9. This is the same as adding the digits of the result
        # together (1 + 6 = 7), but subtracting 9 is a faster shortcut:
        # 16 - 9 = 7
        if digits[i] > 9:
            digits[i] -= 9

    # Add up all the digits (the doubled/adjusted ones plus the untouched ones)
    total_sum = sum(digits)

    # A valid card number always produces a total sum
    # that is a multiple of 10
    return {"valid": total_sum % 10 == 0}


@router.post("/json")
async def validateJSON(data: str):
    try:
        # json.loads tries to convert the string into a Python object.
        # If the text isn't valid JSON, it raises json.JSONDecodeError
        parsed = json.loads(data)
        return {"valid": True, "parsed": parsed}
    except json.JSONDecodeError as e:
        # str(e) gives us a message describing exactly what went wrong
        # and at what position in the text it happened
        return {"valid": False, "error": str(e)}


@router.get("/ip/{ip}")
async def validateIP(ip: str):
    try:
        # ipaddress.ip_address() accepts both IPv4 ("192.168.1.1")
        # and IPv6 ("::1"), and raises ValueError if the format is invalid
        address = ipaddress.ip_address(ip)
        return {
            "valid": True,
            "version": address.version,       # 4 or 6
            "is_private": address.is_private  # True if it's a local network IP
        }
    except ValueError:
        return {"valid": False}