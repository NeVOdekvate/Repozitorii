class Lead:
    """Лид (потенциальный клиент)."""

    def __init__(self, name):
        self.name = name


NEW_NAME = "Иван"


def change_name(lead):
    lead.name = NEW_NAME


if __name__ == "__main__":
    lead1 = Lead("Пётр")
    print("До изменения:", lead1.name)

    change_name(lead1)
    print("После изменения:", lead1.name)
