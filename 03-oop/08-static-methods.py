class Utils:

    @staticmethod
    def clean_text(text):
        return [item.strip() for item in text.split(",")]


raw_text = " mango , apple , banana , strawberry "
print(Utils.clean_text(raw_text))
