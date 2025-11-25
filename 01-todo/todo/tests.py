from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo
from datetime import datetime, timedelta

class TodoModelTest(TestCase):
    """Test Todo model."""
    
    def setUp(self):
        self.todo = Todo.objects.create(
            title="Test TODO",
            description="Test description"
        )
    
    def test_todo_creation(self):
        """Test that a TODO can be created."""
        self.assertEqual(self.todo.title, "Test TODO")
        self.assertFalse(self.todo.is_resolved)
    
    def test_todo_string_representation(self):
        """Test TODO string representation."""
        self.assertEqual(str(self.todo), "Test TODO")
    
    def test_todo_with_due_date(self):
        """Test TODO with due date."""
        due_date = datetime.now() + timedelta(days=1)
        todo = Todo.objects.create(
            title="Test with due date",
            due_date=due_date
        )
        self.assertEqual(todo.due_date, due_date)
    
    def test_todo_resolved(self):
        """Test resolving a TODO."""
        self.todo.is_resolved = True
        self.todo.save()
        self.assertTrue(self.todo.is_resolved)


class TodoViewTest(TestCase):
    """Test Todo views."""
    
    def setUp(self):
        self.client = Client()
        self.todo = Todo.objects.create(title="Test TODO")
    
    def test_home_view(self):
        """Test home page displays TODOs."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test TODO")
    
    def test_create_todo_get(self):
        """Test create todo GET request."""
        response = self.client.get(reverse('create_todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_todo.html')
    
    def test_create_todo_post(self):
        """Test creating a TODO via POST."""
        response = self.client.post(reverse('create_todo'), {
            'title': 'New TODO',
            'description': 'New description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='New TODO').exists())
    
    def test_edit_todo_get(self):
        """Test edit todo GET request."""
        response = self.client.get(reverse('edit_todo', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_todo.html')
    
    def test_edit_todo_post(self):
        """Test editing a TODO via POST."""
        response = self.client.post(reverse('edit_todo', args=[self.todo.pk]), {
            'title': 'Updated TODO',
            'is_resolved': False
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated TODO')
    
    def test_delete_todo_get(self):
        """Test delete todo GET request."""
        response = self.client.get(reverse('delete_todo', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_todo.html')
    
    def test_delete_todo_post(self):
        """Test deleting a TODO via POST."""
        todo_id = self.todo.pk
        response = self.client.post(reverse('delete_todo', args=[todo_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(pk=todo_id).exists())
    
    def test_toggle_resolved(self):
        """Test toggling resolved status."""
        response = self.client.post(reverse('toggle_resolved', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_resolved)