from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ticket.models import Ticket

User = get_user_model()

@login_required
def dashboard(request):
    if request.user.is_customer:
        tickets = Ticket.objects.filter(customer=request.user).count()
        active_tickets = Ticket.objects.filter(customer=request.user, is_resolved=False).count()
        closed_tickets = Ticket.objects.filter(customer=request.user, is_resolved=True).count()
        active_tickets_list = Ticket.objects.filter(customer=request.user, is_resolved=False)
        resolved_tickets_list = Ticket.objects.filter(customer=request.user, is_resolved=True)
        context = {
            'tickets': tickets,
            'active_tickets': active_tickets,
            'closed_tickets': closed_tickets,
            'active_tickets_list': active_tickets_list,
            'resolved_tickets_list': resolved_tickets_list,
        }
        return render(request, 'dashboard/customer_dashboard.html', context)
    
    elif request.user.is_engineer:
        tickets = Ticket.objects.filter(engineer=request.user).count()
        active_tickets = Ticket.objects.filter(engineer=request.user, is_resolved=False).count()
        closed_tickets = Ticket.objects.filter(engineer=request.user, is_resolved=True).count()
        active_tickets_list = Ticket.objects.filter(engineer=request.user, is_resolved=False)
        resolved_tickets_list = Ticket.objects.filter(engineer=request.user, is_resolved=True)
        context = {
            'tickets': tickets,
            'active_tickets': active_tickets,
            'closed_tickets': closed_tickets,
            'active_tickets_list': active_tickets_list,
            'resolved_tickets_list': resolved_tickets_list,
        }
        return render(request, 'dashboard/engineer_dashboard.html', context)
    
    elif request.user.is_superuser:
        total_tickets = Ticket.objects.all().count()
        resolved_tickets = Ticket.objects.filter(is_resolved=True).count()
        unresolved_tickets = Ticket.objects.filter(is_resolved=False).count()
        active_tickets_list = Ticket.objects.filter(is_resolved=False)
        resolved_tickets_list = Ticket.objects.filter(is_resolved=True)
        
        engineers = User.objects.filter(is_engineer=True)
        engineer_tickets = []
        for engineer in engineers:
            active_tickets = Ticket.objects.filter(engineer=engineer, is_resolved=False).count()
            resolved_tickets = Ticket.objects.filter(engineer=engineer, is_resolved=True).count()
            engineer_tickets.append({
                'name': engineer.email,
                'active_tickets': active_tickets,
                'resolved_tickets': resolved_tickets
            })
        
        customers = User.objects.filter(is_customer=True)
        customer_tickets = []
        for customer in customers:
            active_tickets = Ticket.objects.filter(customer=customer, is_resolved=False).count()
            resolved_tickets = Ticket.objects.filter(customer=customer, is_resolved=True).count()
            customer_tickets.append({
                'name': customer.email,
                'active_tickets': active_tickets,
                'resolved_tickets': resolved_tickets
            })

        context = {
            'total_tickets': total_tickets,
            'resolved_tickets': resolved_tickets,
            'unresolved_tickets': unresolved_tickets,
            'active_tickets_list': active_tickets_list,
            'resolved_tickets_list': resolved_tickets_list,
            'engineer_tickets': engineer_tickets,
            'customer_tickets': customer_tickets,
        }
        return render(request, 'dashboard/admin_dashboard.html', context)
