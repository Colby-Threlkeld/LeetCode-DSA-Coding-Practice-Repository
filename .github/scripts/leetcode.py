import os, requests, re, pathlib

USERNAME = os.getenv("LEETCODE_USERNAME", "<Cthrelkeld>")
README = pathlib.Path("README.md")

query = """
query userPublicProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile { ranking }
    submitStatsGlobal {
      acSubmissionNum { difficulty count submissions }
    }
  }
}
"""

resp = requests.post(
    "https://leetcode.com/graphql",
    json={"query": query, "variables": {"username": USERNAME}},
    headers={"Content-Type": "application/json"}
)
resp.raise_for_status()
data = resp.json()

u = data["data"]["matchedUser"]
ranking = u["profile"]["ranking"]
totals = {d["difficulty"]: d for d in u["submitStatsGlobal"]["acSubmissionNum"]}
total  = totals["All"]["count"]
easy   = totals["Easy"]["count"]
medium = totals["Medium"]["count"]
hard   = totals["Hard"]["count"]

block = (
    f"**Username:** [{USERNAME}](https://leetcode.com/{USERNAME}/)  \n"
    f"**Global Rank:** `{ranking}`  \n"
    f"**Solved:** `{total}` (Easy `{easy}` • Medium `{medium}` • Hard `{hard}`)"
)

text = README.read_text(encoding="utf-8")
new = re.sub(
    r"(<!-- LEETCODE:START -->)(.*?)(<!-- LEETCODE:END -->)",
    r"\1\n" + block + r"\n\3",
    text,
    flags=re.S
)
README.write_text(new, encoding="utf-8")
print("Updated README with LeetCode stats.")
