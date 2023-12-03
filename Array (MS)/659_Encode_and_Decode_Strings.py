class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded_string = ""

        for str in strs:
            length = len(str)
            encoded_string += length * '$' + ";" + str

        return encoded_string

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decoded_list = []
        copied = str
        start_idx = 0
        count = 0
        for c in str:
            if c == "$":
                count += 1
            elif c == ";" and count != 0:
                copied = copied[count + 1:]
                decoded_list.append(copied[start_idx:count])
                copied = copied[count:]
                count = 0

        return decoded_list

if __name__ == "__main__":
    solution = Solution()
    password_list = ["lint","code","love","you"]
    encoded_string = solution.encode(password_list)
    print(encoded_string)
    decoded_list = solution.decode(encoded_string)
    print(decoded_list)