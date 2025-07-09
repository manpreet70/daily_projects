class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        Bucket / counting‑sort style solution.
        Time  : O(n)
        Space : O(n)   (buckets of size n + 1)
        """
        n = len(citations)
        # bucket[i] = how many papers have exactly i citations
        # bucket[n] = how many papers have ≥ n citations
        bucket = [0] * (n + 1)
        for c in citations:
            bucket[min(c, n)] += 1

        running = 0  # papers with ≥ current h
        for h in range(n, -1, -1):
            running += bucket[h]
            if running >= h:
                return h
        return 0  # fallback (spec guarantees we return earlier)

    # ------------------------------------------------------------
    # Alternative: O(n log n) solution using sorting
    # ------------------------------------------------------------
    def hIndex_sort(self, citations: list[int]) -> int:
        """
        Classic approach:
        1.  Sort citations in descending order.
        2.  Scan while citations[i] >= i + 1.
        Time  : O(n log n)   (due to sort)
        Space : O(1) extra   (in‑place sort)
        """
        citations.sort(reverse=True)
        for i, c in enumerate(citations, start=1):      # i is 1‑based paper count
            if c < i:
                return i - 1                            # last valid h
        return len(citations)                           # all papers satisfy the rule