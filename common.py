from charms.reactive import BaseRequest, BaseResponse, Field


class ImportResponse(BaseResponse):
    success = Field('Whether or not the import succeeded')
    reason = Field('If failed, a description of why')

    @property
    def name(self):
        """
        The name given when the import was requested.
        """
        return self.request.name


class ImportRequest(BaseRequest):
    RESPONSE_CLASS = ImportResponse

    name = Field("""
                 Name of the dashboard to import. Informational only, so that
                 you can tell which dashboard request this was, e.g. to check
                 for success or failure.
                 """)

    dashboard = Field("""
                      Data structure defining the dashboard. Must be JSON
                      serializable.  (Note: This should *not* be pre-serialized
                      JSON.)
                      """)

    def respond(self, success, reason=None):
        """
        Acknowledge this request, and indicate success or failure with an
        optional explanation.
        """
        super().respond(success=success, reason=reason)
