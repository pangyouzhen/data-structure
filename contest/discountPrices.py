import re


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = []
        keep_val = (100 - discount) / 100
        for i in sentence.split(" "):
            val = re.match('^\$(\d+)$', i)
            if val:
                num = val.group(1)
                replace_num = float(num) * keep_val
                str_num = "$%.2f" % replace_num
                res.append(str_num)
            else:
                res.append(i)
        return " ".join(res)


if __name__ == "__main__":
    func = Solution().discountPrices
    sentence = "there are $1 $2 and 5$ candies in the shop"
    discount = 50
    print(func(sentence, discount))
