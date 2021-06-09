import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols=1
        self.add_widget(Label(text= "What's your Favourite Movie?"))
        self.s_name=TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="What's the IMDB Rating?"))
        self.s_rating = TextInput()
        self.add_widget(self.s_rating)

        self.add_widget(Label(text="Tell us your own thoughts about the Movie"))
        self.s_review = TextInput()
        self.add_widget(self.s_review)

        self.press= Button(text= "Submit")
        self.press.bind(on_press= self.click_me)
        self.add_widget(self.press)
    def click_me(self, instance):
        print("My favourite Movie is "+ self.s_name.text)
        print("The IMDB rating of the Movie is " + self.s_rating.text)
        print("My experience: " + self.s_review.text)
        print("")



class parentApp(App):
    def build(self):
        return childApp()
if __name__== "__main__":
    parentApp().run()