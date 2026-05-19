from pydantic import BaseModel


class RequestIssue(BaseModel):
    message: str | None = None

    def custom_message(self, msg: str):
        self.message = msg
        return self