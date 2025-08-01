from prompt_toolkit import prompt
from prompt_toolkit.input import Input
from prompt_toolkit.output import Output

class DummyInput(Input):
    def fileno(self):
        return 0
    def read_keys(self):
        return []

class DummyOutput(Output):
    def write(self, data):
        pass
    def flush(self):
        pass

passkey = prompt("Enter the passkey for decryption: ", is_password=True, input=DummyInput(), output=DummyOutput())
