hadith_names = ["bukhari", "muslim", "tirmidhi",
                "abu_dawud", "nasai", "ibne_maja"]


class FilterFinder:
    def __init__(self, tokens, numbers, query_intents, caller):
        self.tokens = tokens
        self.numbers = numbers
        self.query_intents = query_intents
        self.caller = caller
        self.score = 0

    def intents(self):
        # Founded numbers intent
        filters_intent = []

        # Founded pre define filters
        pre_define_filters = []

        # Get Pre define filters
        for intent in self.query_intents:
            if intent["type"] == "pre_define_filter":
                pre_define_filters.append(intent)
                # Calculate confident
                self.score += 80

        # Find intent that are comming before numbers
        for number in self.numbers:
            for intent in self.query_intents:
                if intent["index"] == number["index"] - 1:
                    filter_intent = intent.copy()
                    filter_intent["number"] = number["number"]
                    filter_intent["number_index"] = number["index"]
                    filters_intent.append(filter_intent)
                    # Calculate confident
                    self.score += 70
                    break

        # if filters intent and number length is not same this
        # mean some numbers left and need to find the intents for them
        if len(filters_intent) != len(self.numbers):
            numbers_left = []
            for number in self.numbers:
                found = False
                for intent in filters_intent:

                    # Pass pre define filters
                    if intent["type"] == "pre_define_filter":
                        found = True
                        break

                    if number["index"] == intent["number_index"]:
                        found = True
                        break

                if not found:
                    numbers_left.append(number)

            # Find intent that are comming after numbers
            for number in self.numbers:
                for intent in self.query_intents:
                    if intent["index"] == number["index"] + 1:
                        filter_intent = intent.copy()
                        filter_intent["number"] = number["number"]
                        filter_intent["number_index"] = number["index"]
                        filters_intent.append(filter_intent)
                        # Calculate confident
                        self.score += 70
                        break

        return filters_intent + pre_define_filters

    def filters(self, filters_intent):

        filters = [{"name": filter_intent["name"], "number": filter_intent["number"]}
                   for filter_intent in filters_intent]

        # if caller is Hadith and there is any filter name is "bukhari" or something
        # then replace it with hadith_number e.g bukhari 123
        if self.caller == "hadith":
            new_filters = []
            for f in filters:
                if f["name"] in hadith_names:
                    new_filter = f.copy()
                    new_filter["name"] = "hadith_number"
                    new_filters.append(new_filter)

            if new_filters:
                filters = new_filters

        # If filters None then check if any token contain (:) or (-)
        if not filters and self.caller == "quran":
            for token in self.tokens:
                seperator = None

                if ":" in token:
                    seperator = ":"
                if "-" in token:
                    seperator = "-"

                if seperator:
                    parts = token.split(seperator)
                    # Consider first part is surah and second is ayah
                    try:
                        filters = [
                            {
                                "name": "surah",
                                "number": int(parts[0])
                            },
                            {
                                "name": "ayah",
                                "number": int(parts[1])
                            }
                        ]

                        # Calculate confident
                        self.score += 100
                    except ValueError:
                        pass

        return filters
