from __future__ import unicode_literals
from textwrap import dedent
from plyer import filechooser
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout
from kivy.base import runTouchApp
from kivy.lang import Builder
import moviepy.editor as mp
import pypandoc
from PIL import Image
from kivy.utils import rgba
from kivy.uix.scrollview import ScrollView 
from kivy.core.window import Window 
from kivy.app import runTouchApp
import docx2txt
from fpdf import FPDF
from plyer import notification
from pathlib import Path
import webbrowser
from kivy.uix.screenmanager import ScreenManager, Screen 



class MainWindow(Screen):
    class FileChoose(Button):
  
        selection = ListProperty([])

        # Opens specified link when button is pressed.
        def openLink(instnace):
            webbrowser.open('https://www.youtube.com')

        def choose(self):
            '''
            Call plyer filechooser API to run a filechooser Activity.
            '''
            filechooser.open_file(on_selection=self.handle_selection)

        def handle_selection(self, selection):
            '''
            Callback function for handling the selection response from Activity.
            '''
            self.selection = selection

        def on_selection(self, *a, **k):

            try:
                # This variable stores the path of the end users selected file
                # The slicing at the end is to take out the brackets on both ends so the path can be used with the conversion functions
                your_string = str(self.selection)[2:-2]


                # This function returns the filename.datatype when the full path is passed in as a parameter
                def slicing(file_location = your_string):
                    new_list = file_location.split("\\") 
                    your_file = new_list[-1]
                    return your_file

                # This function returns a string of everything in the path up to the datatype
                def slicing_thing(your_file_location):
                    index_of_dot = your_file_location.find('.')
                    dotmp4 = your_file_location[:index_of_dot]
                    return dotmp4


                if self.text == 'Gif to Mp4':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_videofile(slicing_thing(your_string) + ".mp4")
                    my_file = Path(slicing_thing(your_string) + ".mp4")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Gif':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_gif(slicing_thing(your_string) + ".gif")
                    my_file = Path(slicing_thing(your_string) + ".gif")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'HTML to Docx':
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp3 to Wav':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Wav to Mp3':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')
                 
                elif self.text == 'Md to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Wav':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Mp3':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Txt to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Txt':
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Epub to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "HTML to Txt":
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Md to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Txt to PDF":
                    f = open(your_string, "r")
                    x = f.read()

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial",size=30)
                    pdf.cell(200,100, txt = x, ln=1, align="C")
                    pdf.output(slicing_thing(your_string) + ".pdf") 
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                else:
                    print("Wrong file type!")

            except:
                print("Sorry we're having difficulties right now.")

            finally:
                print(slicing_thing(your_string))
                print(slicing(your_string))
class FirstWindow(Screen):
    class FileChoose(Button):
        '''
        Button that triggers 'filechooser.open_file()' and processes
        the data response from filechooser Activity.
        '''
        selection = ListProperty([])

        # Opens specified link when button is pressed.
        def openLink(instnace):
            webbrowser.open('https://www.youtube.com')

        def choose(self):
            '''
            Call plyer filechooser API to run a filechooser Activity.
            '''
            filechooser.open_file(on_selection=self.handle_selection)

        def handle_selection(self, selection):
            '''
            Callback function for handling the selection response from Activity.
            '''
            self.selection = selection

        def on_selection(self, *a, **k):

            try:
                # This variable stores the path of the end users selected file
                # The slicing at the end is to take out the brackets on both ends so the path can be used with the conversion functions
                your_string = str(self.selection)[2:-2]


                # This function returns the filename.datatype when the full path is passed in as a parameter
                def slicing(file_location = your_string):
                    new_list = file_location.split("\\") 
                    your_file = new_list[-1]
                    return your_file

                # This function returns a string of everything in the path up to the datatype
                def slicing_thing(your_file_location):
                    index_of_dot = your_file_location.find('.')
                    dotmp4 = your_file_location[:index_of_dot]
                    return dotmp4


                if self.text == 'Gif to Mp4':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_videofile(slicing_thing(your_string) + ".mp4")
                    my_file = Path(slicing_thing(your_string) + ".mp4")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Gif':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_gif(slicing_thing(your_string) + ".gif")
                    my_file = Path(slicing_thing(your_string) + ".gif")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'HTML to Docx':
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp3 to Wav':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Wav to Mp3':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')
                 
                elif self.text == 'Md to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Wav':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Mp3':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Txt to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Txt':
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Epub to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "HTML to Txt":
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Md to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Txt to PDF":
                    f = open(your_string, "r")
                    x = f.read()

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial",size=30)
                    pdf.cell(200,100, txt = x, ln=1, align="C")
                    pdf.output(slicing_thing(your_string) + ".pdf") 
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                else:
                    print("Wrong file type!")

            except:
                print("Sorry we're having difficulties right now.")

            finally:
                print(slicing_thing(your_string))
                print(slicing(your_string))
class SecondWindow(Screen):
    class FileChoose(Button):
        '''
        Button that triggers 'filechooser.open_file()' and processes
        the data response from filechooser Activity.
        '''
        selection = ListProperty([])

        # Opens specified link when button is pressed.
        def openLink(instnace):
            webbrowser.open('https://www.youtube.com')

        def choose(self):
            '''
            Call plyer filechooser API to run a filechooser Activity.
            '''
            filechooser.open_file(on_selection=self.handle_selection)

        def handle_selection(self, selection):
            '''
            Callback function for handling the selection response from Activity.
            '''
            self.selection = selection

        def on_selection(self, *a, **k):

            try:
                # This variable stores the path of the end users selected file
                # The slicing at the end is to take out the brackets on both ends so the path can be used with the conversion functions
                your_string = str(self.selection)[2:-2]


                # This function returns the filename.datatype when the full path is passed in as a parameter
                def slicing(file_location = your_string):
                    new_list = file_location.split("\\") 
                    your_file = new_list[-1]
                    return your_file

                # This function returns a string of everything in the path up to the datatype
                def slicing_thing(your_file_location):
                    index_of_dot = your_file_location.find('.')
                    dotmp4 = your_file_location[:index_of_dot]
                    return dotmp4


                if self.text == 'Gif to Mp4':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_videofile(slicing_thing(your_string) + ".mp4")
                    my_file = Path(slicing_thing(your_string) + ".mp4")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Gif':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_gif(slicing_thing(your_string) + ".gif")
                    my_file = Path(slicing_thing(your_string) + ".gif")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'HTML to Docx':
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp3 to Wav':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Wav to Mp3':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')
                 
                elif self.text == 'Md to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Wav':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Mp3':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Txt to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Txt':
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Epub to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "HTML to Txt":
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Md to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Txt to PDF":
                    f = open(your_string, "r")
                    x = f.read()

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial",size=30)
                    pdf.cell(200,100, txt = x, ln=1, align="C")
                    pdf.output(slicing_thing(your_string) + ".pdf") 
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                else:
                    print("Wrong file type!")

            except:
                print("Sorry we're having difficulties right now.")

            finally:
                print(slicing_thing(your_string))
                print(slicing(your_string))
class ThirdWindow(Screen):
    class FileChoose(Button):
        '''
        Button that triggers 'filechooser.open_file()' and processes
        the data response from filechooser Activity.
        '''
        selection = ListProperty([])

        # Opens specified link when button is pressed.
        def openLink(instnace):
            webbrowser.open('https://www.youtube.com')

        def choose(self):
            '''
            Call plyer filechooser API to run a filechooser Activity.
            '''
            filechooser.open_file(on_selection=self.handle_selection)

        def handle_selection(self, selection):
            '''
            Callback function for handling the selection response from Activity.
            '''
            self.selection = selection

        def on_selection(self, *a, **k):

            try:
                # This variable stores the path of the end users selected file
                # The slicing at the end is to take out the brackets on both ends so the path can be used with the conversion functions
                your_string = str(self.selection)[2:-2]


                # This function returns the filename.datatype when the full path is passed in as a parameter
                def slicing(file_location = your_string):
                    new_list = file_location.split("\\") 
                    your_file = new_list[-1]
                    return your_file

                # This function returns a string of everything in the path up to the datatype
                def slicing_thing(your_file_location):
                    index_of_dot = your_file_location.find('.')
                    dotmp4 = your_file_location[:index_of_dot]
                    return dotmp4


                if self.text == 'Gif to Mp4':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_videofile(slicing_thing(your_string) + ".mp4")
                    my_file = Path(slicing_thing(your_string) + ".mp4")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Gif':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_gif(slicing_thing(your_string) + ".gif")
                    my_file = Path(slicing_thing(your_string) + ".gif")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'HTML to Docx':
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp3 to Wav':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Wav to Mp3':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')
                 
                elif self.text == 'Md to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Wav':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Mp3':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Txt to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Txt':
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Epub to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "HTML to Txt":
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Md to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Txt to PDF":
                    f = open(your_string, "r")
                    x = f.read()

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial",size=30)
                    pdf.cell(200,100, txt = x, ln=1, align="C")
                    pdf.output(slicing_thing(your_string) + ".pdf") 
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                else:
                    print("Wrong file type!")

            except:
                print("Sorry we're having difficulties right now.")

            finally:
                print(slicing_thing(your_string))
                print(slicing(your_string))
class FourthWindow(Screen):
    class FileChoose(Button):
        '''
        Button that triggers 'filechooser.open_file()' and processes
        the data response from filechooser Activity.
        '''
        selection = ListProperty([])

        # Opens specified link when button is pressed.
        def openLink(instnace):
            webbrowser.open('https://www.youtube.com')

        def choose(self):
            '''
            Call plyer filechooser API to run a filechooser Activity.
            '''
            filechooser.open_file(on_selection=self.handle_selection)

        def handle_selection(self, selection):
            '''
            Callback function for handling the selection response from Activity.
            '''
            self.selection = selection

        def on_selection(self, *a, **k):

            try:
                # This variable stores the path of the end users selected file
                # The slicing at the end is to take out the brackets on both ends so the path can be used with the conversion functions
                your_string = str(self.selection)[2:-2]


                # This function returns the filename.datatype when the full path is passed in as a parameter
                def slicing(file_location = your_string):
                    new_list = file_location.split("\\") 
                    your_file = new_list[-1]
                    return your_file

                # This function returns a string of everything in the path up to the datatype
                def slicing_thing(your_file_location):
                    index_of_dot = your_file_location.find('.')
                    dotmp4 = your_file_location[:index_of_dot]
                    return dotmp4


                if self.text == 'Gif to Mp4':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_videofile(slicing_thing(your_string) + ".mp4")
                    my_file = Path(slicing_thing(your_string) + ".mp4")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Gif':
                    clip = mp.VideoFileClip(your_string)
                    clip.write_gif(slicing_thing(your_string) + ".gif")
                    my_file = Path(slicing_thing(your_string) + ".gif")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'HTML to Docx':
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp3 to Wav':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Wav to Mp3':
                    clip = mp.AudioFileClip(your_string)
                    clip.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to PNG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".png", 'PNG')
                    my_file = Path(slicing_thing(your_string) + ".png")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'PNG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')
                 
                elif self.text == 'Md to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Md':
                    output = pypandoc.convert_file(slicing(your_string), 'md', outputfile=slicing_thing(your_string) + ".md")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".md")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPG to JPEG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpeg", 'JPEG')
                    my_file = Path(slicing_thing(your_string) + ".jpeg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'JPEG to JPG':
                    image = Image.open(your_string)
                    image.save(slicing_thing(your_string) + ".jpg")
                    my_file = Path(slicing_thing(your_string) + ".jpg")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Wav':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".wav")
                    my_file = Path(slicing_thing(your_string) + ".wav")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Mp4 to Mp3':
                    clip = mp.VideoFileClip(your_string)
                    clip.audio.write_audiofile(slicing_thing(your_string) + ".mp3")
                    my_file = Path(slicing_thing(your_string) + ".mp3")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Epub':
                    output = pypandoc.convert_file(slicing(your_string), 'epub', outputfile=slicing_thing(your_string) + ".epub")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".epub")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to Docx':
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".docx")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Md to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Txt to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Epub to HTML':
                    output = pypandoc.convert_file(slicing(your_string), 'html', outputfile=slicing_thing(your_string) + ".html")
                    assert output == ""
                    my_file = Path(slicing_thing(your_string) + ".html")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == 'Docx to Txt':
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Epub to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "HTML to Txt":
                    conuot = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert conuot == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Md to Txt":
                    output = pypandoc.convert_file(slicing(your_string), 'docx', outputfile=slicing_thing(your_string) + ".docx")
                    assert output == ""
                    MY_TEXT = docx2txt.process(slicing_thing(your_string) + ".docx")
                    with open(slicing_thing(your_string) + ".txt", "w") as text_file:
                        print(MY_TEXT, file=text_file)
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                elif self.text == "Txt to PDF":
                    f = open(your_string, "r")
                    x = f.read()

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial",size=30)
                    pdf.cell(200,100, txt = x, ln=1, align="C")
                    pdf.output(slicing_thing(your_string) + ".pdf") 
                    my_file = Path(slicing_thing(your_string) + ".txt")
                    if my_file.is_file():
                        notification.notify(title='Easy Convert', message='Your File Is Ready')

                else:
                    print("Wrong file type!")

            except:
                print("Sorry we're having difficulties right now.")

            finally:
                print(slicing_thing(your_string))
                print(slicing(your_string))

class WindowManager(ScreenManager):
    pass

class ChooserApp(App):
  
    def build(self):
        return Builder.load_string(dedent('''

            WindowManager:
                MainWindow:
                    name: "main"
                FirstWindow:
                    name: "first"
                SecondWindow:
                    name: "second"
                ThirdWindow:
                    name: "third"
                FourthWindow:
                    name: "fourth"

            <MainWindow>:
                name: "main"

                GridLayout:           
                    cols: 1

                    canvas:
                        Color:
                            rgb: 1, 1, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
             
                    GridLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        row_default_height: 60
                        cols: 2
                        spacing: 0
                        padding: 0

                        canvas:
                            Color: 
                                rgb: .26, .26, .26, 1
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        Label:
                            text:"EasyConvert"
                            size_hint: .1, .07
                            font_size: 60
                            pos_hint: {"x": .1, "top": .9}
                        
                        FileChoose:
                            text: ''
                            size_hint_x: None
                            width: 200
                            size_hint_y: None
                            background_color: 0, 0, 0, 0
                            height: 120
                            on_press: self.openLink()
                            Image:
                                source: "transparent_q.png"
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y

                    GridLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        row_default_height: 60
                        cols: 2
                        spacing: 20
                        padding: 20

                        GridLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing: 20
                            padding: 20


                            Button:
                                color: 0, 0, 0, 1
                                text: 'Video'
                                font_size: 60
                                background_color: .5, .5, 1, 1
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 200
                                on_release: 
                                    app.root.current = "first"
                                    root.manager.transition.direction = "left"


                            Button:
                                color: 0, 0, 0, 1
                                text: 'Text'
                                font_size: 60
                                background_color: .5, .5, 1, 1
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 200
                                on_release: 
                                    app.root.current = "second"
                                    root.manager.transition.direction = "left"

                        GridLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing:20
                            padding:20

                            Button:
                                color: 0, 0, 0, 1
                                text: 'Developer'
                                font_size: 60
                                background_color: .5, .5, 1, 1
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 200
                                on_release: 
                                    app.root.current = "third"
                                    root.manager.transition.direction = "left"

                            Button:
                                color: 0, 0, 0, 1
                                text: 'Images'
                                font_size: 60
                                background_color: .5, .5, 1, 1
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 200
                                on_release: 
                                    app.root.current = "fourth"
                                    root.manager.transition.direction = "left"

            <FirstWindow>:
                orientation: 'horizontal'

                GridLayout:
                    cols: 1
                    spacing: 20
                    orientation: 'horizontal'

                    canvas:
                        Color: 
                            rgb: (1, 1, 1, 1)
                        Rectangle:
                            pos: self.pos
                            size: self.size
                
                    GridLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        row_default_height: 60
                        cols: 2
                        spacing: 0
                        padding: 0

                        canvas:
                            Color: 
                                rgb: .26, .26, .26, 1
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        Label:
                            text:"EasyConvert"
                            size_hint: .1, .07
                            font_size: 60
                            pos_hint: {"x": .1, "top": .9}
                    
                        Button:
                            text: ''
                            size_hint_x: None
                            width: 200
                            size_hint_y: None
                            background_color: 0, 0, 0, 0
                            height: 120
                            on_release: 
                                app.root.current = "main"
                                root.manager.transition.direction = "right"
                            Image:
                                source: "home.png"
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                    ScrollView:
              
                        GridLayout:
                            orientation: 'horizontal'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing: 20 
                            padding: 20

                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Gif to Mp4'
                               
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Mp4 to Gif'
                               
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Mp3 to Wav'
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Wav to Mp3'
                              
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Mp4 to Wav'
                                
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Mp4 to Mp3'

            <SecondWindow>:

                orientation: 'horizontal'

                GridLayout:
                    cols: 1
                    spacing: 20
                    orientation: 'horizontal'

                    canvas:
                        Color: 
                            rgb: (1, 1, 1, 1)
                        Rectangle:
                            pos: self.pos
                            size: self.size
                
                    GridLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        row_default_height: 60
                        cols: 2
                        spacing: 0
                        padding: 0

                        canvas:
                            Color: 
                                rgb: .26, .26, .26, 1
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        Label:
                            text:"EasyConvert"
                            size_hint: .1, .07
                            font_size: 60
                            pos_hint: {"x": .1, "top": .9}
                    
                        Button:
                            text: ''
                            size_hint_x: None
                            width: 200
                            size_hint_y: None
                            background_color: 0, 0, 0, 0
                            height: 120
                            on_release: 
                                app.root.current = "main"
                                root.manager.transition.direction = "right"
                            Image:
                                source: "home.png"
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                    ScrollView:
              
                        GridLayout:
                            orientation: 'horizontal'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing: 20 
                            padding: 20

                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Docx to Txt'

                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Txt to PDF'
                            


            <ThirdWindow>:
                orientation: 'horizontal'

                GridLayout:
                    cols: 1
                    spacing: 20
                    orientation: 'horizontal'

                    canvas:
                        Color: 
                            rgb: (1, 1, 1, 1)
                        Rectangle:
                            pos: self.pos
                            size: self.size
                
                    GridLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        row_default_height: 60
                        cols: 2
                        spacing: 0
                        padding: 0

                        canvas:
                            Color: 
                                rgb: .26, .26, .26, 1
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        Label:
                            text:"EasyConvert"
                            size_hint: .1, .07
                            font_size: 60
                            pos_hint: {"x": .1, "top": .9}
                    
                        Button:
                            text: ''
                            size_hint_x: None
                            width: 200
                            size_hint_y: None
                            background_color: 0, 0, 0, 0
                            height: 120
                            on_release: 
                                app.root.current = "main"
                                root.manager.transition.direction = "right"
                            Image:
                                source: "home.png"
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                    ScrollView:
              
                        GridLayout:
                            orientation: 'horizontal'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing: 20 
                            padding: 20

                            FileChoose:
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_color: .1, .5, .1, 1
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Md to Docx'
                         
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Docx to Md'
                              
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Md to Epub'
                               
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Epub to Md'
                               
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'HTML to Docx'
                               
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Docx to Epub'
                                
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Epub to Docx'
                               
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Docx to HTML'
                              
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Md to HTML'
                               
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Epub to HTML'
                              
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Epub to Txt'
                            
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'HTML to Txt'
                            
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Md to Txt'
                               
                            FileChoose:
                                background_color: .1, .5, .1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'Txt to HTML'

                        


            <FourthWindow>:

                orientation: 'horizontal'

                GridLayout:
                    cols: 1
                    spacing: 20
                    orientation: 'horizontal'

                    canvas:
                        Color: 
                            rgb: (1, 1, 1, 1)
                        Rectangle:
                            pos: self.pos
                            size: self.size
                
                    GridLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: self.minimum_height
                        row_default_height: 60
                        cols: 2
                        spacing: 0
                        padding: 0

                        canvas:
                            Color: 
                                rgb: .26, .26, .26, 1
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        Label:
                            text:"EasyConvert"
                            size_hint: .1, .07
                            font_size: 60
                            pos_hint: {"x": .1, "top": .9}
                    
                        Button:
                            text: ''
                            size_hint_x: None
                            width: 200
                            size_hint_y: None
                            background_color: 0, 0, 0, 0
                            height: 120
                            on_release: 
                                app.root.current = "main"
                                root.manager.transition.direction = "right"
                            Image:
                                source: "home.png"
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                    ScrollView:
              
                        GridLayout:
                            orientation: 'horizontal'
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height: 60
                            cols: 1
                            spacing: 20 
                            padding: 20

                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'JPEG to PNG'
                            
                              
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'PNG to JPEG'
                                
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'JPG to PNG'
                               
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'PNG to JPG'
                              
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'JPG to JPEG'
                            
                            FileChoose:
                                background_color: .5, .5, 1, 1
                                color: 0, 0, 0, 1
                                font_size: 45
                                background_normal: 'normal.png'
                                background_down: 'down.png'
                                border: 30,30,30,30
                                size_hint_y: None
                                height: 120
                                on_release: self.choose()
                                text: 'JPEG to JPG'

        '''))


if __name__ == '__main__':
    ChooserApp().run()
