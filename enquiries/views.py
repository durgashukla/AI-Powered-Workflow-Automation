
from django.shortcuts import render, redirect,get_object_or_404
from .forms import EnquiryForm, SuggestedResponseForm
from django.contrib.auth import login, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from .ai_service import analyze_enquiry
from django.db.models import Count
from django.db.models import Q

def submit_enquiry(request):

    if request.method == 'POST':

        form = EnquiryForm(request.POST)

        if form.is_valid():

            # Customer enquiry message
            message = form.cleaned_data['message']

            # Analyze enquiry using Groq AI
            analysis = analyze_enquiry(message)

            # Create enquiry object without saving
            enquiry = form.save(commit=False)

            # Save AI analysis in model fields
            enquiry.category = analysis['category']
            enquiry.budget = analysis['budget']
            enquiry.location = analysis['location']
            enquiry.priority = analysis['priority']
            enquiry.requirements = analysis['requirements']

            enquiry.missing_information = ', '.join(
                analysis['missing_information']
            )

            enquiry.ai_summary = analysis['ai_summary']
            enquiry.suggested_response = analysis['suggested_response']

            # Save everything in database
            enquiry.save()

            return render(
                request,
                'enquiries/enquiry_success.html'
            )

    else:
        form = EnquiryForm()

    return render(
        request,
        'enquiries/enquiry_form.html',
        {'form': form}
    )



def admin_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')

            form.add_error(None, 'Admin access only.')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'enquiries/admin_login.html',
        {'form': form}
    )


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Enquiry




@login_required
def admin_dashboard(request):

    if not request.user.is_staff:
        return HttpResponseForbidden("Admin access only.")

    # Dashboard par sirf New enquiries
    enquiries = Enquiry.objects.filter(
        status='new'
    ).order_by('-created_at')

    category_labels = dict(Enquiry.CATEGORY_CHOICES)

    category_data = Enquiry.objects.values(
        'category'
    ).annotate(
        total=Count('id')
    ).order_by('-total')

    category_distribution = [
        {
            'label': category_labels[item['category']],
            'total': item['total']
        }
        for item in category_data
    ]

    context = {
        'enquiries': enquiries,

        'total_enquiries': Enquiry.objects.count(),

        'new_enquiries': Enquiry.objects.filter(
            status='new'
        ).count(),

        'high_priority': Enquiry.objects.filter(priority='high',status__in=['new', 'in_progress']).count(),

        'in_progress': Enquiry.objects.filter(
            status='in_progress'
        ).count(),

        'converted': Enquiry.objects.filter(
            status='converted'
        ).count(),

        'category_distribution': category_distribution,

        'priority_distribution': 
        [
            {'label': 'Low','total': Enquiry.objects.filter(priority='low',status__in=['new', 'in_progress']).count()},
            {'label': 'Medium','total': Enquiry.objects.filter(priority='medium', status__in=['new', 'in_progress']).count()},
            {'label': 'High','total': Enquiry.objects.filter(priority='high',status__in=['new', 'in_progress']).count()},
        ],
    }

    return render(
        request,
        'enquiries/admin_dashboard.html',
        context
    )




@login_required
def enquiry_detail(request, enquiry_id):

    if not request.user.is_staff:
        return HttpResponseForbidden("Admin access only.")

    enquiry = get_object_or_404(
        Enquiry,
        id=enquiry_id
    )

    if request.method == 'POST':

        # Save edited AI response
        if 'save_response' in request.POST:

            response_form = SuggestedResponseForm(
                request.POST,
                instance=enquiry
            )

            if response_form.is_valid():
                response_form.save()

        # Update enquiry status
        elif 'status' in request.POST:

            new_status = request.POST.get('status')

            valid_statuses = [
                choice[0] for choice in Enquiry.STATUS_CHOICES
            ]

            if new_status in valid_statuses:
                enquiry.status = new_status
                enquiry.save()

        return redirect(
            'enquiry_detail',
            enquiry_id=enquiry.id
        )

    response_form = SuggestedResponseForm(
        instance=enquiry
    )

    return render(
        request,
        'enquiries/enquiry_detail.html',
        {
            'enquiry': enquiry,
            'response_form': response_form
        }
    )


@require_POST
def admin_logout(request):
    logout(request)
    return redirect('admin_login')



@login_required
def customer_enquiries(request):

    if not request.user.is_staff:
        return HttpResponseForbidden("Admin access only.")

    search_query = request.GET.get('search', '').strip()
    category = request.GET.get('category', '')
    priority = request.GET.get('priority', '')
    status = request.GET.get('status', '')

    enquiries = Enquiry.objects.all().order_by('-created_at')

    # Search by customer name, email or phone
    if search_query:
        enquiries = enquiries.filter(
            Q(customer_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone_number__icontains=search_query)
        )

    # Category filter
    if category:
        enquiries = enquiries.filter(category=category)

    # Priority filter
    if priority:
        enquiries = enquiries.filter(priority=priority)

    # Status filter
    if status:
        enquiries = enquiries.filter(status=status)

    context = {
        'enquiries': enquiries,
        'search_query': search_query,
        'selected_category': category,
        'selected_priority': priority,
        'selected_status': status,
        'categories': Enquiry.CATEGORY_CHOICES,
        'priorities': Enquiry.PRIORITY_CHOICES,
        'statuses': Enquiry.STATUS_CHOICES,
    }

    return render(
        request,
        'enquiries/customer_enquiries.html',
        context
    )
