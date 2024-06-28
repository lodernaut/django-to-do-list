from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from todoAPP.forms import ToDoItemForm

from .models import ToDoItem, ToDoList

# Create your views here.


class ListListView(ListView):
    model = ToDoList
    template_name = "todoAPP/pages/index.html"


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todoAPP/partials/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    template_name = "todoAPP/forms/todolist_form.html"
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context


class ItemCreate(CreateView):
    template_name = "todoAPP/forms/todoitem_form.html"

    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    template_name = "todoAPP/forms/todoitem_form.html"

    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemDelete(DeleteView):
    model = ToDoItem
    template_name = "todoAPP/partials/todoitem_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context


class ListDeletex(DeleteView):
    model = ToDoList
    template_name = "todoAPP/partials/todolist_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object
        return context


class ListDelete(DeleteView):
    model = ToDoList
    template_name = "todoAPP/partials/todolist_confirm_delete.html"

    # def get_success_url(self):
    #     return reverse_lazy("list", args=[self.kwargs["list_id"]])
    def get_success_url(self):
        return reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:  # Check if the object exists before accessing its attributes
            context["todo_list"] = self.object
        return context
