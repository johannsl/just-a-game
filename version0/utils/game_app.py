import kivy.app
import kivy.uix.dropdown
import kivy.uix.button
import kivy.base
import utils.game_widget

class JustAGameApp(kivy.app.App):

	
	def build(self):
		dropdown = kivy.uix.dropdown.DropDown()
		for i in range(5):
			button = kivy.uix.button.Button(text="lol", size_hint_y=None, 
											height=44)
			button.bind(on_release=lambda button: dropdown.select(button.text))
			dropdown.add_widget(button)
		mainbutton = kivy.uix.button.Button(text="lol", size_hint=(None, None))
		mainbutton.bind(on_release=dropdown.open)		
		dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 
															"text", x))
		kivy.base.runTouchApp(mainbutton)
		return utils.game_widget.JustAGame()
