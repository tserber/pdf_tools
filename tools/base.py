import argparse


class BaseTool:
    name: str = ""
    description: str = ""

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser) -> None:
        raise NotImplementedError

    @classmethod
    def from_args(cls, args: argparse.Namespace) -> "BaseTool":
        raise NotImplementedError

    def run(self) -> int:
        raise NotImplementedError
