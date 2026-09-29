class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        str_joined = "".join(strs)
        code = ""
        for element in strs:
            code = code + f"{len(element)},"
        identifier = len(code) - 1

        return str_joined + code + str(identifier)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        identifier = ""
        for i in range(len(s)-1, 0, -1):
            if s[i] == ",":
                break
            identifier = s[i] + identifier
        s = s[:-(len(identifier)+1)]
        identifier = int(identifier) if identifier != "" else 0

        s_original = s[:-identifier]
        code = s[-identifier:]

        lengths = [int(x) for x in code.split(",")]

        result = []
        for length in lengths:
            word = s_original[:length]
            s_original = s_original[length:]
            result.append(word)

        return result