"""
How to use?
- Replace original_text with any text.
- Run `python generator.py`
- Copy the generated text from the terminal.

Sample usage in Javascript:
i18n.t("parents_slash_grandparents")?.default;

"""

original_text = "Grand Nephew/Niece"

if __name__ == '__main__':
  
    text = original_text.split(" ")
    key = []
    new_text = []

    for x in text:
        k = x\
            .replace("(", "")\
            .replace(")", "")\
            .replace(".", "_dot")\
            .replace("?", "_qm")\
            .replace(",", "_comma") \
            .replace("'", "") \
            .replace('"', "dquote") \
            .replace(":", "_col") \
            .replace(";", "_semicol") \
            .replace("/", "_slash_")
        key.append(k.lower())
        new_text.append(x.lower())

    new_key = "_".join(key)
    default = original_text
    lowercase = original_text.lower()
    uppercase = original_text.upper()
    title = original_text.title()
    capitalize = original_text.capitalize()

    print(
        """
        "%s": {
            "default": '%s',
            "lowercase": '%s',
            "uppercase": '%s',
            "title": '%s',
            "capitalize": '%s'
        },
        """ % (
            new_key,
            default,
            lowercase,
            uppercase,
            title,
            capitalize
        )
    )

    print(
        """
        "%s": {
            "default": "%s",
            "lowercase": "%s",
            "uppercase": "%s",
            "title": "%s",
            "capitalize": "%s"
        },
        """ % (
            new_key,
            default,
            lowercase,
            uppercase,
            title,
            capitalize
        )
    )
