class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("(al)","al").replace("()","o")
        return command