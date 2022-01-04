from rest_framework.filters import OrderingFilter


class CustomOrderingFilter(OrderingFilter):
    """ Custom Ordering Filter with field description """

    def get_schema_fields(self, view):

        check = hasattr(view, "ordering_fields")

        if check:
            fields = [f"`{field}`" for field in view.ordering_fields]
            reverse_fields = [f"`-{field}`" for field in view.ordering_fields]

            self.ordering_description = (
                f"Fields to use when ordering the results: {', '.join(fields)}. "
                f"To reverse the ordering of the results: {', '.join(reverse_fields)} "
            )

        return super().get_schema_fields(view)
