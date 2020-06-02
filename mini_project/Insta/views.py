from django.views. generic import TemplateView

class HelloWorld(TemplateView): #继承 templateview hello world is a templateview 
    template_name = 'test.html' # override template name 