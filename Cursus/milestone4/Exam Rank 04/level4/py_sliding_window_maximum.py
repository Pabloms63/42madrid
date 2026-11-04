def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []
    result = []
    dq = []
    head = 0
    for i in range(len(nums)):
        if head < len(dq) and dq[head] <= i - k:
            head += 1
        while len(dq) > head and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[head]])
    return result

def main() -> int:
    print(sliding_window_maximum([1, 2, 3, 4, 5], 2))


if __name__ == "__main__":
    main()