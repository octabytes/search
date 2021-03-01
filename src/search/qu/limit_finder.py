from .alpha_numbers import numeric_words


class LimitFinder:
    def __init__(self, tokens, filters_intent):
        self.tokens = tokens
        self.filters_intent = filters_intent
        self.score = 0

    def intent(self):
        direction = "start"
        limit_index = None

        # if there is "first" word before or after number
        for index, token in enumerate(self.tokens):
            if (token == "first" and
                (self.tokens[index + 1].isnumeric() or
                         self.tokens[index + 1] in numeric_words)
                ):
                # This is the limit e.g first 5 ayahs
                limit_index = index + 1
                direction = "start"
                # calculate confidence
                self.score += 5

            elif (token == "last" and
                    (self.tokens[index + 1].isnumeric() or
                     self.tokens[index + 1] in numeric_words)
                  ):
                # This is the limit e.g last 5 ayahs
                limit_index = index + 1
                direction = "end"
                # calculate confidence
                self.score += 5

        # if any limit index found
        if limit_index:
            # Get filter intent
            limit_intent = next((
                filter_intent for filter_intent in self.filters_intent
                if filter_intent["number_index"] == limit_index), None)

            if limit_intent:
                limit_intent["direction"] = direction

            return limit_intent

        return None
