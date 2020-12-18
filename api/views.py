from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from lib import Calculator


class ApiView(View):
    """
    Simple Django View allowing access to `Calculator via the API`. Usually this would be done
    with `django-rest-framework` but it would be an overkill in this case.

    HOW TO USE:
    POST /api {expression=`..`          Calculate prefix expression notation.
    POST /api?infix?true {expression=`..`    Calculate infix expression notation.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ApiView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        expression = request.POST.get('expression', None)
        infix = request.GET.get('infix', False)

        if not expression:
            return JsonResponse({})

        calculator = Calculator()

        try:
            if infix:
                result = calculator.calculate(expression, infix=True)
            else:
                result = calculator.calculate(expression)
        except Exception as e:  # Broad exception but will do for this demo :)
            result = f'There was an error evaluating your expression: {e}'

        return JsonResponse({
            'expression': expression,
            'result': result
        })
