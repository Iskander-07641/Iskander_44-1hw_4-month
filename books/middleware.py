from django.utils.deprecation import MiddlewareMixin


class SalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:

            user_level = getattr(request.user, 'user_level', 'junior')

            if user_level == 'junior':
                salary = 500
            elif user_level == 'middle':
                salary = 1000
            elif user_level == 'senior':
                salary = 3000
            else:
                salary = 0

            request.user.salary = salary  # Attach salary to user object
