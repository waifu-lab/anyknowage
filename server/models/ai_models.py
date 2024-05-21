import attr


@attr.s
class GPTModel:
    models = attr.ib(
        default=[
            "gpt-4",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0125",
            "gpt-4-turbo",
            "gpt-4o",
            "gpt-4-turbo-preview",
        ]
    )
    model = attr.ib(default=None)

    @model.validator
    def check_model(self, _, value):
        if value not in self.models:
            raise ValueError(f"{value} is not a valid model.")

    def __str__(self):
        return self.model
