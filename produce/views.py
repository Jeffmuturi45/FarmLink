from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produce
from .forms import ProduceForm


# All available produce — visible to buyers and farmers
def produce_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    produce = Produce.objects.filter(is_available=True)

    if query:
        produce = produce.filter(name__icontains=query)

    if category:
        produce = produce.filter(category=category)

    return render(request, 'produce/list.html', {
        'produce':    produce,
        'query':      query,
        'category':   category,
        'categories': Produce.CATEGORY_CHOICES,
    })


# Farmers post new produce
@login_required
def post_produce(request):
    if not request.user.is_farmer:
        messages.error(request, 'Only farmers can post produce.')
        return redirect('produce:list')

    if request.method == 'POST':
        form = ProduceForm(request.POST, request.FILES)
        if form.is_valid():
            produce = form.save(commit=False)
            produce.farmer = request.user
            produce.save()
            messages.success(request, f'"{produce.name}" posted successfully!')
            return redirect('dashboard:farmer')
    else:
        form = ProduceForm()

    return render(request, 'produce/post.html', {'form': form})


# Farmer deletes their own produce
@login_required
def delete_produce(request, pk):
    produce = get_object_or_404(Produce, pk=pk, farmer=request.user)
    produce.delete()
    messages.success(request, 'Produce removed successfully.')
    return redirect('dashboard:farmer')


# Farmer toggles availability
@login_required
def toggle_availability(request, pk):
    produce = get_object_or_404(Produce, pk=pk, farmer=request.user)
    produce.is_available = not produce.is_available
    produce.save()
    status = 'available' if produce.is_available else 'unavailable'
    messages.success(request, f'"{produce.name}" marked as {status}.')
    return redirect('dashboard:farmer')
