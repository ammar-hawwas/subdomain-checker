import requests
import argparse

def check_domain(domain):
    """
    يرسل طلب GET إلى النطاق المحدد باستخدام HTTPS ويطبع كود الاستجابة.
    إذا حدث خطأ، يطبع رسالة الخطأ.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(f"https://{domain}", headers=headers, timeout=20, verify=False)
        print(f"{domain}\t{response.status_code}\n\n")
    except requests.RequestException as e:
        print(f"{domain}\tError: {e}\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check HTTP status codes of subdomains.")
    parser.add_argument("file", help="Path to the file containing subdomains, one per line.")
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
        for domain in domains:
            check_domain(domain)
    except FileNotFoundError:
        print(f"File not found: {args.file}")