from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def calculate(request):
    if request.method == "POST":
        first_num = request.POST.get("first_num")
        second_num = request.POST.get("second_num")
        operators = request.POST.get("operators")

        if first_num and second_num:
            try:
                if operators == "add":
                    result = float(first_num) + float(second_num)
                elif operators == "subtract":
                    result = float(first_num) - float(second_num)
                elif operators == "multiply":
                    result = float(first_num) * float(second_num)
                elif operators == "divide":
                    result = float(first_num) / float(second_num) if float(second_num) != 0 else "Error: Division by zero"
                else:
                    result = "Invalid operator"

            except ValueError:
                result = "Invalid input"
        else:
            result = "Missing input values"

        return render(request, 'calculator.html', {'result': result})

   
    return render(request, 'calculator.html', {'result': None})