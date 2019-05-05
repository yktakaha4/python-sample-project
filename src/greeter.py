
class Greeter:
    @staticmethod
    def greet(name: str):
        """挨拶を返す。

        Args:
            name [str]: 名前
        Returns:
            str: 英語の挨拶

        """

        return "Hello, {}.".format(name.upper())
