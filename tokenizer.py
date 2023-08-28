import re


def tokenizer(url):
    # Normalize to lowercase
    url = url.lower()

    # Extract domain and path using regular expressions
    domain = re.findall(r"(?P<domain>https?://\S+?/|www\.\S+?/|https?://\S+?$)", url)
    path = re.sub(r"https?://\S+?/|www\.\S+?/|https?://\S+?$", "", url)

    # Tokenize domain and path
    domain_tokens = re.findall(r"\w+", domain[0]) if domain else []
    path_tokens = re.findall(r"\w+", path)

    tokens = domain_tokens + path_tokens

    return tokens
