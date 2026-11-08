import re

# Read the script with surrogate pairs and fix surrogates
with open(r"C:\Users\Ahamed Mihad\.gemini\antigravity\scratch\gridx\sync_prompt_to_index.py", "r", encoding="utf-8", errors="surrogatepass") as f:
    code = f.read()

# Replace the write part to use surrogatepass or fix surrogates
fix_code = code.replace(
    'f.write(html_content)',
    'f.write(html_content.encode("utf-16", "surrogatepass").decode("utf-16"))'
)

with open(r"C:\Users\Ahamed Mihad\.gemini\antigravity\scratch\gridx\sync_prompt_to_index.py", "w", encoding="utf-8", errors="surrogatepass") as f:
    f.write(fix_code)

print("Fixed surrogate encoding handling in sync script")
