class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        lower_char = False
        upper_char = False
        digits = False
        other = False
        pre = None
        for i in password:
            if i.islower():
                lower_char = True
            elif i.isupper():
                upper_char = True
            elif i.isdigit():
                digits =True
            else:
                if i in "!@#$%^&*()-+":
                    other = True
            if i != pre:
                pre = i
                continue
            else:
                return False
        return lower_char and upper_char and  digits and other