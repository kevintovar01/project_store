

def import_total_car(request):
    total = 0
    print('car' in request.session)
    print(request.session.items())
    if 'car' in request.session:
        for key, value in request.session['car'].items():
            total = total + (float(value['price']))
            
    return {'import_total_car':total}